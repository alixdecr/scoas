from .Rule import Rule
from config import SOURCES


class Has200Or204IfDelete(Rule):


    description = "Always implement a response with the status code '200 OK' or '204 No Content' in a 'DELETE' method."
    sources = [SOURCES["200"], SOURCES["204"], SOURCES["delete"]]


    @classmethod
    def _check(cls, data):

        method_name = data.get("method-name", "")
        status_codes = data.get("status-codes", [])

        if method_name != "delete":
            return True

        return "200" in status_codes or "204" in status_codes