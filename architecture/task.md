# Task

* Title
* Description
* Status (TODO/IN PROGRESS/BLOCKED/DONE)
* Category (optional)
* Priority (optional)
* Label/Tag (optional)
* Efforts?
* Start time (optional)
* Stop time (optional)
* Stale: true if blocked time has expired

* Project (optional)
    * Not just a category/tag/label!
    * Should be a complicated structure
    * Sort of like a epic? (can be used as reference)

    * Can have?
        * Goals
        * Timeline
        * Separate logging (should be able to view project specific metrics)
        * Completion percentage

## Types

* Recurring
    - date and time of recurrence

* Deadline
    - date and time of deadline

## Task blocking time validity logic

* Assume a task T1 with start_time s1 and stop_time s2 and a task T2 with start_time s3 and stop_time s4

```
s1 > s3, s2 > s4 - VALID

s1 < s3, s2 > s4 - INVALID
s1 > s3, s2 < s4 - INVALID

s1 < s3, s2 < s4 - VALID
```