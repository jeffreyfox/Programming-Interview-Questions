from typing import Optional
import json
from dataclasses import dataclass

class Task:
    def __init__(self, task_id: str, name: str, priority: int) -> None:
        self.task_id = task_id
        self.name = name
        self.priority = priority

class User:
    def __init__(self, user_id: str, quota: int) -> None:
        self.user_id = user_id
        self.quota = quota

@dataclass
class Assignment:
    user_id: str
    task_id: str
    start_timestamp: int
    end_timestamp: int
    completed: bool = False


class TaskManager:
    def __init__(self):
        self.tasks: dict[str, Task] = {}
        self.task_count = 0
        self.users: dict[str, User] = {}
        self.user_assignments: dict[str, list[Assignment]] = {}

    def add_task(self, timestamp: int, name: str, priority: int) -> str:
        self.task_count += 1
        task_id = f"task_id_{self.task_count}"
        self.tasks[task_id] = Task(task_id, name, priority)
        return task_id
    
    def update_task(self, timestamp: int, task_id: str, name: str, priority: int) -> bool:
        if task_id not in self.tasks:
            return False
        
        self.tasks[task_id].name = name
        self.tasks[task_id].priority = priority
        return True
    
    def get_task(self, timestamp: int, task_id: str) -> Optional[str]:
        task = self.tasks.get(task_id, None)
        if not task:
            return None

        d = {"name": task.name, "priority": task.priority}
        return json.dumps(d, separators=(",", ":"))

    def search_tasks(self, timestamp: int, name_filter: str, max_results: int) -> list[str]:
        if max_results <= 0:
            return []

        tasks = [task for task in self.tasks.values() if name_filter in task.name]
        tasks.sort(key=lambda t : (-t.priority, int(t.task_id[8:])))
        task_ids = [task.task_id for task in tasks]
        return task_ids[:max_results]

    def list_tasks_sorted(self, timestamp: int, limit: int) -> list[str]:
        if limit <= 0:
            return []
        
        tasks = [task for task in self.tasks.values()]
        tasks.sort(key=lambda t : (-t.priority, int(t.task_id[8:])))
        task_ids = [task.task_id for task in tasks]
        return task_ids[:limit]

    def add_user(self, timestamp: int, user_id: str, quota: int) -> bool:
        if user_id in self.users:
            return False
        
        user = User(user_id, quota)
        self.users[user_id] = user
        return True

    def assign_task(self, timestamp: int, task_id: str, user_id: str, finish_time: int) -> bool:
        if timestamp >= finish_time:
            return False

        if task_id not in self.tasks:
            return False

        user = self.users.get(user_id, None)
        if not user:
            return False

        assignments = self.user_assignments.setdefault(user_id, [])

        active_assignments = [
            a for a in assignments
            if a.start_timestamp <= timestamp < a.end_timestamp and not a.completed
        ]
        if len(active_assignments) == user.quota:
            return False

        self.user_assignments[user_id].append(
            Assignment(
                user_id=user_id,
                task_id=task_id,
                start_timestamp=timestamp,
                end_timestamp=finish_time,
            )
        )
        return True

    def get_user_tasks(self, timestamp: int, user_id: str) -> list[str]:
        if user_id not in self.users:
            return []
        assignments = self.user_assignments.get(user_id, None)
        if not assignments:
            return []
        active_assignments = [
            a for a in assignments
            if a.start_timestamp <= timestamp < a.end_timestamp
            and not a.completed
        ]
        active_assignments.sort(key = lambda a : (a.end_timestamp, a.start_timestamp))
        return [a.task_id for a in active_assignments]

    def complete_task(self, timestamp: int, task_id: str, user_id: str) -> bool:
        if user_id not in self.users or task_id not in self.tasks:
            return False
        assignments = self.user_assignments.setdefault(user_id, [])

        filtered_assignments = [
            a for a in assignments
            if a.start_timestamp <= timestamp < a.end_timestamp
            and a.task_id == task_id
            and not a.completed
        ]
        if not filtered_assignments:
            return False
        
        earliest = min(filtered_assignments, key=lambda a : a.start_timestamp)
        earliest.completed = True
        return True

    def get_overdue_assignments(self, timestamp: int, user_id: str) -> list[str]:
        if user_id not in self.users:
            return []
        assignments = self.user_assignments.setdefault(user_id, [])

        overdue_assignments = [
            a for a in assignments
            if a.end_timestamp <= timestamp and not a.completed
        ]
        overdue_assignments.sort(key=lambda a: (a.end_timestamp, a.start_timestamp))
        return [a.task_id for a in overdue_assignments]

