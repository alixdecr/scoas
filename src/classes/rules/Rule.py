import logging
from abc import ABC, abstractmethod


logger = logging.getLogger(__name__)


class Rule(ABC):


    id: str
    description: str
    category: str


    @classmethod
    def check(cls, data):

        route = data.get("route-name", "")
        status_codes = ",".join(data.get("status-codes", []))

        result = cls._check(data)

        if result:
            logger.info(f"Result of rule '{cls.id}' for '{route}' with responses '{status_codes}': PASS")
        else:
            logger.warning(f"Result of rule '{cls.id}' for '{route}' with responses '{status_codes}': FAIL")

        return result


    @classmethod
    @abstractmethod
    def _check(cls, data):

        pass