from dataclasses import dataclass
from typing import List
from datetime import datetime

from tamager.types.task import Task
from tamager.types.stack import Stack

@dataclass
class CalendarManager:

    #NOTE: can be made into an efficient algorithm if we store a datetime based sorted array of tasks in each stack,
    # but at the moment this is not necessary as the number of tasks won't be that much
    def validate_time_block(self, task: Task, stack: Stack) -> bool:

        if task.time_block is None:
            raise Exception(f"Given task: {task} does not have a time_block")
        
        start_time = task.time_block.start_time
        stop_time = task.time_block.stop_time

        for other in stack.tasks:
            if other == task or other.time_block is None:
                continue

            other_start_time = other.time_block.start_time
            other_stop_time = other.time_block.stop_time

            if start_time < other_stop_time and stop_time > other_start_time:
                return False
        
        return True