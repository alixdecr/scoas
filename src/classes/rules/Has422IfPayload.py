from .Rule import Rule
from config import SOURCES


class Has422IfPayload(Rule):


    description = "Always implement a response with the status code '422 Unprocessable Content' if the method contains a payload (in case of invalid semantics)."
    sources = [SOURCES["422"]]


    @classmethod
    def _check(cls, data):

        method_name = data.get("method-name", "")
        status_codes = data.get("status-codes", [])

        if method_name not in ("post", "put", "patch"):
            return True
        
        return "422" in status_codes