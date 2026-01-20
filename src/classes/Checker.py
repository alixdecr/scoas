import logging
import utils
from config import OUT_PATH
from .rules import RULES


logger = logging.getLogger(__name__)


class Checker:


    def __init__(self, name, oas):

        self.name = name
        self.oas = oas
        self.execution = {
            "status-codes": {},
            "rule-violations": []
        }


    def execute(self):

        logger.info(f"Starting execution for '{self.name}'")

        if not self.oas or "paths" not in self.oas:
            logger.error("Empty or invalid OAS file")
            return
        
        for path_name, path_data in self.oas["paths"].items():

            has_path_parameters = self.has_path_parameters(path_name)
            has_common_query_parameters = self.has_query_parameters(path_data)

            for method_name, method_data in path_data.items():

                if method_name not in ("get", "post", "put", "patch", "delete"):
                    continue

                route_name = f"{method_name.upper()} {path_name}"
                has_query_parameters = self.has_query_parameters(method_data) or has_common_query_parameters
                status_codes = []

                for code_name, code_data in method_data["responses"].items():
                    status_codes.append(code_name)
                    self.add_status_code(code_name)
                    logger.info(f"Found response '{code_name}' in '{route_name}'")

                check_data = {
                    "method-name": method_name,
                    "method-data": method_data,
                    "status-codes": status_codes,
                    "route-name": route_name,
                    "has-path-parameters": has_path_parameters,
                    "has-query-parameters": has_query_parameters
                }

                self.check_rules(check_data)

        OUT_FILE = OUT_PATH / self.name / "execution.json"

        utils.save_json(OUT_FILE, self.execution)

        logger.info(f"Finished execution for '{self.name}'")


    def check_rules(self, check_data):

        for rule in RULES:
            if not rule.check(check_data):
                self.execution["rule-violations"].append(
                    {
                        "rule": rule.id,
                        "route": check_data["route-name"],
                        "status-codes": check_data["status-codes"]
                    }
                )


    @staticmethod
    def has_path_parameters(path_name):

        return "{" in path_name and "}" in path_name
    

    @staticmethod
    def has_query_parameters(data):

        for parameter in data.get("parameters", []):
            if parameter.get("in") == "query":
                return True
                
        return False
    

    def add_status_code(self, code):

        if code not in self.execution["status-codes"]:
            self.execution["status-codes"][code] = 0

        self.execution["status-codes"][code] += 1