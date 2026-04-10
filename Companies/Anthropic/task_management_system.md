Task Management System (Interview Problem)
Problem Summary
You need to build a task management system. There are 4 levels. Each level gets harder and adds new features:

Level 1: Build basic functions to add, update, and read tasks.
Level 2: Add features to search and sort tasks.
Level 3: Add users. Assign tasks to users with time limits and quotas.
Level 4: Allow users to finish tasks. Find tasks that were not finished on time.
You must solve the current level to move to the next one.

Priority and Quota are always positive numbers (or zero).
Timestamp and Finish Time are seconds since the system started.
Time always moves forward. New operations will always have a higher timestamp.
Level 1: Basics
Requirement
Create a system to add new tasks, update them, and view their details.

Operations
addTask(timestamp, name, priority) → String
Creates a new task.
Returns a unique ID like "task_id_1", "task_id_2", etc.
IDs are created in order (1, 2, 3...).
You can have multiple tasks with the same name. Thewill have different IDs.
Ignore the timestamp for the logic in Level 1.
updateTask(timestamp, taskId, name, priority) → boolean
Changes the name and priority of a specific task.
Returns true if successful.
Returns false if the taskId is not found.
getTask(timestamp, taskId) → Optional<String>
Returns a string with task details in JSON format.
Returns Optional.empty() if the task is not found.
Format Rules:
Do not put spaces between keys and values.
Keep spaces that are inside the name string.
Order: first name, then priority.
Level 1 Examples
| Queries | Explanations | | --- | --- | | addTask(1, "Task 1", 5) | Returns "task_id_1" | | addTask(2, "Task 1", 5) | Returns "task_id_2". Same name allowed. | | updateTask(3, "task_id_1", "Updated Task 1", 4) | Returns true. Updates the first task. | | getTask(4, "task_id_1") | Returns '{"name":"Updated Task 1","priority":4}'. No extra spaces. | | getTask(5, "task_id_3") | Returns Optional.empty(). Task does not exist. | | updateTask(6, "task_id_3", "Non-existingk", 1) | Returns false. Task does not exist. |

Level 1 Code
from typing import Optional

class Task:
    def __init__(self, task_id: str, name: str, priority: int):
        self.task_id = task_id
        self.name = name
        self.priority = priority

class TaskManagementSystem:
    def __init__(self):
        self.tasks: dict[str, Task] = {}
        self.task_counter = 0

    def add_task(self, timestamp: int, name: str, priority: int) -> str:
        self.task_counter += 1
        task_id = f"task_id_{self.task_counter}"
        self.tasks[task_id] = Task(task_id, name, priority)
        return task_id

    def update_task(self, timestamp: int, task_id: str, name: str, priority: int) -> bool:
        if task_id not in self.tasks:
            return False
        self.tasks[task_id].name = name
        self.tasks[task_id].priority = priority
        return True

    def get_task(self, timestamp: int, task_id: str) -> Optional[str]:
        if task_id not in self.tasks:
            return None
        task = self.tasks[task_id]
        return f'{{"name":"{task.name}","priority":{task.priority}}}'
Level 2: Search & Sort
Requirement
Add tools to find tasks and list them in a specific order.

