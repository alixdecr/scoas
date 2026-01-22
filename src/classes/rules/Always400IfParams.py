from .Rule import Rule
from config import SOURCES


class Always400IfParams(Rule):


    id = "always-400-if-params"
    description = "Always implement a response with the status code '400 Bad Request' if the method contains parameters (in case of invalid syntax)."
    sources = [SOURCES["400"]]


    @classmethod
    def _check(cls, data):

        status_codes = data.get("status-codes", [])
        has_path_parameters = data.get("has-path-parameters", False)
        has_query_parameters = data.get("has-query-parameters", False)

        if not has_path_parameters and not has_query_parameters:
            return True
        
        return "400" in status_codes