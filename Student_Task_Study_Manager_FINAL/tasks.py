from datetime import datetime

import storage
import validation
def get_tasks():
    return storage.tasks


def add_task(title, subject, due_date, priority):
    for value, field_name in [(title, "Task title"), (subject, "Task subject"), (due_date, "Due date")]:
        valid, message = validation.validate_not_empty(value, field_name)
        if not valid:
            return False, message

    valid, message = validation.validate_date(due_date)
    if not valid:
        return False, message

    valid, message = validation.validate_not_empty(priority, "Priority")
    if not valid:
        return False, message

    task = {
        "title": title,
        "subject": subject,
        "due date": due_date,
        "priority": priority,
        "status": "pending",
    }

    storage.tasks.append(task)
    storage.save_data()

    return True, "Task added successfully!"
def delete_task(title):
    valid, message = validation.validate_not_empty(title, "Task title")
    if not valid:
        return False, message

    for task in storage.tasks:
        if task["title"] == title:
            storage.tasks.remove(task)
            storage.save_data()
            return True, "Task deleted successfully!"

    return False, "Task not found."
def complete_task(title):
    valid, message = validation.validate_not_empty(title, "Task title")
    if not valid:
        return False, message

    for task in storage.tasks:
        if task["title"] == title:
            task["status"] = "completed"
            storage.save_data()
            return True, "Task completed successfully!"

    return False, "Task not found."
def search_tasks(keyword):
    keyword = keyword.strip().lower()

    if keyword == "":
        return []

    return [
        task for task in storage.tasks
        if keyword in task["title"].lower() or keyword in task["subject"].lower()
    ]
def get_pending_tasks():
    return [task for task in storage.tasks if task["status"] == "pending"]


def get_completed_tasks():
    return [task for task in storage.tasks if task["status"] == "completed"]


def get_overdue_tasks():
    overdue_tasks = []
    today = datetime.now()

    for task in storage.tasks:
        if task["status"] == "pending":
            try:
                due_date = datetime.strptime(task["due date"], "%d-%m-%Y")
            except ValueError:
                continue

            if due_date < today:
                overdue_tasks.append(task)

    return overdue_tasks
