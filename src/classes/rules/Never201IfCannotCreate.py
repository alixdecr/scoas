from .Rule import Rule
from config import SOURCES


class Never201IfCannotCreate(Rule):


    id = "never-201-if-cannot-create"
    description = "Never implement a response with the status code '201 Created' if the method cannot create data ('GET', 'PATCH', or 'DELETE')."
    sources = [SOURCES["201"], SOURCES["get"], SOURCES["patch"], SOURCES["delete"]]


    @classmethod
    def _check(cls, data):

        method_name = data.get("method-name", "")
        status_codes = data.get("status-codes", [])

        if method_name not in ("get", "patch", "delete"):
            return True
        
        return "201" not in status_codes