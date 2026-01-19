from .Rule import Rule



class Always400IfPayload(Rule):


    id = "always-400-if-payload"
    description = "Always implement a response with the status code '400 Bad Request' if the method contains a payload (for invalid syntax)."
    category = "standard"


    @classmethod
    def _check(cls, data):

        method_name = data.get("method-name", "")
        status_codes = data.get("status-codes", [])

        if method_name not in ("post", "put", "patch"):
            return True
        
        return "400" in status_codes