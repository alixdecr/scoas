from .Rule import Rule


class Always201InCreate(Rule):


    id = "always-201-in-create"
    description = "Always implement a response with the status code '201 Created' if the method can create data (POST or PUT)."
    category = "standard"


    @classmethod
    def _check(cls, data):

        method_name = data.get("method-name", "")
        status_codes = data.get("status-codes", [])

        if method_name not in ("post", "put"):
            return True

        return "201" in status_codes