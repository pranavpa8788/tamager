from dataclasses import dataclass, field
from uuid import UUID, uuid4
from datetime import datetime

from types.status import STATUS
from types.category import CATEGORY
from types.priority import PRIORITY
from types.tag import TAG

#TODO: move start_time and stop_time into a separate time block object and add field for time log record

@dataclass
class Task:
    id: UUID = field(default_factory=uuid4)
    title: str
    description: str
    status: STATUS
    priority: PRIORITY | None = None
    category: CATEGORY | None = None
    tag: TAG | None = None
    start_time: datetime | None = None
    stop_time: datetime | None = None

    def __eq__(self, other) -> bool:
        if other.__class__ is self.__class__:
            return self.id == other.id
        else:
            #TODO: Replace with custom exception
            raise Exception(f"Unexpected comparison between classes: {self.__class__} and {other.__class__}")
    
    def block_time(self, start_time: datetime, stop_time: datetime) -> None:
        self.start_time = start_time
        self.stop_time = stop_time

        #TODO: should affect calendar and check for conflicting time