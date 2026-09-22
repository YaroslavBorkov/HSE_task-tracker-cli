import sys

from storage import add_task, list_tasks


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 src/main.py <command>")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Usage: python3 src/main.py add <task>")
            return

        title = " ".join(sys.argv[2:])
        task = add_task(title)
        print(f"Task added: {task['title']}")

    elif command == "list":
        tasks = list_tasks()

        if not tasks:
            print("No tasks found.")
            return

        for index, task in enumerate(tasks, start=1):
            status = "x" if task["completed"] else " "
            print(f"{index}. [{status}] {task['title']}")

    else:
        print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()