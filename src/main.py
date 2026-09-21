import sys

from storage import add_task


def main():
    if len(sys.argv) < 3 or sys.argv[1] != "add":
        print("Usage: python3 src/main.py add <task>")
        return

    title = " ".join(sys.argv[2:])
    task = add_task(title)

    print(f"Task added: {task['title']}")


if __name__ == "__main__":
    main()