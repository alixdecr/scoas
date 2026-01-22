from .Rule import Rule
from config import SOURCES


class Always422IfParams(Rule):


    id = "always-422-if-params"
    description = "Always implement a response with the status code '422 Unprocessable Content' if the method contains parameters (for invalid semantic)."
    sources = [SOURCES["422"]]


    @classmethod
    def _check(cls, data):

        status_codes = data.get("status-codes", [])
        has_path_parameters = data.get("has-path-parameters", False)
        has_query_parameters = data.get("has-query-parameters", False)

        if not has_path_parameters and not has_query_parameters:
            return True
        
        return "422" in status_codes