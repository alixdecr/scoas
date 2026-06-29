from .Rule import Rule
from config import SOURCES


class No405IfNoAllow(Rule):


    description = "Never implement a response with the status code '405 Method Not Allowed' if it does not return an 'Allow' header."
    sources = [SOURCES["405"], SOURCES["Allow"]]


    @classmethod
    def _check(cls, data):

        status_codes = data.get("status-codes", [])

        if "405" not in status_codes:
            return True
        
        response_headers_405 = data.get("method-data", {}).get("responses", {}).get("405", {}).get("headers", {})

        return "Allow" in response_headers_405