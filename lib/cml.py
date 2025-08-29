from collections.abc import Mapping
from io import TextIOWrapper


class CML:

    @staticmethod
    def __tokenize(content) -> list[str]:
        line = ' '.join([x.strip() for x in content.splitlines() if x.strip() != ""])
        if not line:
            return []

        separators = set('<>+-')
        stack = []
        tokens = []

        for char in line:
            if char in separators:
                if stack:
                    tokens.append(''.join(stack).strip())
                    stack.clear()
            stack.append(char)

        return tokens


    @staticmethod
    def load(stream: TextIOWrapper) -> Mapping:

        root = {}
        stack = []

        cur_map = root

        for token in CML.__tokenize(stream.read()):

            if token.startswith('<'):
                key = token[1:].strip()
                new_map = {}
                cur_map[key] = new_map
                stack.append(new_map)
                cur_map = new_map

            elif token == '>':
                if len(stack) > 1:
                    stack.pop()
                    cur_map = stack[-1]

            elif token.startswith('+'):
                if 'pros' not in cur_map:
                    cur_map['pros'] = []
                cur_map['pros'].append(token[1:].strip())

            elif token.startswith('-'):
                if 'cons' not in cur_map:
                    cur_map['cons'] = []
                cur_map['cons'].append(token[1:].strip())

            elif not token:
                continue

            else:
                raise ValueError

        return root