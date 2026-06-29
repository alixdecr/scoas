from .Rule import Rule
from config import SOURCES


class No304IfNoGetOrHead(Rule):


    description = "Never implement a response with the status code '304 Not Modified' if the request method is not 'GET' or 'HEAD'."
    sources = [SOURCES["304"], SOURCES["get"], SOURCES["head"]]


    @classmethod
    def _check(cls, data):

        method_name = data.get("method-name", "")
        status_codes = data.get("status-codes", [])

        if method_name in ("get", "head"):
            return True

        return "304" not in status_codes