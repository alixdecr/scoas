from .Rule import Rule
from config import SOURCES


class No501IfImplemented(Rule):


    description = "Never implement a response with the status code '501 Not Implemented' if the request method is actually implemented. In the case of an OAS file, the code should not appear at all."
    sources = [SOURCES["501"]]


    @classmethod
    def _check(cls, data):

        status_codes = data.get("status-codes", [])

        return "501" not in status_codes