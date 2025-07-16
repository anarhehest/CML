import json
from treelib import Tree

with open("examples/example.json", "r") as f:
    data = json.load(f)

print(data)


class CML:
    (IN, PLUS, MINUS, OUT) = range(4)
    _ml = {
        '<': IN,
        '+': PLUS,
        '-': MINUS,
        '>': OUT,
    }

    normalize = lambda x: x.replace('\n', ' ').replace('\r', '').replace('    ', '').replace('\t', '').strip()

    def __init__(self):
        self.root = None
        self.tree = Tree()


    def process(self, tokens, tree:Tree, i=0):
        if i == len(tokens):
            return tree, tokens
        try:
            # TODO: ну надо чёто этсамое, тыры-пыры, непонятно как это вообще реализовать
            ml, text = tokens[i][0], tokens[i][2:]
            print(ml, text)
        except IndexError:
            if tokens[i] == ">":
                ml = tokens[i]
                print(ml)
        return self.process(tokens, tree, i+1)


cml = CML()
with open("examples/example.cml", "r") as f:
    tokens = list(map(CML.normalize, f.readlines()))
    data = cml.process(tokens, cml.tree)

print(data[1])
data[0].show()