def level_1():
    manager = TaskManager()
    task_id_1 = manager.add_task(1, "Task 1", 5)
    print(task_id_1)
    assert task_id_1 == "task_id_1"

    task_id_2 = manager.add_task(2, "Task 1", 5)
    print(task_id_2)
    assert task_id_2 == "task_id_2"

    status = manager.update_task(3, "task_id_1", "Updated Task 1", 4)
    print(status)
    assert status is True

    task = manager.get_task(4, "task_id_1")
    print(task)
    assert task == '{"name":"Updated Task 1","priority":4}'

    task2 = manager.get_task(5, "task_id_3")
    print(task2)
    assert task2 is None

    status = manager.update_task(6, "task_id_3", "Non-existing Task", 1)
    print(status)
    assert status is False


def level_2():
    manager = TaskManager()
    task_id = manager.add_task(1, "Alpha", 10)
    print(task_id)
    assert task_id == "task_id_1"

    task_id = manager.add_task(2, "Bravo", 15)
    print(task_id)
    assert task_id == "task_id_2"

    task_id = manager.add_task(3, "Bravo Alpha", 5)
    print(task_id)
    assert task_id == "task_id_3"

    task_ids = manager.list_tasks_sorted(4, 2)
    print(task_ids)
    assert task_ids == ["task_id_2", "task_id_1"]

    task_ids = manager.search_tasks(5, "Bra", 5)
    print(task_ids)
    assert task_ids == ["task_id_2", "task_id_3"]

    status = manager.update_task(6, "task_id_1", "Alpha Updated", 20)
    print(status)
    assert status

    task_ids = manager.search_tasks(7, "Al", 1)
    print(task_ids)
    assert task_ids == ["task_id_1"]


def level_3():
    manager = TaskManager()
    assert manager.add_user(1, "user1", 2)
    assert not manager.add_user(2, "user1", 3)
    
    task_id = manager.add_task(3, "Task A", 10)
    print(task_id)
    assert task_id == "task_id_1"

    task_id = manager.add_task(4, "Task B", 5)
    print(task_id)
    assert task_id == "task_id_2"

    assert manager.assign_task(5, "task_id_1", "user1", 15)
    task_ids = manager.get_user_tasks(8, "user1")
    print(task_ids)
    assert task_ids == ['task_id_1']

    assert manager.assign_task(7, "task_id_2", "user1", 20)
    task_ids = manager.get_user_tasks(8, "user1")
    print(task_ids)
    assert task_ids == ['task_id_1', 'task_id_2']

    assert not manager.assign_task(9, "task_id_1", "user1", 25)
    
    task_ids = manager.get_user_tasks(16, "user1")
    print(task_ids)
    assert task_ids == ['task_id_2']   

    task_ids = manager.get_user_tasks(21, "user1")
    print(task_ids)
    assert task_ids == []   


def level_4():
    manager = TaskManager()

    assert manager.add_user(1, "user1", 2)

    task_id = manager.add_task(3, "Task A", 10)
    assert task_id == "task_id_1"

    task_id = manager.add_task(4, "Task B", 5)
    print(task_id)
    assert task_id == "task_id_2"

    assert manager.assign_task(6, "task_id_1", "user1", 15)
    assert manager.complete_task(10, "task_id_1", "user1")

    task_ids = manager.get_user_tasks(11, "user1")
    assert task_ids == []

    task_ids = manager.get_overdue_assignments(18, "user1")
    assert task_ids == []

    assert manager.assign_task(13, "task_id_2", "user1", 15)
    task_ids = manager.get_overdue_assignments(30, "user1")
    print(task_ids)
    assert task_ids == ["task_id_2"]

    assert manager.assign_task(35, "task_id_1", "user1", 45)
    assert manager.assign_task(40, "task_id_1", "user1", 55)
    assert manager.complete_task(43, "task_id_1", "user1")
    task_ids = manager.get_user_tasks(44, "user1")
    assert task_ids == ["task_id_1"]

def main():
    level_1()
    print("\n=== level 1 SUCCESS ===\n")
    level_2()
    print("\n=== level 2 SUCCESS ===\n")
    level_3()
    print("\n=== level 3 SUCCESS ===\n")
    level_4()
    print("\n=== level 4 SUCCESS ===\n")


if __name__ == "__main__":
    main()
        
