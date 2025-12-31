from typing import List, Optional
from .models import Task

class TaskManager:
    def __init__(self):
        self._tasks: List[Task] = []
        self._next_id: int = 1

    def add_task(self, title: str, description: Optional[str] = None) -> Task:
        """Adds a new task to the list."""
        if not title.strip():
            raise ValueError("Task title cannot be empty.")

        task: Task = {
            "id": self._next_id,
            "title": title.strip(),
            "description": description,
            "completed": False,
        }
        self._tasks.append(task)
        self._next_id += 1
        return task

    def get_tasks(self) -> List[Task]:
        """Returns all tasks."""
        return self._tasks

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """Finds a task by its ID."""
        for task in self._tasks:
            if task["id"] == task_id:
                return task
        return None

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> Task:
        """Updates an existing task."""
        task = self.get_task_by_id(task_id)
        if not task:
            raise ValueError(f"Task with ID {task_id} not found.")

        if title is not None:
            if not title.strip():
                raise ValueError("Task title cannot be empty.")
            task["title"] = title.strip()

        if description is not None:
            task["description"] = description

        return task

    def delete_task(self, task_id: int) -> bool:
        """Deletes a task by ID."""
        task = self.get_task_by_id(task_id)
        if task:
            self._tasks.remove(task)
            return True
        raise ValueError(f"Task with ID {task_id} not found.")

    def toggle_complete(self, task_id: int) -> Task:
        """Toggles the completion status of a task."""
        task = self.get_task_by_id(task_id)
        if not task:
            raise ValueError(f"Task with ID {task_id} not found.")

        task["completed"] = not task["completed"]
        return task
