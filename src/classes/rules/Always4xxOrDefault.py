from .Rule import Rule
from config import SOURCES


class Always4xxOrDefault(Rule):


    id = "always-4xx-or-default"
    description = "Always implement a response with a status code in the '4xx' (client error) range or a 'default' response in case of a client and/or unexpected error."
    sources = [SOURCES["4xx"], SOURCES["openapi-default-response"]]


    @classmethod
    def _check(cls, data):

        status_codes = data.get("status-codes", [])
        has_4xx = any(code[0] == "4" for code in status_codes)
        has_default = "default" in status_codes

        return has_4xx or has_default