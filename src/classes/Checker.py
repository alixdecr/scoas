import logging
import utils
import re
from jinja2 import Environment, FileSystemLoader
from config import OUT_PATH, TEMPLATE_PATH, STATUS_CODES, TIMESTAMP
from .rules import RULES


logger = logging.getLogger(__name__)


class Checker:


    def __init__(self, name, oas):

        self.name = name
        self.oas = oas
        self.execution = {
            "name": name,
            "timestamp": TIMESTAMP,
            "nb-routes": 0,
            "nb-routes-without-violations": 0,
            "status-codes": {
                "total": 0,
                "by-code": {}
            },
            "rule-violations": {
                "total": 0,
                "average-per-route": 0,
                "by-rule": {},
                "list": []
            }
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

                self.execution["nb-routes"] += 1

                route_name = f"{method_name.upper()} {path_name}"
                has_query_parameters = self.has_query_parameters(method_data) or has_common_query_parameters
                has_auth = self.has_auth(method_data)
                status_codes = []

                parameters = path_data.get("parameters", []) + method_data.get("parameters", [])
                parameter_list = []

                for param in parameters:
                    if "name" in param:
                        name = param["name"]
                        is_in = param.get("in", "unknown")
                        parameter_list.append(f"{name} ({is_in})")

                for code, code_data in method_data["responses"].items():
                    status_codes.append(code)
                    self.add_status_code(code)

                check_data = {
                    "method-name": method_name,
                    "method-data": method_data,
                    "status-codes": status_codes,
                    "route-name": route_name,
                    "has-path-parameters": has_path_parameters,
                    "has-query-parameters": has_query_parameters,
                    "has-auth": has_auth,
                    "parameter-list": parameter_list
                }

                logger.info(f"Checking route '{route_name}'")

                has_violations = self.check_rules(check_data)

                if not has_violations:
                    self.execution["nb-routes-without-violations"] += 1

        self.execution["rule-violations"]["average-per-route"] = round(self.execution["rule-violations"]["total"] / self.execution["nb-routes"], 2)

        OUT_FILE = OUT_PATH / self.name / "execution.json"

        utils.save_json(OUT_FILE, self.execution)

        self.generate_report()

        logger.info(f"Finished execution for '{self.name}'")


    def check_rules(self, check_data):

        has_violations = False

        for rule in RULES:
            if not rule.check(check_data):
                self.execution["rule-violations"]["list"].append(
                    {
                        "rule": {
                            "id": rule.id,
                            "description": rule.description,
                            "sources": rule.sources
                        },
                        "route": check_data["route-name"],
                        "status-codes": check_data["status-codes"],
                        "parameters": check_data["parameter-list"]
                    }
                )

                self.execution["rule-violations"]["total"] += 1

                if rule.id not in self.execution["rule-violations"]["by-rule"]:
                    self.execution["rule-violations"]["by-rule"][rule.id] = 0

                self.execution["rule-violations"]["by-rule"][rule.id] += 1

                has_violations = True


        return has_violations


    @staticmethod
    def has_path_parameters(path_name):

        return "{" in path_name and "}" in path_name
    

    @staticmethod
    def has_query_parameters(data):

        for parameter in data.get("parameters", []):
            if parameter.get("in") == "query":
                return True
                
        return False
    

    def has_auth(self, data):

        return "security" in self.oas or "security" in data
    

    def add_status_code(self, code):

        if code not in self.execution["status-codes"]["by-code"]:
            self.execution["status-codes"]["by-code"][code] = 0

        self.execution["status-codes"]["by-code"][code] += 1
        self.execution["status-codes"]["total"] += 1


    def prepare_report_data(self):

        report_data = self.execution

        report_data["rule-violations"]["by-rule"] = dict(sorted(report_data["rule-violations"]["by-rule"].items(), key=lambda item: item[1], reverse=True))

        for violation in report_data["rule-violations"]["list"]:
            violation["rule"]["description"] = re.sub(r"'([^']+)'", r"<code>\1</code>", violation["rule"]["description"])

            violation["rule"]["sources"] = " | ".join(violation["rule"]["sources"])

            # transform the status code list into a string list of status codes with their corresponding names (200 OK, 404 Not Found, etc)
            violation["status-codes"] = ", ".join(
                f"{code_id} {STATUS_CODES.get(code_id, {}).get("name", "Unknown")}"
                for code_id in violation.get("status-codes", [])
            )

            if violation["parameters"]:
                violation["parameters"] = ", ".join(violation["parameters"])
            else:
                violation["parameters"] = "/"

        return report_data


    def generate_report(self):

        OUT_FILE = OUT_PATH / self.name / "report.html"

        TEMPLATE_DIR = str(TEMPLATE_PATH.parent)
        TEMPLATE_FILE = str(TEMPLATE_PATH.name)

        env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
        template = env.get_template(TEMPLATE_FILE)

        report_data = self.prepare_report_data()

        report = template.render(data=report_data)

        utils.save_data(OUT_FILE, report)