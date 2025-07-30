import argparse
import yaml
from collections.abc import Mapping


def load_data(file_path):
    with open(file_path, 'r') as stream:
        return yaml.safe_load(stream)


def evaluate(data, current_path=None, results=None):
    if results is None:
        results = {}
    if current_path is None:
        current_path = []

    if isinstance(data, Mapping):
        for key, value in data.items():
            new_path = current_path + [key]

            if 'pros' in value or 'cons' in value:
                pros = value.get('pros', [])
                cons = value.get('cons', [])
                path_str = "::".join(new_path)
                results[path_str] = {
                    'pros': len(pros),
                    'cons': len(cons),
                    'total': len(pros) - len(cons)
                }

            evaluate(value, new_path, results)
    return results


def choose(results):
    return max(results.items(), key=lambda x: x[1]['total'])


def main(file):
    data = load_data(file)
    results = evaluate(data)

    for option, stats in results.items():
        print(f'> {option} ({stats['pros']} - {stats["cons"]} = {stats["total"]})')

    best_option, best_stats = choose(results)
    print(f'< {best_option} ({best_stats['total']})')


if __name__ == "__main__":
    argparse = argparse.ArgumentParser()
    argparse.add_argument("-f", "--file", required=True)
    args = argparse.parse_args()
    main(args.file)
