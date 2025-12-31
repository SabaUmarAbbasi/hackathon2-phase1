# The Todo App — Phase I: In-Memory Python Console App

## Project Overview

**the-todo-app** is a **command-line todo application** that allows users to manage tasks **entirely in memory**.  
This project is built following a **spec-driven development approach** using **Claude Code** and **Spec-Kit Plus**.

Phase I focuses on **basic level functionality** for a single user:
- Add tasks
- View tasks
- Update tasks
- Delete tasks
- Mark tasks complete/incomplete

No databases, files, or web frameworks are used — everything exists **temporarily during runtime**.

---

## Table of Contents

1. [Features](#features)  
2. [Technology Stack](#technology-stack)  
3. [Setup Instructions](#setup-instructions)  
4. [Usage](#usage)  
5. [Project Structure](#project-structure)  
6. [CLI Interaction](#cli-interaction)  
7. [Error Handling](#error-handling)  
8. [Development Workflow](#development-workflow)  
9. [License](#license)  

---

## Features

Phase I implements the following **mandatory features**:

1. **Add Task**  
   - Create tasks with a **title** (required) and **description** (optional)
2. **View Task List**  
   - List all tasks with **status indicators** (complete/incomplete)
3. **Update Task**  
   - Modify title or description of an existing task
4. **Delete Task**  
   - Remove a task by its unique ID
5. **Mark Task Complete/Incomplete**  
   - Toggle a task’s completion status

---

## Technology Stack

- **Python 3.13+**  
- **Claude Code** (for code generation)  
- **Spec-Kit Plus** (for spec-driven development)  
- Standard Python **CLI tools** only (no external libraries required)

---

## Setup Instructions

1. **Clone the repository**:

```bash
git clone https://github.com/yourusername/the-todo-app.git
cd the-todo-app


Navigate to the source folder:

cd src


Run the application:

python main.py


Ensure you have Python 3.13+ installed.

Usage

The app runs in a menu-driven CLI interface.

Users can perform actions by entering numeric menu choices.

Tasks exist only in memory and will be lost when the program exits.

Project Structure
the-todo-app/
│
├── README.md
├── CLAUDE.md
├── /specs_history/
│   ├── sp.constitution
│   ├── sp.specify
│   ├── sp.plan
│   └── sp.task
└── /src/
    ├── main.py          # Entry point for the CLI app
    ├── task_manager.py  # Task data model and in-memory storage
    └── cli.py           # CLI menu and user input handling

CLI Interaction

Main Menu:

Add Task

View Tasks

Update Task

Delete Task

Mark Task Complete/Incomplete

Exit

Task Input:

Prompted for task ID, title, description as needed

Menu continues until user selects Exit

Error Handling

The application handles:

Invalid menu selection

Empty task list

Invalid task ID

Empty task title input

All errors are gracefully handled with user-friendly messages.

Development Workflow

The project follows the Agentic Dev Stack:

Global Constitution (sp.constitution)
Defines rules, agent behavior, phase governance, and technology constraints.

Phase Specification (sp.specify)
Details Phase I scope, required features, data model, and CLI flow.

Technical Plan (sp.plan)
Defines implementation strategy, data structures, and control flow.

Tasks (sp.task)
Breaks plan into small, testable, atomic implementation tasks.

Implementation (sp.implement)
Actual coding of tasks following all specs and plans.

No manual coding outside Claude Code is allowed.

License

This project is licensed under the MIT License.
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
