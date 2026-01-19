from .Rule import Rule


class Always406IfAccept(Rule):


    id = "always-406-if-accept"
    description = "Always implement a response with the status code '406 Not Acceptable' in case the sever does not support the 'Accept' header specified in the request."
    category = "standard"


    @classmethod
    def _check(cls, data):

        status_codes = data.get("status-codes", [])

        return "406" in status_codes