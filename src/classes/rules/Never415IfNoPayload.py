from .Rule import Rule


class Never415IfNoPayload(Rule):


    id = "never-415-if-no-payload"
    description = "Never implement a response with the status code '415 Unsupported Media Type' if the method does not contain a payload."
    category = "standard"


    @classmethod
    def _check(cls, data):

        method_name = data.get("method-name", "")
        status_codes = data.get("status-codes", [])

        if method_name in ("post", "put", "patch"):
            return True

        return "415" not in status_codes