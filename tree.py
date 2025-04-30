import io
from typing import List

(IN, OPT, PRO, CON, QUE, STAR, HASH,) = range(7)

class Node:
    counter = 0

    def __init__(self, mode, value, depth):
        self.id: int = Node.counter
        Node.counter += 1
        self.mode: int = mode
        self.value: int = value
        self.depth: int = depth
        self.children: List[Node] = list()
        self.links: List[Node] = list()


class Tree:
    root:Node

    def __init__(self, f:io.TextIOWrapper):
        for l in f.readlines():
            if l.startswith('<'):
                self.root = Node(0, IN, 0, dict())


if __name__ == "__main__":
    print(Tree(open('example.q')))
