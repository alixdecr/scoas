from .Rule import Rule


class Always413IfContentLength(Rule):


    id = "always-413-if-content-length"
    description = "Always implement a response with the status code '413 Content Too Large' in case the server does not support the 'Content-Length' header specified in the request."
    category = "standard"


    @classmethod
    def _check(cls, data):

        method_name = data.get("method-name", "")
        status_codes = data.get("status-codes", [])

        if method_name not in ("post", "put", "patch"):
            return True

        return "413" in status_codes