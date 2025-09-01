from collections.abc import Mapping

class Choice:
    results: Mapping

    def __init__(self):
        self.results = {}

    def evaluate(self, data, stack=None):
        if stack is None:
            stack = []

        if isinstance(data, Mapping):
            for key, value in data.items():
                new_path = stack + [key]

                if 'pros' in value or 'cons' in value:
                    pros = value.get('pros', [])
                    cons = value.get('cons', [])
                    path_str = "::".join(new_path)
                    self.results[path_str] = {
                        'pros': len(pros),
                        'cons': len(cons),
                        'total': len(pros) - len(cons)
                    }

                self.evaluate(value, new_path)
        return self.results

    def choose(self):
        return [
            (option, stats)
            for option, stats in self.results.items()
            if stats['total'] == max(item['total'] for item in self.results.values())
        ]

    def print_result(self):
        for option, stats in self.results.items():
            print(f'> {option} ({stats['pros']} - {stats["cons"]} = {stats["total"]})')
        for option, stats in self.choose():
            print(f'< {option} ({stats['total']})')