from .Rule import Rule
import data_loader


STANDARD_STATUS_CODES = list(data_loader.STATUS_CODES.keys())


class NeverNonStandardCodes(Rule):


    id = "never-non-standard-codes"
    description = "Never implement responses with non-standard status codes."
    category = "standard"


    @classmethod
    def _check(cls, data):

        status_codes = data.get("status-codes", [])

        has_non_standard = any(code not in STANDARD_STATUS_CODES for code in status_codes)

        return not has_non_standard