from collections.abc import Mapping
from io import TextIOWrapper


class CML:

    @staticmethod
    def __tokenize(content):
        lines = [ln.strip() for ln in content.splitlines() if ln.strip() != ""]

        # parsing oneliners
        if len(lines) == 1:
            line = lines[0]
            stack = []
            tokens = []
            i = 0
            while True:
                if i == len(line)-1:
                    tokens.append('>')
                    return tokens
                if line[i]:
                    stack.append(line[i])
                if line[i+1] in ('<', '>', '+', '-'):
                    tokens.append(''.join(stack).strip())
                    stack.clear()
                i += 1

        # else use splitted lines from above
        else:
            return [x.strip() for x in lines]

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