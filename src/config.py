import json
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_PATH = PROJECT_ROOT / "data"
OAS_PATH = PROJECT_ROOT / "data" / "oas"
OUT_PATH = PROJECT_ROOT / "outputs"
LOGS_PATH = PROJECT_ROOT / "logs"

_PATHS_TO_CREATE = [
    OUT_PATH,
    LOGS_PATH
]

for _path in _PATHS_TO_CREATE:
    _path.mkdir(parents=True, exist_ok=True)

def _load_data(file_name):
    with open(DATA_PATH / file_name, encoding="utf-8") as file:
        return json.load(file)

STATUS_CODES = _load_data("status-codes.json")