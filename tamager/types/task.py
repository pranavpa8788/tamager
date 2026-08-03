from uuid import UUID, uuid4
from datetime import datetime
from dataclasses import dataclass, field

from tamager.types.tag import TAG
from tamager.types.status import STATUS
from tamager.types.category import CATEGORY
from tamager.types.priority import PRIORITY
from tamager.types.time.time_log import TimeLog
from tamager.types.time.time_block import TimeBlock

#TODO: move start_time and stop_time into a separate time block object and add field for time log record

@dataclass
class Task:
    title: str
    description: str
    status: STATUS

    id: UUID = field(default_factory=uuid4)
    priority: PRIORITY | None = None
    category: CATEGORY | None = None
    tag: TAG | None = None
    time_block: TimeBlock | None = None
    time_log: TimeLog | None = None

    def __eq__(self, other) -> bool:
        if other.__class__ is self.__class__:
            return self.id == other.id
        else:
            #TODO: Replace with custom exception
            raise Exception(f"Unexpected comparison between classes: {self.__class__} and {other.__class__}")
    
    def block_time(self, start_time: datetime, stop_time: datetime) -> None:
        self.time_block.start_time = start_time
        self.time_block.stop_time = stop_time

        #TODO: should affect calendar and check for conflicting time