from .Rule import Rule


class Always415IfContentType(Rule):


    id = "always-415-if-content-type"
    description = "Always implement a response with the status code '415 Unsupported Media Type' in case the server does not support the 'Content-Type' header specified in the request."
    category = "standard"


    @classmethod
    def _check(cls, data):

        method_name = data.get("method-name", "")
        status_codes = data.get("status-codes", [])

        if method_name not in ("post", "put", "patch"):
            return True

        return "415" in status_codes