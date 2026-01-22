from .Rule import Rule
from config import SOURCES


class Never5xxIfNo4xx(Rule):


    id = "never-5xx-if-no-4xx"
    description = "Never implement a response with a status code in the range '5xx' if the route does not implement at least a response with a status code in the range '4xx'."
    sources = [SOURCES["5xx"], SOURCES["4xx"]]


    @classmethod
    def _check(cls, data):

        status_codes = data.get("status-codes", [])

        has_4xx = any(code[0] == "4" for code in status_codes)
        has_5xx = any(code[0] == "5" for code in status_codes)

        if not has_5xx:
            return True
        
        return has_4xx