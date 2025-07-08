from io import TextIOWrapper
from treelib import Tree


INTEND_CHAR = "\t"
(IN, PRO, CON, OUT) = range(4)

types = {
    '<': IN,
    '+': PRO,
    '-': CON,
    '>': OUT
}


def populate_tree(t:Tree, f:TextIOWrapper):
    lines = f.readlines()
    for i in range(0, len(lines)):
        line = lines[i].rstrip("\n")
        if len(line) == 0:
            continue
        type = line.lstrip(INTEND_CHAR)[0]
        tag = line.lstrip(INTEND_CHAR).lstrip(type).lstrip(' ')
        intend = line.count(INTEND_CHAR)
        print(intend, types[type], tag)

        if intend == types[type] == i == 0:
            t.create_node(line, type, None, types[type])
        # TODO: here goes tree population
        else:
            raise ValueError



tree = Tree()
with open("example.q", 'r') as f:
    populate_tree(tree, f)
tree.show()