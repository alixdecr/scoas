from .Rule import Rule
from config import SOURCES


class Always204ForSuccessWithNoContent(Rule):


    id = "always-204-for-success-with-no-content"
    description = "Always implement a response with the status code '204 No Content' if a response in the '2xx Successful' range does not have content."
    sources = [SOURCES["204"], SOURCES["2xx"]]


    @classmethod
    def _check(cls, data):

        method_responses = data.get("method-data", {}).get("responses", {})

        for code in method_responses:
            # because only 2xx status codes are impacted by this rule
            if code[0] == "2":
                response_data = method_responses.get(code)

                if response_data:
                    content = response_data.get("content", {})

                    if not content and code != "204":
                        return False
                    
        return True