from .Rule import Rule
from config import SOURCES


class No401IfNoWWWAuthenticate(Rule):


    description = "Never implement a response with the status code '401 Unauthorized' if it does not return a 'WWW-Authenticate' header."
    sources = [SOURCES["401"], SOURCES["WWW-Authenticate"]]


    @classmethod
    def _check(cls, data):

        status_codes = data.get("status-codes", [])

        if "401" not in status_codes:
            return True
        
        response_headers_401 = data.get("method-data", {}).get("responses", {}).get("401", {}).get("headers", {})

        return "WWW-Authenticate" in response_headers_401