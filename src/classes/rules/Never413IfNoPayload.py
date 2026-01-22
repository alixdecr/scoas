from .Rule import Rule
from config import SOURCES


class Never413IfNoPayload(Rule):


    id = "never-413-if-no-payload"
    description = "Never implement a response with the status code '413 Content Too Large' if the method does not contain a payload."
    sources = [SOURCES["413"]]


    @classmethod
    def _check(cls, data):

        method_name = data.get("method-name", "")
        status_codes = data.get("status-codes", [])

        if method_name in ("post", "put", "patch"):
            return True

        return "413" not in status_codes