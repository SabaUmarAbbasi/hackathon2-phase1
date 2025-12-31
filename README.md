# the-todo-app

A simple Python-based Todo application built with Spec-Driven Development.

## Phase I Features
- Add tasks with title and optional description.
- View task list with status indicators.
- Update task details.
- Delete tasks by ID.
- Toggle completion status.
- **In-memory storage only** (data clears on exit).

## Prerequisites
- Python 3.13+
- [uv](https://github.com/astral-sh/uv)

## Installation
```bash
git clone <repo-url>
cd the-todo-app
uv sync
```

## Running the App
```bash
uv run src/app.py
```

## Running Tests
```bash
uv run pytest
```
