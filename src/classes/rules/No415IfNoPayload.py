from .Rule import Rule
from config import SOURCES


class No415IfNoPayload(Rule):


    description = "Never implement a response with the status code '415 Unsupported Media Type' if the method does not contain a payload."
    sources = [SOURCES["415"]]


    @classmethod
    def _check(cls, data):

        method_name = data.get("method-name", "")
        status_codes = data.get("status-codes", [])

        if method_name in ("post", "put", "patch"):
            return True

        return "415" not in status_codes