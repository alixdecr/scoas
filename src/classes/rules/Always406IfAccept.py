from .Rule import Rule
from config import SOURCES


class Always406IfAccept(Rule):


    id = "always-406-if-accept"
    description = "Always implement a response with the status code '406 Not Acceptable' in case the sever does not support the 'Accept' header specified in the request. Only applies to routes that respond with content."
    sources = [SOURCES["406"], SOURCES["Accept"]]


    @classmethod
    def _check(cls, data):

        status_codes = data.get("status-codes", [])
        method_responses = data.get("method-data", {}).get("responses", {})
        
        # only check the rule for methods that actually return content
        has_content = False

        for code in method_responses:
            if method_responses.get(code, {}).get("content", {}):
                has_content = True
                break

        if not has_content:
            return True

        return "406" in status_codes