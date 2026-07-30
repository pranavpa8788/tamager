from datetime import datetime
from dataclasses import dataclass

@dataclass
class TimeBlock:
    start_time: datetime
    stop_time: datetime