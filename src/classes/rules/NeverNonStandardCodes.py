from .Rule import Rule
from config import SOURCES
from config import STATUS_CODES


class NeverNonStandardCodes(Rule):


    id = "never-non-standard-codes"
    description = "Never implement responses with non-standard status codes."
    sources = [SOURCES["standard-status-codes"]]


    @classmethod
    def _check(cls, data):

        status_codes = data.get("status-codes", [])

        has_non_standard = any(code not in list(STATUS_CODES.keys()) for code in status_codes)

        return not has_non_standard