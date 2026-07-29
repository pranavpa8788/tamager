from enum import Enum, auto

#TODO: in future these can be custom?
class STATUS(Enum):
    TODO = auto()
    IN_PROGRESS = auto()
    BLOCKED = auto()
    DONE = auto()