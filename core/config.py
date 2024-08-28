import json
from utils import path


def read(name: str):
    with open(f"{path.get_root_path()}/config/config.json", "r") as f:
        json_file = json.load(f)
    return json_file[name]