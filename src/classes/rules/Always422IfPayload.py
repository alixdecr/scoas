from .Rule import Rule
from config import SOURCES


class Always422IfPayload(Rule):


    id = "always-422-if-payload"
    description = "Always implement a response with the status code '422 Unprocessable Content' if the method contains a payload (for invalid semantic)."
    sources = [SOURCES["422"]]


    @classmethod
    def _check(cls, data):

        method_name = data.get("method-name", "")
        status_codes = data.get("status-codes", [])

        if method_name not in ("post", "put", "patch"):
            return True
        
        return "422" in status_codes