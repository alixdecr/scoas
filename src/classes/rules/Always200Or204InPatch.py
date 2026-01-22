from .Rule import Rule
from config import SOURCES


class Always200Or204InPatch(Rule):


    id = "always-200-or-204-in-patch"
    description = "Always implement a response with the status code '200 OK' or '204 No Content' in a 'PATCH' method."
    sources = [SOURCES["200"], SOURCES["204"], SOURCES["patch"]]


    @classmethod
    def _check(cls, data):

        method_name = data.get("method-name", "")
        status_codes = data.get("status-codes", [])

        if method_name != "patch":
            return True

        return "204" in status_codes or "200" in status_codes