New Operations
searchTasks(timestamp, nameFilter, maxResults) → List<String>
Finds tasks where the name contains the nameFilter.
Returns a list of task IDs (up to maxResults).
Sorting Rules:
First, by priority (High to Low).
If priorities are equal, sort by creation order (Low IDs first).
If maxResults is 0 or less, return an empty list.
listTasksSorted(timestamp, limit) → List<String>
Lists all task IDs up to the limit.
Uses the same sorting rules as search: priority (High -> Low), then creation order.
Level 2 Examples
| Queries | Explanations | | --- | --- | | addTask(1, "Alpha", 10) | Returns "task_id_1" | | addTask(2, "Bravo", 15) | Returns "task_id_2" | | addTask(3, "Bravo Alpha", 5) | Returns "task_id_3" | | listTasksSorted(4, 2) | Returns ["task_id_2", "task_id_1"]. Sorts by priority. | | searchTasks(5, "Bra" | Returns ["task_id_2", "task_id_3"]. Matches "Bravo". | | updateTask(6, "task_id_1", "Alpha Updated", 20) | Returns true. Priority is now 20. | | searchTasks(7, "Al", 1) | Returns ["task_id_1"]. "Alpha Updated" is now highest priority. |

Level 2 Code
Add these methods to the previous code:

class TaskManagementSystem:
    def __init__(self):
        self.tasks: dict[str, Task] = {}
        self.task_counter = 0
        self.creation_order: dict[str, int] = {}  # Maps task_id to creation number

    def add_task(self, timestamp: int, name: str, priority: int) -> str:
        self.task_counter += 1
        task_id = f"task_id_{self.task_counter}"
        self.tasks[task_id] = Task(task_id, name, priority)
        self.creation_order[task_id] = self.task_counter
        return task_id

    # ... Include Level 1 methods here ...

    def search_tasks(self, timestamp: int, name_filter: str, max_results: int) -> list[str]:
        if max_results <= 0:
            return []

        matching = [
            task_id for task_id, task in self.tasks.items()
            if name_filter in task.name
        ]

        # Sort: Priority Descending (-), then Creation Order Ascending (+)
        matching.sort(key=lambda tid: (-self.tasks[tid].priority, self.creation_order[tid]))

        return matching[:max_results]

    def list_tasks_sorted(self, timestamp: int, limit: int) -> list[str]:
        if limit <= 0:
            return []

        task_ids = list(self.tasks.keys())
        task_ids.sort(key=lambda tid: (-self.tasks[tid].priority, self.creation_order[tid]))

        return task_ids[:limit]
Level 3: Users & Assignments
Requirement
Add users to the system. Users have a limit on how many tasks they can do at once (quota). Tasks are assigned for a specific time period.

New Operations
addUser(timestamp, userId, quota) → boolean
Adds a user with a specific task limit (quota).
Returns true if successful.
Returns false if the user ID already exists.
assignTask(timestamp, taskId, userId, finishTime) → boolean
Assig task to a user from timestamp until finishTime.
Quota Rule: Each active task uses 1 quota slot.
Returns false if:
Task or User doesn't exist.
User has reached their quota limit at this moment.
When timestamp reaches finishTime, the task expires and the quota slot is freed automatically.
You can assign the same task multiple times. Each assignment is separate.
getUserTasks(timestamp, userId) → List<String>
Gets a list of IDs for tasks currently assigned to the user.
A task is "active" if: start_time <= timestamp < finish_time.
Sorting: Sort by finish_time (soonest first). Tie-break with assignment time.
Level 3 Examples
| Queries | Explanations | | --- | --- | | addUser(1, "user1", 2) | Returns true. Quota is 2. | | aUser(2, "user1", 3) | Returns false. User exists. | | addTask(3, "Task A", 10) | Returns "task_id_1" | | addTask(4, "Task B", 5) | Returns "task_id_2" | | assignTask(5, "task_id_1", "user1", 15) | Returns true. Assigned until time 15. | | getUserTasks(6, "user1") | Returns ["task_id_1"] | | assignTask(7, "task_id_2", "user1", 20) | Returns true. Assigned until time 20. | | getUserTasks(8, "user1") | Returns ["task_id_1", "task_id_2"]. | | assignTask(9, "task_id_1", "user1", 25) | Returns false. Quota full (2 active tasks). | | getUserTasks(16, "user1") | Returns ["task_id_2"]. Task 1 expired at 15. | | getUserTasks(21, "user1") | Returns []. Both tasks expired. |

Level 3 Code
from dataclasses import dataclass

@dataclass
class Assignment:
    task_id: str
    user_id: str
    start_time: int
    finish_time: int
    completed: bool = False

class User:
    def __init__(self, user_id: str, quota: int):
        self.user_id = user_id
        self.quota = quota
        self.assignments: list[Assignment] = []

class TaskManagementSystem:
    def __init__(self):
        self.tasks: dict[str, Task] = {}
        self.task_counter = 0
        self.creation_order: dict[str, int] = {}
        self.users: dict[str, User] = {}

    # ... Include Level 1 & 2 methods here ...

    def add_user(self, timestamp: int, user_id: str, quota: int) -> bool:
        if user_id in self.users:
            return False
        self.users[user_id] = User(user_id, quota)
        return True

    def _get_active_assignment_count(self, user: User, timestamp: int) -> int:
        """Count how many assignments are active right now."""
        return sum(
            1 for a in user.assignments
            if a.start_time <= timestamp < a.finish_time and not a.completed
        )

    def assign_task(self, timestamp: int, task_id: str, user_id: str, finish_time: int) -> bool:
        if task_id not in self.tasks or user_id not in self.users:
            return False

        user = self.users[user_id]

        # Check if user has space in their quota
        active_count = self._get_active_assignment_count(user, timestamp)
        if active_count >= user.quota:
            return False

        # Add new assignment
        assignment = Assignment(task_id, user_id, timestamp, finish_time)
        user.assignments.append(assignment)
        return True

    def get_user_tasks(self, timestamp: int, user_id: str) -> list[str]:
        if user_id not in self.users:
            return []

        user = self.users[user_id]
        active = [
            a for a in user.assignments
            if a.start_time <= timestamp < a.finish_time and not a.completed
        ]

        # Sort by finish_time, then start_time
        active.sort(key=lambda a: (a.finish_time, a.start_time))

        return [a.task_id for a in active]
Level 4: Completion & History
Requirement
Allow users to finish tasks. You also need to report which tasks were ignored (expired without being finished).

New Operations
completeTask(timestamp, taskId, userId) → boolean
Marks a task as done.
The task must be active right now.
Frees up one quota slot immediately.
Constrnt: If the user has the same task assigned multiple times, complete the one that started earliest.
Returns false if the task is not assigned to this user at this time.
getOverdueAssignments(timestamp, userId) → List<String>
Lists tasks that expired in the past without being completed.
"Overdue" means finish_time <= timestamp AND the task was never finished.
Sorting: Sort by finish_time (oldest expiry first).
If a task expired multiple times, list it multiple times.
Level 4 Examples
| Queries Explanations | | --- | --- | | assignTask(6, "task_id_1", "user1", 15) | Assignment active [6, 15). | | completeTask(10, "task_id_1", "user1") | Returns true. Task done. Quota freed. | | getUserTasks(11, "user1") | Returns []. No active tasks. | | getOverdueAssignments(18, "user1") | Returns []. Task 1 was finished, so it is not overdue. | | assignTask(13, "task_id_3", "user1", 25) | Assignment active [13, 25). | | getOverdueAssignments(30, "user1") | Returns ["task_id_3"]. It expired at 25 without completion. | | assignTask(35, "task_id_1", "user1", 45) | Re-assign Task 1. | | assignTask(40, "task_id_1", "user1", 55) | Re-assign Task 1 again. Overlapping. | | completeTask(43, "task_id_1", "user1") | Completes the first one (started at 35). | | getUserTasks(44, "user1") | Returns ["task_id_1"]. The second one is still active. |

Level 4 Code
Update the completion and overdue logic:

class TaskManagementSystem:
    # ... Level 1-3 methods ...

    def complete_task(self, timestamp: int, task_id: str, user_id: str) -> bool:
        if task_id not in self.tasks or user_id not in self.users:
            return False

        user = self.users[user_id]

        # Find active assignments for this task
        active_assignments = [
            a for a in user.assignments
            if a.task_id == task_id
            and a.start_time <= timestamp < a.finish_time
            and not a.completed
        ]

        if not active_assignments:
            return False

        # Complete the earliest one
        active_assignments.sort(key=lambda a: a.start_time)
        active_assignments[0].completed = True
        return True

    def get_overdue_assignments(self, timestamp: int, user_id: str) -> list[str]:
        if user_id not in self.users:
            return []

        user = self.users[user_id]

        # Find assignments that expired and were not finished
        overdue = [
            a for a in user.assignments
            if a.finish_time <= timestamp and not a.completed
        ]

        # Sort by finish_time, then start_time
        overdue.sort(key=lambda a: (a.finish_time, a.start_time))

        return [a.task_id for a in overdue]
Full Solution Code
Here is the complete code with all features combined:

from typing import Optional
from dataclasses import dataclass

@dataclass
class Assignment:
    task_id: str
    user_id: str
    start_time: int
    finish_time: int
    completed: bool = False

class Task:
    def __init__(self, task_id: str, name: str, priority: int):
        self.task_id = task_id
        self.name = name
        self.priority = priority

class User:
    def __init__(self, user_id: str, quota: int):
        self.user_id = user_id
        self.quota = quota
        self.assignments: list[Assignment] = []

class TaskManagementSystem:
    def __init__(self):
        self.tasks: dict[str, Task] = {}
        self.task_counter = 0
        self.creation_order: dict[str, int] = {}
        self.users: dict[str, User] = {}

    # Level 1
    def add_task(self, timestamp: int, name: str, priority: int) -> str:
        self.task_counter += 1
        task_id = f"task_id_{self.task_counter}"
        self.tasks[task_id] = Task(task_id, name, priority)
        self.creation_order[task_id] = self.task_counter
        return task_id

    def update_task(self, timestamp: int, task_id: str, name: str, priority: int) -> bool:
        if task_id not in self.tasks:
            return False
        self.tasks[task_id].name = name
        self.tasks[task_id].priority = priority
        return True

    def get_task(self, timestamp: int, task_id: str) -> Optional[str]:
        if task_id not in self.tasks:
            return None
        task = self.tasks[task_id]
        return f'{{"name":"{task.name}","priority":{task.priority}}}'

    # Level 2
    def search_tasks(self, timestamp: int, name_filter: str, max_results: int) -> list[str]:
        if max_results <= 0:
            return []

        matching = [
            task_id for task_id, task in self.tasks.items()
            if name_filter in task.name
        ]

        matching.sort(key=lambda tid: (-self.tasks[tid].priority, self.creation_order[tid]))
        return matching[:max_results]

    def list_tasks_sorted(self, timestamp: int, limit: int) -> list[str]:
        if limit <= 0:
            return []

        task_ids = list(self.tasks.keys())
        task_ids.sort(key=lambda tid: (-self.tasks[tid].priority, self.creation_order[tid]))
        return task_ids[:limit]

    # Level 3
    def add_user(self, timestamp: int, user_id: str, quota: int) -> bool:
        if user_id in self.users:
            return False
        self.users[user_id] = User(user_id, quota)
        return True

    def _get_active_assignment_count(self, user: User, timestamp: int) -> int:
        return sum(
            1 for a in user.assignments
            if a.start_time <= timestamp < a.finish_time and not a.completed
        )

    def assign_task(self, timestamp: int, task_id: str, user_id: str, finish_time: int) -> bool:
        if task_id not in self.tasks or user_id not in self.users:
            return False

        user = self.users[user_id]
        active_count = self._get_active_assignment_count(user, timestamp)
        if active_count >= user.quota:
            return False

        assignment = Assignment(task_id, user_id, timestamp, finish_time)
        user.assignments.append(assignment)
        return True

    def get_user_tasks(self, timestamp: int, user_id: str) -> list[str]:
        if user_id not in self.users:
            return []

        user = self.users[user_id]
        active = [
            a for a in user.assignments
            if a.start_time <= timestamp < a.finish_time and not a.completed
        ]

        active.sort(key=lambda a: (a.finish_time, a.start_time))
        return [a.task_id for a in active]

    # Level 4
    def complete_task(self, timestamp: int, task_id: str, user_id: str) -> bool:
        if task_id not in self.tasks or user_id not in self.users:
            return False

        user = self.users[user_id]
        active_assignments = [
            a for a in user.assignments
            if a.task_id == task_id
            and a.start_time <= timestamp < a.finish_time
            and not a.completed
        ]

        if not active_assignments:
            return False

        active_assignments.sort(key=lambda a: a.start_time)
        active_assignments[0].completed = True
        return True

    def get_overdue_assignments(self, timestamp: int, user_id: str) -> list[str]:
        if user_id not in self.users:
            return []

        user = self.users[user_id]
        overdue = [
            a for a in user.assignments
            if a.finish_time <= timestamp and not a.completed
        ]

        overdue.sort(key=lambda a: (a.finish_time, a.start_time))
        return [a.task_id for a in overdue]
Big O Analysis
Here is how efficient the solution is:

| Operation | Time Complexity | Space Complexity | | --- | --- | --- | | addTask | O(1) | O(1) | | updateTask | O(1) | O(1) | | getTask | O(1) | O(1) | | searchTasks | O(T log T) | O(T) | | listTasksSorted | O(T log T) | O(T) | | addUser | O(1) | O(1) | | assignTask | O(A) | O(1) | | getUserTasks | O(A log A) | O(A) | | completeTask | O(A log A) | O(A) | | getOverdueAssignments | O(A log A) | O(A) |

Definitions:

T = Total number of tasks.
A = Number of assignments for a specific user.
