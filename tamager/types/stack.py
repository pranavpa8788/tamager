from typing import List
from bisect import insort
from dataclasses import dataclass

from tamager.types.task import Task

@dataclass
class Stack:
    title: str
    tasks: List[Task]
    sort_by_priority: bool = False
    can_create_tasks: bool = False

    def task_exists(self, task: Task) -> bool:
        for _task in self.tasks:
            if (task == _task):
                return True
        return False
    
    def add_task(self, task: Task) -> None:
        if (self.sort_by_priority == True):
            insort(self.tasks, task, key=lambda t: t.priority)
        else:
            self.tasks.append(task)
    
    def remove_task(self, task: Task) -> None:
        self.tasks.remove(task)

    def order_based_on_priority(self, persist_sorting: bool) -> None:
        if persist_sorting == True:
            self.sort_by_priority = True

        self.tasks.sort(key=lambda task: task.priority)