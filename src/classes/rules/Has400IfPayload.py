from .Rule import Rule
from config import SOURCES


class Has400IfPayload(Rule):


    description = "Always implement a response with the status code '400 Bad Request' if the method contains a payload (in case of invalid syntax)."
    sources = [SOURCES["400"]]


    @classmethod
    def _check(cls, data):

        method_name = data.get("method-name", "")
        status_codes = data.get("status-codes", [])

        if method_name not in ("post", "put", "patch"):
            return True
        
        return "400" in status_codes