from .Rule import Rule
from config import SOURCES


class Has422IfParams(Rule):


    description = "Always implement a response with the status code '422 Unprocessable Content' if the method contains parameters (in case of invalid semantics)."
    sources = [SOURCES["422"]]


    @classmethod
    def _check(cls, data):

        status_codes = data.get("status-codes", [])
        has_path_parameters = data.get("has-path-parameters", False)
        has_query_parameters = data.get("has-query-parameters", False)

        if not has_path_parameters and not has_query_parameters:
            return True
        
        return "422" in status_codes