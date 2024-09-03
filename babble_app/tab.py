from dataclasses import dataclass
from enum import Enum, IntEnum

class Tab(IntEnum):
    CAM = 0
    SETTINGS = 1
    ALGOSETTINGS = 2


class CamInfoOrigin(Enum):
    MODEL = 1
    FAILURE = 2


@dataclass
class CamInfo:
    info_type: CamInfoOrigin
    output: str
