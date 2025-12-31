import sys
from .manager import TaskManager

def print_menu():
    print("\n--- Phase I: Todo App ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Complete / Incomplete")
    print("6. Exit")

def main():
    manager = TaskManager()

    while True:
        print_menu()
        choice = input("Select an option (1-6): ").strip()

        try:
            if choice == "1":
                title = input("Enter Task Title: ").strip()
                desc = input("Enter Description (optional): ").strip() or None
                task = manager.add_task(title, desc)
                print(f"Task added successfully! ID: {task['id']}")

            elif choice == "2":
                tasks = manager.get_tasks()
                if not tasks:
                    print("No tasks found.")
                else:
                    print("\n--- Your Tasks ---")
                    for t in tasks:
                        status = "[X]" if t["completed"] else "[ ]"
                        print(f"{t['id']}. {status} {t['title']} - {t['description'] or 'No description'}")

            elif choice == "3":
                task_id = int(input("Enter Task ID to update: "))
                new_title = input("Enter new title (leave blank to keep current): ").strip() or None
                new_desc = input("Enter new description (leave blank to keep current): ").strip() or None
                manager.update_task(task_id, new_title, new_desc)
                print("Task updated successfully!")

            elif choice == "4":
                task_id = int(input("Enter Task ID to delete: "))
                manager.delete_task(task_id)
                print("Task deleted successfully!")

            elif choice == "5":
                task_id = int(input("Enter Task ID to toggle status: "))
                task = manager.toggle_complete(task_id)
                status = "Completed" if task["completed"] else "Pending"
                print(f"Task marked as {status}!")

            elif choice == "6":
                print("Goodbye!")
                sys.exit(0)

            else:
                print("Invalid selection. Please choose 1-6.")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
