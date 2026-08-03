# Database Design

## Task

* id (uuid)
* title: str
* description: str
* status: str
* category (optional): str
* priority (optional): int
* tag (optional): str
* stale: boolean

* Time log records
    * relation to time log table

* time_block records
    * start_time (optional): str? (or timestamp)
    * stop_time (optional): str? (or timestamp)

## Stack

* title: str
* tasks: tasks[]
* sort_by_priority: boolean

## Time log

* start_time: str? (or timestamp)
* stop_time: str? (or timestamp)
* description: str