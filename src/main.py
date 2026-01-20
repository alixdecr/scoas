import logging
import time
import utils
from config import LOGS_PATH, OAS_PATH, TIMESTAMP
from classes.Checker import Checker


# --------------
# LOGGING SETUP
# --------------
LOG_FILE = LOGS_PATH / f"{TIMESTAMP}.log"

logging.basicConfig(
    encoding="utf-8",
    level=logging.INFO,
    format="{asctime} | {levelname:<8} | {filename:<25} | {funcName:<25} | {lineno:<4} | {message}",
    style="{",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


# ---------------
# MAIN EXECUTION
# ---------------
def main():

    if not OAS_PATH.exists() or not OAS_PATH.is_dir():
        logger.error(f"OAS path does not exist or is not a directory: '{OAS_PATH}'")
        return
    
    for file_path in OAS_PATH.glob("*.json"):
        try:
            name = file_path.stem
            oas = utils.load_json(file_path)

            logger.info(f"Processing OAS file '{file_path.name}'")
        
            checker = Checker(name, oas)
            checker.execute()

        except Exception as e:
            logger.error(f"Failed to process OAS file '{file_path.name}'")
            logger.error(e)


if __name__ == "__main__":
    main()