from .Rule import Rule
from config import SOURCES


class No401IfNoAuth(Rule):


    description = "Never implement a response with the status code '401 Unauthorized' if the specification does not contains an authentication mechanism."
    sources = [SOURCES["401"]]


    @classmethod
    def _check(cls, data):

        status_codes = data.get("status-codes", [])
        has_auth = data.get("has-auth", False)

        if "401" not in status_codes:
            return True
        
        return has_auth