from collections.abc import Iterable, Mapping
from io import TextIOWrapper


class CML:

    @staticmethod
    def __tokenize(content):
        return [x.strip() for x in content.split('\n')]

    @staticmethod
    def load(stream: TextIOWrapper):

        def parse(tokens: Iterable) -> Mapping:

            root = {}
            stack = []

            cur_map = root

            for token in tokens:

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

        return parse(CML.__tokenize(stream.read()))