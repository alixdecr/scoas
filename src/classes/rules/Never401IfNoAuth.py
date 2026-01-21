from .Rule import Rule


class Never401IfNoAuth(Rule):


    id = "never-401-if-no-auth"
    description = "Never implement a response with the status code '401 Unauthorized' if the specification does not contains an authentication mechanism."
    category = "rest"


    @classmethod
    def _check(cls, data):

        status_codes = data.get("status-codes", [])
        has_auth = data.get("has-auth", False)

        if "401" not in status_codes:
            return True
        
        return has_auth