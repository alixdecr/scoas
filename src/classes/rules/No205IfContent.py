from .Rule import Rule
from config import SOURCES


class No205IfContent(Rule):


    description = "Never implement a response with the status code '205 Reset Content' if its content is not empty. In the case of an OAS file, the response should not have a 'content' field."
    sources = [SOURCES["205"]]


    @classmethod
    def _check(cls, data):

        status_codes = data.get("status-codes", [])

        if "205" not in status_codes:
            return True
        
        response_content_205 = data.get("method-data", {}).get("responses", {}).get("205", {}).get("content", {})

        if response_content_205:
            return False
        
        return True