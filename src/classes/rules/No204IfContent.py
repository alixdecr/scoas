from .Rule import Rule
from config import SOURCES


class No204IfContent(Rule):


    description = "Never implement a response with the status code '204 No Content' if its content is not empty. In the case of an OAS file, the response should not have a 'content' field."
    sources = [SOURCES["204"]]


    @classmethod
    def _check(cls, data):

        status_codes = data.get("status-codes", [])

        if "204" not in status_codes:
            return True
        
        response_content_204 = data.get("method-data", {}).get("responses", {}).get("204", {}).get("content", {})

        if response_content_204:
            return False
        
        return True