import json
from pathlib import Path


PROJECT_ROOT = Path(__file__).parent.parent
DATA_PATH = PROJECT_ROOT / "data"


def load_json(filename):
    with open(DATA_PATH / filename, encoding="utf-8") as file:
        return json.load(file)


STATUS_CODES = load_json("codes.json")
CONFIG = load_json("config.json")