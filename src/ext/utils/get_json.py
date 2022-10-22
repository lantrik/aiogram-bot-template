from typing import Dict

from json import load


def get_json(json_name: str) -> Dict[str, str]:
    with open(f"src/content/templates/{json_name}.json") as file:
        json = load(file)

    return json
