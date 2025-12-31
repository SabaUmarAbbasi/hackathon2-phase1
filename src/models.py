from typing import TypedDict, Optional

class Task(TypedDict):
    id: int
    title: str
    description: Optional[str]
    completed: bool
