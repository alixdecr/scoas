import json, logging, os


logger = logging.getLogger(__name__)


def load_json(path):

    logger.info(f"Attempting to load JSON file from '{path}'")

    try:
        with open(path, "r", encoding="utf-8-sig") as file:
            file = json.load(file)

            logger.info(f"Successfully loaded JSON file from '{path}'")

            return file

    except Exception as e:
        logger.error(f"Failed to load JSON file from '{path}'")
        logger.error(e)

        return {}


def save_json(path, data):

    # first, attempt to create the folders leading to the file if they do not exist yet
    dir_path = os.path.dirname(path)
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)

    with open(path, "w", encoding="utf-8-sig") as file:
        json.dump(data, file, indent=4)

    logger.info(f"Saved JSON file to '{path}'")