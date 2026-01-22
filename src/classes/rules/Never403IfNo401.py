from .Rule import Rule
from config import SOURCES


class Never403IfNo401(Rule):


    id = "never-403-if-no-401"
    description = "Never implement a response with the status code '403 Forbidden' if the method does not implement a response with the status code '401 Unauthorized'."
    sources = [SOURCES["403"], SOURCES["401"]]


    @classmethod
    def _check(cls, data):

        status_codes = data.get("status-codes", [])

        if "403" not in status_codes:
            return True
        
        return "401" in status_codes