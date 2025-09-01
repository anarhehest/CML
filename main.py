import argparse

from lib.file import load
from lib.choice import Choice


def main(args):
    data = load(args.file)
    choice = Choice()
    choice.evaluate(data)
    choice.print_result()


if __name__ == "__main__":
    argparse = argparse.ArgumentParser()
    argparse.add_argument("-f", "--file", required=True)
    main(argparse.parse_args())
