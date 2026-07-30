from datetime import datetime

from src.types.task import Task
from src.types.stack import Stack
from src.types.status import STATUS
from src.types.time.time_block import TimeBlock
from src.managers.calendar_manager import CalendarManager

def test_non_blocking_time_blocks_1():
    """
    time_block_1 starts and ends before time_block_2 even starts
    """
    start_time_1 = datetime(2001, 1, 1, 9, 0)
    stop_time_1 = datetime(2001, 1, 1, 10, 0)

    start_time_2 = datetime(2001, 1, 1, 12, 0)
    stop_time_2 = datetime(2001, 1, 1, 13, 0)

    time_block_1 = TimeBlock(start_time_1, stop_time_1)
    time_block_2 = TimeBlock(start_time_2, stop_time_2)

    task_1 = Task(title="Task 1", description="", status=STATUS.IN_PROGRESS, time_block=time_block_1)
    task_2 = Task(title="Task 2", description="", status=STATUS.IN_PROGRESS, time_block=time_block_2)

    stack = Stack("Stack", [task_1, task_2])
    calendar_manager = CalendarManager()

    assert calendar_manager.validate_time_block(task_2, stack=stack) == True

    assert calendar_manager.validate_time_block(task_1, stack=stack) == True

def test_blocking_time_blocks_1():
    """
    time_block_2 is in between time_block_1
    """
    start_time_1 = datetime(2001, 1, 1, 9, 0)
    stop_time_1 = datetime(2001, 1, 1, 13, 0)

    start_time_2 = datetime(2001, 1, 1, 10, 0)
    stop_time_2 = datetime(2001, 1, 1, 11, 0)

    time_block_1 = TimeBlock(start_time_1, stop_time_1)
    time_block_2 = TimeBlock(start_time_2, stop_time_2)

    task_1 = Task(title="Task 1", description="", status=STATUS.IN_PROGRESS, time_block=time_block_1)
    task_2 = Task(title="Task 2", description="", status=STATUS.IN_PROGRESS, time_block=time_block_2)

    stack = Stack("Stack", [task_1, task_2])
    calendar_manager = CalendarManager()

    assert calendar_manager.validate_time_block(task_2, stack=stack) == False

    assert calendar_manager.validate_time_block(task_1, stack=stack) == False

def test_blocking_time_blocks_2():
    """
    time_block_1 starts before time_block_2 ends
    """
    start_time_1 = datetime(2001, 1, 1, 9, 0)
    stop_time_1 = datetime(2001, 1, 1, 13, 0)

    start_time_2 = datetime(2001, 1, 1, 10, 0)
    stop_time_2 = datetime(2001, 1, 1, 11, 0)

    time_block_1 = TimeBlock(start_time_1, stop_time_1)
    time_block_2 = TimeBlock(start_time_2, stop_time_2)

    task_1 = Task(title="Task 1", description="", status=STATUS.IN_PROGRESS, time_block=time_block_1)
    task_2 = Task(title="Task 2", description="", status=STATUS.IN_PROGRESS, time_block=time_block_2)

    stack = Stack("Stack", [task_1, task_2])
    calendar_manager = CalendarManager()

    assert calendar_manager.validate_time_block(task_2, stack=stack) == False

    assert calendar_manager.validate_time_block(task_1, stack=stack) == False

def test_blocking_time_blocks_3():
    """
    time_block_1 starts before time_block_2 ends
    """
    start_time_1 = datetime(2001, 1, 1, 10, 0)
    stop_time_1 = datetime(2001, 1, 1, 12, 0)

    start_time_2 = datetime(2001, 1, 1, 11, 0)
    stop_time_2 = datetime(2001, 1, 1, 13, 0)

    time_block_1 = TimeBlock(start_time_1, stop_time_1)
    time_block_2 = TimeBlock(start_time_2, stop_time_2)

    task_1 = Task(title="Task 1", description="", status=STATUS.IN_PROGRESS, time_block=time_block_1)
    task_2 = Task(title="Task 2", description="", status=STATUS.IN_PROGRESS, time_block=time_block_2)

    stack = Stack("Stack", [task_1, task_2])
    calendar_manager = CalendarManager()

    assert calendar_manager.validate_time_block(task_2, stack=stack) == False

    assert calendar_manager.validate_time_block(task_1, stack=stack) == False