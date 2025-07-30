import argparse

from lib.data import Choice
from lib.file import File


def main(file):
    data = File.load(file)
    choice = Choice()
    choice.evaluate(data)

    for option, stats in choice.results.items():
        print(f'> {option} ({stats['pros']} - {stats["cons"]} = {stats["total"]})')

    for best_option, best_stats in choice.choose():
        print(f'< {best_option} ({best_stats['total']})')


if __name__ == "__main__":
    argparse = argparse.ArgumentParser()
    argparse.add_argument("-f", "--file", required=True)
    args = argparse.parse_args()
    main(args.file)
