import json
import os
import yaml

import lib.cml as cml

def load(file_path):
    _, ext = os.path.splitext(file_path)
    match ext.lower():
        case ".cml":
            func = cml.load
        case ".json":
            func = json.load
        case ".yml" | ".yaml":
            func = yaml.safe_load
        case _:
            raise NotImplementedError
    with open(file_path, 'r') as stream:
        return func(stream)
