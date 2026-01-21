from .Rule import Rule



class Never200ForError(Rule):


    id = "never-200-for-error"
    description = "Never implement a response with the status code '200 OK' if the response content describes an error."
    category = "standard"


    @classmethod
    def _check(cls, data):

        status_codes = data.get("status-codes", [])

        if "200" not in status_codes:
            return True

        try:
            response_message_200 = data["method-data"]["responses"]["200"]["description"]
        except KeyError:
            response_message_200 = ""

        return not ("error" in response_message_200 or "bad request" in response_message_200 or "invalid" in response_message_200)