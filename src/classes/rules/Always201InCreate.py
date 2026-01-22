from .Rule import Rule
from config import SOURCES


class Always201InCreate(Rule):


    id = "always-201-in-create"
    description = "Always implement a response with the status code '201 Created' if the method can create data ('POST' or 'PUT')."
    sources = [SOURCES["201"], SOURCES["post"], SOURCES["put"]]


    @classmethod
    def _check(cls, data):

        method_name = data.get("method-name", "")
        status_codes = data.get("status-codes", [])

        if method_name not in ("post", "put"):
            return True

        return "201" in status_codes