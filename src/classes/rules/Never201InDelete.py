from .Rule import Rule
from config import SOURCES


class Never201InDelete(Rule):


    id = "never-201-in-delete"
    description = "Never implement a response with the status code '201 Created' in a 'DELETE' method (as it can never create data)."
    sources = [SOURCES["201"], SOURCES["delete"]]


    @classmethod
    def _check(cls, data):

        method_name = data.get("method-name", "")
        status_codes = data.get("status-codes", [])

        if method_name != "delete":
            return True
        
        return "201" not in status_codes