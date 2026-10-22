# Python Task Manager

A command-line task management application developed with Python.

This project allows users to create, view, update, and delete tasks while storing their data locally in a JSON file.

## Features

- Create new tasks.
- View existing tasks and their completion status.
- Edit task descriptions.
- Change task status between Pending and Completed.
- Update task descriptions and statuses together.
- Delete tasks with confirmation.
- Cancel operations and return to the main menu.
- Save and load tasks using JSON.
- Handle invalid user inputs.

## Technologies

- Python 3
- JSON
- pathlib
- Git
- GitHub

No external Python libraries are required.

## Getting Started

### Requirements

- Python 3 installed on your computer.

### Installation

Clone the repository:

```bash
git clone https://github.com/GlennderVallejo/python-task-manager.git
```

Navigate to the project directory:

```bash
cd python-task-manager
```

Run the application:

```bash
python main.py
```

## Usage

The application displays the following menu:

```text
========== MAIN MENU ==========

1. Add Task
2. View Tasks
3. Edit Task
4. Delete Task
5. Exit
```

Select an option to manage your tasks.

Tasks are automatically saved in a local `tasks.json` file.

## Project Structure

```text
python-task-manager/
├── main.py
├── README.md
└── .gitignore
```

## Data Storage

Tasks are stored in JSON format.

Example:

```json
[
    {
        "description": "Study Python",
        "completed": false
    },
    {
        "description": "Practice SQL",
        "completed": true
    }
]
```

The `tasks.json` file is excluded from version control.

## Future Improvements

- Add task priorities and due dates.
- Implement task searching and filtering.
- Add automated tests.
- Explore database persistence using SQLite.

## License

This project is currently provided without a license.