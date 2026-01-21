from .Rule import Rule


class Always204For2xxNoContent(Rule):


    id = "always-204-for-2xx-no-content"
    description = "Always implement a response with the status code '204 No Content' if a successful ('2xx') response content is empty."
    category = "standard"


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