from .Rule import Rule


class Never204ForContent(Rule):


    id = "never-204-for-content"
    description = "Never implement a response with the status code '204 No Content' if the response content is not empty."
    category = "standard"


    @classmethod
    def _check(cls, data):

        status_codes = data.get("status-codes", [])

        if "204" not in status_codes:
            return True
        
        response_content_204 = data.get("method-data", {}).get("responses", {}).get("204", {}).get("content", {})

        if response_content_204:
            return False
        
        return True