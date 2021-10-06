from dataclasses import dataclass
from enum import Enum


class SewerType(Enum):
    NONE = 1
    YES = 2
    STORM = 3
    MUNICIPAL = 4
    SEPTIC = 5


@dataclass
class PropertySewer:
    address: str
    zip_code: str
    sewer: SewerType
