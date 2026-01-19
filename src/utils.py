import json
import logging
from pathlib import Path


logger = logging.getLogger(__name__)


def load_json(file_path):

    logger.info(f"Attempting to load JSON file from '{file_path}'")

    file_path = Path(file_path)

    if not file_path.exists():
        logger.warning(f"JSON file does not exist in '{file_path}'")
        return None

    try:
        with file_path.open(encoding="utf-8") as file:
            file = json.load(file)

            logger.info(f"Loaded JSON file from '{file_path}'")

            return file
        
    except json.JSONDecodeError as e:
        logger.error(f"Failed to decode JSON file '{file_path}': {e}")
        return None

    except Exception as e:
        logger.error(f"Unexpected error while loading JSON file '{file_path}': {e}")
        return None


def save_json(file_path, data):

    file_path = Path(file_path)
    file_path.parent.mkdir(parents=True, exist_ok=True)

    with file_path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    logger.info(f"Saved JSON file to '{file_path}'")