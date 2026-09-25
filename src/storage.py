import json


def load_tasks(filename="tasks.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_tasks(tasks, filename="tasks.json"):
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=2)
       
        
def add_task(title, filename="tasks.json"):
    tasks = load_tasks(filename)

    task = {
        "title": title,
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks, filename)

    return task

def list_tasks(filename="tasks.json"):
    return load_tasks(filename)

def complete_task(index, filename="tasks.json"):
    tasks = load_tasks(filename)

    if index < 1 or index > len(tasks):
        return False

    tasks[index - 1]["completed"] = True
    save_tasks(tasks, filename)

    return True

