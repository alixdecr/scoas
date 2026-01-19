from .Rule import Rule


class Always200Or204InDelete(Rule):


    id = "always-200-or-204-in-delete"
    description = "Always implement a response with the status code '200 OK' or '204 No Content' in a DELETE method."
    category = "standard"


    @classmethod
    def _check(cls, data):

        method_name = data.get("method-name", "")
        status_codes = data.get("status-codes", [])

        if method_name != "delete":
            return True

        return "204" in status_codes or "200" in status_codes