import logging, re
from abc import ABC, abstractmethod


logger = logging.getLogger(__name__)


class Rule(ABC):


    id: str
    description: str
    category: str


    def __init_subclass__(cls):

        super().__init_subclass__()
        # automatically generate the class ID based on the class name -> MyRule becomes my-rule
        name = re.sub(r"(?<!^)(?=[A-Z]|(?<=\D)(?=\d))", "-", cls.__name__).lower()
        cls.id = name.lower()


    @classmethod
    def check(cls, data):

        route = data.get("route-name", "")
        status_codes = ",".join(data.get("status-codes", []))

        result = cls._check(data)

        if result:
            logger.info(f"Rule '{cls.id}' for '{route}' with responses '{status_codes}': PASS")
        else:
            logger.warning(f"Rule '{cls.id}' for '{route}' with responses '{status_codes}': FAIL")

        return result


    @classmethod
    @abstractmethod
    def _check(cls, data):

        pass