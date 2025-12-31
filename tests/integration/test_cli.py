import pytest
from src.app import main
from io import StringIO
import sys

def test_cli_add_and_view(monkeypatch):
    # Inputs: 1 (Add), Test Title, Test Desc, 2 (View), 6 (Exit)
    inputs = iter(["1", "Test Title", "Test Desc", "2", "6"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    output = StringIO()
    monkeypatch.setattr('sys.stdout', output)

    with pytest.raises(SystemExit):
        main()

    out = output.getvalue()
    assert "Task added successfully!" in out
    assert "1. [ ] Test Title - Test Desc" in out

def test_cli_toggle_status(monkeypatch):
    # Inputs: 1 (Add), Title, empty desc, 5 (Toggle), 1 (ID), 2 (View), 6 (Exit)
    inputs = iter(["1", "Toggle Me", "", "5", "1", "2", "6"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    output = StringIO()
    monkeypatch.setattr('sys.stdout', output)

    with pytest.raises(SystemExit):
        main()

    out = output.getvalue()
    assert "Task marked as Completed!" in out
    assert "1. [X] Toggle Me" in out

def test_cli_delete(monkeypatch):
    # Inputs: 1 (Add), Title, desc, 4 (Delete), 1 (ID), 2 (View), 6 (Exit)
    inputs = iter(["1", "Delete Me", "Bye", "4", "1", "2", "6"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    output = StringIO()
    monkeypatch.setattr('sys.stdout', output)

    with pytest.raises(SystemExit):
        main()

    out = output.getvalue()
    assert "Task deleted successfully!" in out
    assert "No tasks found." in out
