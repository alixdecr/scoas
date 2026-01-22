from .Rule import Rule
from config import SOURCES


class Always200Or204InUpdate(Rule):


    id = "always-200-or-204-in-update"
    description = "Always implement a response with the status code '200 OK' or '204 No Content' in a 'PUT' or 'PATCH' method."
    sources = [SOURCES["200"], SOURCES["204"], SOURCES["put"], SOURCES["patch"]]


    @classmethod
    def _check(cls, data):

        method_name = data.get("method-name", "")
        status_codes = data.get("status-codes", [])

        if method_name not in ("put", "patch"):
            return True

        return "204" in status_codes or "200" in status_codes