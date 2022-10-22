from typing import Dict

from json import load


parrent: str = "src/content/templates"

def get_json(json_name: str) -> Dict[str, str]:
    with open(f"{parrent}/{json_name}.json") as file:
        json = load(file)

    return json
