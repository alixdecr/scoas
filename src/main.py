import logging, time, os
import data_loader
from classes.Checker import Checker
from utils import utils


# setup logger configuration
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    encoding="utf-8",
    level=logging.INFO,
    format="{asctime} | {levelname:<8} | {filename:<25} | {funcName:<25} | {lineno:<4} | {message}",
    style="{",
    handlers=[
        logging.FileHandler("logs/" + time.strftime("%Y-%m-%d-%H-%M") + ".log"),
        logging.StreamHandler()
    ]
)


CONFIG = data_loader.CONFIG


def main():
    
    oas_path = CONFIG["oas-path"]

    for file in os.listdir(oas_path):

        name = file.replace(".json", "")
        oas = utils.load_json(f"{oas_path}/{file}")
        
        checker = Checker(name, oas)
        checker.execute()


if __name__ == "__main__":
    main()