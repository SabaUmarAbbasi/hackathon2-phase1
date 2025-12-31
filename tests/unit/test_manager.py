import pytest
from src.manager import TaskManager

def test_add_task():
    manager = TaskManager()
    task = manager.add_task("Test Task", "Test Description")
    assert task["id"] == 1
    assert task["title"] == "Test Task"
    assert task["description"] == "Test Description"
    assert task["completed"] is False

def test_add_task_empty_title():
    manager = TaskManager()
    with pytest.raises(ValueError, match="Task title cannot be empty."):
        manager.add_task("")

def test_get_tasks():
    manager = TaskManager()
    manager.add_task("Task 1")
    manager.add_task("Task 2")
    tasks = manager.get_tasks()
    assert len(tasks) == 2
    assert tasks[0]["id"] == 1
    assert tasks[1]["id"] == 2

def test_get_task_by_id():
    manager = TaskManager()
    manager.add_task("Task 1")
    task = manager.get_task_by_id(1)
    assert task["title"] == "Task 1"
    assert manager.get_task_by_id(99) is None

def test_update_task():
    manager = TaskManager()
    manager.add_task("Old Title")
    manager.update_task(1, title="New Title", description="New Desc")
    task = manager.get_task_by_id(1)
    assert task["title"] == "New Title"
    assert task["description"] == "New Desc"

def test_delete_task():
    manager = TaskManager()
    manager.add_task("To Delete")
    assert len(manager.get_tasks()) == 1
    manager.delete_task(1)
    assert len(manager.get_tasks()) == 0

def test_toggle_complete():
    manager = TaskManager()
    manager.add_task("Pending Task")
    task = manager.toggle_complete(1)
    assert task["completed"] is True
    manager.toggle_complete(1)
    assert task["completed"] is False
