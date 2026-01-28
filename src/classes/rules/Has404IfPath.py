from .Rule import Rule
from config import SOURCES


class Has404IfPath(Rule):


    description = "Always implement a response with the status code '404 Not Found' if the method contains path parameters."
    sources = [SOURCES["404"]]


    @classmethod
    def _check(cls, data):

        status_codes = data.get("status-codes", [])
        has_path_parameters = data.get("has-path-parameters", False)

        if not has_path_parameters:
            return True
        
        return "404" in status_codes