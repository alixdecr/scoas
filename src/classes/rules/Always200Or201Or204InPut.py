from .Rule import Rule
from config import SOURCES


class Always200Or201Or204InPut(Rule):


    id = "always-200-or-201-or-204-in-put"
    description = "Always implement a response with the status code '200 OK', '201 Created', or '204 No Content' in a 'PUT' method."
    sources = [SOURCES["200"], SOURCES["201"], SOURCES["204"], SOURCES["put"]]


    @classmethod
    def _check(cls, data):

        method_name = data.get("method-name", "")
        status_codes = data.get("status-codes", [])

        if method_name != "put":
            return True

        return "200" in status_codes or "201" in status_codes or "204" in status_codes