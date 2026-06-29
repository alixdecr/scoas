from .Rule import Rule
from config import SOURCES


class No426IfNoUpgrade(Rule):


    description = "Never implement a response with the status code '426 Upgrade Required' if it does not return an 'Upgrade' header."
    sources = [SOURCES["426"], SOURCES["Upgrade"]]


    @classmethod
    def _check(cls, data):

        status_codes = data.get("status-codes", [])

        if "426" not in status_codes:
            return True
        
        response_headers_426 = data.get("method-data", {}).get("responses", {}).get("426", {}).get("headers", {})

        return "Upgrade" in response_headers_426