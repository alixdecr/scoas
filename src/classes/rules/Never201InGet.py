from .Rule import Rule
from config import SOURCES


class Never201InGet(Rule):


    id = "never-201-in-get"
    description = "Never implement a response with the status code '201 Created' in a 'GET' method (as it can never create data)."
    sources = [SOURCES["201"], SOURCES["get"]]


    @classmethod
    def _check(cls, data):

        method_name = data.get("method-name", "")
        status_codes = data.get("status-codes", [])

        if method_name != "get":
            return True
        
        return "201" not in status_codes