# Architecture

## Questions

* Bigger question: should we even support this much generic design or enfore things by creating predefined rules, stacks, etc

* How does a stack/task relate to a day
    * Becomes clear in case of tasks with time block, what about rest?

* Should we enforce every task to have a efforts/time estimate?
    * Because this will make time management and planning easier

* Rules engine for stacks?
    * So that status can automatically be changed

* Add a planned for date attribute for tasks?
    * Server should automatically move this somewhere once the day is done
    * Server should also automatically log unlogged time once the day ends or when user starts logging time

## Index

* [Concerns](concerns.md)
* [Task](task.md)
* [Stack](stack.md)
* [Task Server](task_server.md)
* [Time Log](time_log.md)

## Typical workflow

* Previous day
    * create tasks - done
    * add task to next day list
    * block time for next day (optional)

* Next day:
    * Clear view of which tasks are high priority
    * An order of work is defined

## Category

## Label/Tags

* For additional organizing

## Managers

### Calendar Manager

* Should validate if blocking a certain time is allowed

## Sync with other devices

* Support account system using a uuid like

## Global Settings/Config

* Should reside in an appropriate file format

* Can be made accessible through UI

