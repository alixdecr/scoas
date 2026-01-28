from .Rule import Rule
from config import SOURCES


class Has415IfContentType(Rule):


    description = "Always implement a response with the status code '415 Unsupported Media Type' in case the server does not support the 'Content-Type' header specified in the request."
    sources = [SOURCES["415"], SOURCES["Content-Type"]]


    @classmethod
    def _check(cls, data):

        method_name = data.get("method-name", "")
        status_codes = data.get("status-codes", [])

        if method_name not in ("post", "put", "patch"):
            return True

        return "415" in status_codes