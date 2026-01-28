from .Rule import Rule
from config import SOURCES


class No201IfPatch(Rule):


    description = "Never implement a response with the status code '201 Created' in a 'PATCH' method (as it can never create data)."
    sources = [SOURCES["201"], SOURCES["patch"]]


    @classmethod
    def _check(cls, data):

        method_name = data.get("method-name", "")
        status_codes = data.get("status-codes", [])

        if method_name != "patch":
            return True
        
        return "201" not in status_codes