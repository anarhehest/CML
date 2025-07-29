import sys
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
                path_str = " -> ".join(new_path)
                results[path_str] = {
                    'pros_count': len(pros),
                    'cons_count': len(cons),
                    'total': len(pros) - len(cons)
                }

            evaluate(value, new_path, results)
    return results


def choice(results):
    return max(results.items(), key=lambda x: x[1]['total'])


def main(*args):
    data = load_data(args[0][1])
    results = evaluate(data)

    print("Details:")
    for option, stats in results.items():
        print(f"\n{option}")
        print(f"\tPros: {stats['pros_count']}")
        print(f"\tCons: {stats['cons_count']}")
        print(f"\tTotal: {stats['total']}")

    best_option, best_stats = choice(results)
    print(f"\n★ Best choice: {best_option} (Total: {best_stats['total']})")


if __name__ == "__main__":
    main(sys.argv)
