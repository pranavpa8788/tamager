from typing import List
from dataclasses import dataclass

from task import Task

@dataclass
class Stack:
    title: str
    tasks: List[Task]

    def task_exists(self, task: Task) -> bool:
        for _task in self.tasks:
            if (task == _task):
                return True
        return False
    
    def add_task(self, task: Task) -> None:
        self.tasks.append(task)
    
    def remove_task(self, task: Task) -> None:
        self.tasks.remove(task)