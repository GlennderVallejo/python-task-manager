import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("tasks.json")


def load_tasks():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            tasks = json.load(file)

            if not isinstance(tasks, list):
                print("Invalid data format. Starting with an empty task list.")
                return []

            for task in tasks:
                if (
                    not isinstance(task, dict)
                    or not isinstance(task.get("description"), str)
                    or not isinstance(task.get("completed"), bool)
                ):
                    print("Invalid task data. Starting with an empty task list.")
                    return []

            return tasks

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Error reading tasks.json. Starting with an empty task list.")
        return []

    except OSError as error:
        print(f"Error accessing task file: {error}")
        return []


def save_tasks(tasks):
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=4, ensure_ascii=False)

        return True

    except OSError as error:
        print(f"Error saving tasks: {error}")
        return False


def view_tasks(tasks):
    print("\n========== TASK LIST ==========")

    if not tasks:
        print("No tasks available.")
        return

    for index, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{index}. {task['description']} [{status}]")


def add_task(tasks):
    print("\n========== ADD TASK ==========")
    print("Enter 0 to return to the main menu.")

    while True:
        description = input("\nEnter task description: ").strip()

        if description == "0":
            print("Returning to main menu.")
            return

        if not description:
            print("Task description cannot be empty.")
            continue

        new_task = {
            "description": description,
            "completed": False
        }

        updated_tasks = tasks + [new_task]

        if save_tasks(updated_tasks):
            tasks.append(new_task)
            print("Task added successfully!")

        return


def select_task(tasks, action):
    if not tasks:
        print("\nNo tasks available.")
        return None

    while True:
        view_tasks(tasks)

        print("\n0. Return to main menu")

        option = input(f"\nSelect task number to {action}: ").strip()

        if option == "0":
            return None

        try:
            task_number = int(option)

            if 1 <= task_number <= len(tasks):
                return task_number - 1

            print("Invalid task number.")

        except ValueError:
            print("Please enter a valid number.")


def select_status():
    while True:
        print("\n========== CHANGE STATUS ==========")
        print("1. Pending")
        print("2. Completed")
        print("0. Return to main menu")

        option = input("\nSelect status: ").strip()

        if option == "0":
            return None

        if option == "1":
            return False

        if option == "2":
            return True

        print("Invalid option. Please try again.")


def edit_task(tasks):
    print("\n========== EDIT TASK ==========")

    task_index = select_task(tasks, "edit")

    if task_index is None:
        return

    original_task = tasks[task_index]

    # Work on a copy to prevent partial changes.
    updated_task = original_task.copy()

    while True:
        status = "Completed" if original_task["completed"] else "Pending"

        print("\n========== EDIT TASK ==========")
        print(f"Selected task: {original_task['description']}")
        print(f"Current status: {status}")

        print("\n1. Edit description")
        print("2. Change status")
        print("3. Edit both")
        print("0. Return to main menu")

        option = input("\nSelect an option: ").strip()

        if option == "0":
            print("Edit cancelled.")
            return

        if option not in ("1", "2", "3"):
            print("Invalid option.")
            continue

        if option in ("1", "3"):
            while True:
                print("\nEnter 0 to cancel editing.")

                new_description = input("Enter new description: ").strip()

                if new_description == "0":
                    print("Edit cancelled.")
                    return

                if not new_description:
                    print("Description cannot be empty.")
                    continue

                updated_task["description"] = new_description
                break

        if option in ("2", "3"):
            new_status = select_status()

            if new_status is None:
                print("Edit cancelled.")
                return

            updated_task["completed"] = new_status

        if updated_task == original_task:
            print("No changes were made.")
            return

        updated_tasks = tasks.copy()
        updated_tasks[task_index] = updated_task

        if save_tasks(updated_tasks):
            tasks[task_index] = updated_task
            print("Task updated successfully!")

        return


def delete_task(tasks):
    print("\n========== DELETE TASK ==========")

    task_index = select_task(tasks, "delete")

    if task_index is None:
        return

    selected_task = tasks[task_index]

    while True:
        print("\n========== CONFIRM DELETE ==========")
        print(f"Selected task: {selected_task['description']}")

        print("\n1. Yes, delete task")
        print("2. No, cancel")
        print("0. Return to main menu")

        option = input("\nSelect an option: ").strip()

        if option in ("0", "2"):
            print("Deletion cancelled.")
            return

        if option == "1":
            updated_tasks = tasks.copy()
            updated_tasks.pop(task_index)

            if save_tasks(updated_tasks):
                tasks.pop(task_index)
                print("Task deleted successfully!")

            return

        print("Invalid option. Please try again.")


def main():
    tasks = load_tasks()

    print("\n========== PYTHON TASK MANAGER ==========")

    while True:
        print("\n========== MAIN MENU ==========")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Exit")

        option = input("\nSelect an option: ").strip()

        if option == "1":
            add_task(tasks)

        elif option == "2":
            view_tasks(tasks)
            input("\nPress Enter to return to main menu...")

        elif option == "3":
            edit_task(tasks)

        elif option == "4":
            delete_task(tasks)

        elif option == "5":
            print("\nGoodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()