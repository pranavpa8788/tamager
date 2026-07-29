from dataclasses import dataclass
from typing import List
from datetime import datetime

from ..stack import Stack

@dataclass
class CalendarManager:
    stacks: List[Stack]

    #NOTE: can be made into an efficient algorithm if we store a datetime based sorted array of tasks in each stack,
    # but at the moment this is not necessary as the number of tasks won't be that much
    def validate_time_block(self, start_time: datetime, stop_time: datetime, stack_filter: List[Stack]) -> bool:
        stacks = self.stacks

        if stack_filter:
            stacks = stack_filter

        for stack in stacks:
            for task in stack.tasks:
                if (task.start_time is not None) and (task.stop_time is not None):
                    if (start_time > task.start_time and stop_time > task.stop_time) or (start_time < task.start_time and stop_time < task.stop_time):
                        return True
                    else:
                        return False