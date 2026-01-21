from .Rule import Rule


class Always200InGet(Rule):


    id = "always-200-in-get"
    description = "Always implement a response with the status code '200 OK' in a 'GET' method."
    category = "standard"


    @classmethod
    def _check(cls, data):

        method_name = data.get("method-name", "")
        status_codes = data.get("status-codes", [])

        if method_name != "get":
            return True

        return "200" in status_codes