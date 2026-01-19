import logging
import time
import utils
from pathlib import Path
from data_loader import CONFIG
from classes.Checker import Checker


# --------------
# LOGGING SETUP
# --------------
LOG_PATH = Path("logs")
LOG_PATH.mkdir(exist_ok=True)
TIMESTAMP = time.strftime("%Y-%m-%d-%H-%M")
LOG_FILE = LOG_PATH / f"{TIMESTAMP}.log"

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
    
    oas_path = Path(CONFIG["oas-path"])

    if not oas_path.exists() or not oas_path.is_dir():
        logger.error(f"OAS path does not exist or is not a directory: '{oas_path}'")
        return
    
    for file_path in oas_path.glob("*.json"):
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