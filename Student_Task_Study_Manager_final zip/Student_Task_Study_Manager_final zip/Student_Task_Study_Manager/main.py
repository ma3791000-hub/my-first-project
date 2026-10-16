import json
import os
from datetime import datetime

subjects = []
tasks = []
study_sessions = []
student_profile = {}


def load_data():
    file_path = os.path.join(os.path.dirname(__file__), "data", "study_manager.json")

    with open(file_path, "r") as file:
        data = json.load(file)

    subjects.extend(data["subjects"])
    tasks.extend(data["tasks"])
    study_sessions.extend(data.get("study_sessions", []))
    student_profile.update(data.get("student_profile", {}))


def save_data():
    file_path = os.path.join(os.path.dirname(__file__), "data", "study_manager.json")

    with open(file_path, "w") as file:
     json.dump({
    "subjects": subjects,
    "tasks": tasks,
    "study_sessions": study_sessions,
    "student_profile": student_profile
}, file, indent=4)

def save_student_profile(name, roll_no, semester, program):

    if name.strip() == "":
        return False, "Name cannot be empty."

    if roll_no.strip() == "":
        return False, "Roll number cannot be empty."

    if semester.strip() == "":
        return False, "Semester cannot be empty."

    if program.strip() == "":
        return False, "Program cannot be empty."

    student_profile["name"] = name
    student_profile["roll_no"] = roll_no
    student_profile["semester"] = semester
    student_profile["program"] = program

    save_data()

    return True, "Student profile saved successfully!"
def add_subject():
    subject = input("Enter your subject: ")
    if subject.strip() == "":
        print("Subject cannot be empty")
        return
    if subject in subjects:
        print("Subject already exists.")
        return
    subjects.append(subject)
    save_data()
    print("Subject added successfully")


def delete_subject(subject):

    if subject.strip() == "":
        return False, "Subject cannot be empty."

    if subject in subjects:
        subjects.remove(subject)
        save_data()
        return True, "Subject deleted successfully!"
    else:
        return False, "Subject not found."


def delete_task(title):

    if title.strip() == "":
        return False, "Task title cannot be empty."

    for task in tasks:
        if task["title"] == title:
            tasks.remove(task)
            save_data()
            return True, "Task deleted successfully!"

    return False, "Task not found."


def add_task(title, subject, due_date, priority):

    if title.strip() == "":
        return False, "Task title cannot be empty."

    if subject.strip() == "":
        return False, "Task subject cannot be empty."

    if due_date.strip() == "":
        return False, "Due date cannot be empty."

    try:
        datetime.strptime(due_date, "%d-%m-%Y")
    except ValueError:
        return False, "Invalid date format. Use DD-MM-YYYY"

    if priority.strip() == "":
        return False, "Priority cannot be empty."

    task = {
        "title": title,
        "subject": subject,
        "due date": due_date,
        "priority": priority,
        "status": "pending",
    }

    tasks.append(task)
    save_data()

    return True, "Task added successfully!"

def add_study_session(subject, duration):

    if subject.strip() == "":
        return False, "Subject cannot be empty."

    if subject not in subjects:
        return False, "Subject not found."

    try:
        duration = int(duration)
    except ValueError:
        return False, "Duration must be a number."

    if duration <= 0:
        return False, "Duration must be greater than 0."

    session = {
        "subject": subject,
        "duration": duration,
        "date": datetime.now().strftime("%d-%m-%Y")
    }

    study_sessions.append(session)
    save_data()

    return True, "Study session added successfully!"

def view_study_sessions():

    if len(study_sessions) == 0:
        print("No study sessions available.")
        return

    print("\n========================================")
    print("          STUDY SESSIONS")
    print("========================================")

    for number, session in enumerate(study_sessions, start=1):

        print(f"\nSession #{number}")
        print("----------------------------------------")
        print("Subject  :", session["subject"])
        print("Duration :", session["duration"], "minutes")
        print("Date     :", session["date"])
        print("----------------------------------------")

    print("Study sessions displayed successfully!")

def progress_report():
    total_tasks = len(tasks)
    completed_tasks = len(get_completed_tasks())
    pending_tasks = len(get_pending_tasks())

    total_study_minutes = 0

    for session in study_sessions:
        total_study_minutes += session["duration"]

    print("\n========================================")
    print("           PROGRESS REPORT")
    print("========================================")
    print("Total Tasks        :", total_tasks)
    print("Completed Tasks    :", completed_tasks)
    print("Pending Tasks      :", pending_tasks)
    print("Study Time         :", total_study_minutes, "minutes")
    print("========================================")
    print("Progress report function completed.")
def view_tasks():
    if len(tasks) == 0:
        print("No tasks available")
        return

    print("\n========================================")
    print("              YOUR TASKS")
    print("========================================")

    for number, task in enumerate(tasks, start=1):
        print(f"\nTask #{number}")
        print("----------------------------------------")
        print("Title    :", task["title"])
        print("Subject  :", task["subject"])
        print("Due Date :", task["due date"])
        print("Priority :", task["priority"])
        print("Status   :", task["status"])
        print("----------------------------------------")

    print("Tasks displayed successfully!")


def get_pending_tasks():
    return [task for task in tasks if task["status"] == "pending"]

def get_overdue_tasks():
    overdue_tasks = []

    today = datetime.now()

    for task in tasks:

        if task["status"] == "pending":

            try:
                due_date = datetime.strptime(
                    task["due date"],
                    "%d-%m-%Y"
                )
            except ValueError:
                continue

            if due_date < today:
                overdue_tasks.append(task)

    return overdue_tasks

def get_completed_tasks():
    return [task for task in tasks if task["status"] == "completed"]

def view_overdue_tasks():

    overdue_tasks = get_overdue_tasks()

    if len(overdue_tasks) == 0:
        print("No overdue tasks")
        return

    print("\n========================================")
    print("            OVERDUE TASKS")
    print("========================================")

    for number, task in enumerate(overdue_tasks, start=1):

        print(f"\nTask #{number}")
        print("----------------------------------------")
        print("Title    :", task["title"])
        print("Subject  :", task["subject"])
        print("Due Date :", task["due date"])
        print("Priority :", task["priority"])
        print("Status   :", task["status"])
        print("----------------------------------------")

    print("Overdue tasks displayed successfully!")

def search_tasks(keyword):

    keyword = keyword.strip().lower()

    if keyword == "":
        return []

    results = []

    for task in tasks:
        if keyword in task["title"].lower() or keyword in task["subject"].lower():
            results.append(task)

    return results


def view_search_tasks():

    keyword = input("Enter task title or subject to search: ")

    results = search_tasks(keyword)

    if len(results) == 0:
        print("No matching tasks not found.")
        return

    print("\n========================================")
    print("            SEARCH RESULTS")
    print("========================================")

    for number, task in enumerate(results, start=1):

        print(f"\nTask #{number}")
        print("----------------------------------------")
        print("Title    :", task["title"])
        print("Subject  :", task["subject"])
        print("Due Date :", task["due date"])
        print("Priority :", task["priority"])
        print("Status   :", task["status"])
        print("----------------------------------------")

    print("Search completed successfully!")


def view_pending_tasks():
    pending_tasks = [task for task in tasks if task["status"] == "pending"]

    if len(pending_tasks) == 0:
        print("No pending tasks")
        return

    print("\n========================================")
    print("           PENDING TASKS")
    print("========================================")

    for number, task in enumerate(pending_tasks, start=1):
        print(f"\nTask #{number}")
        print("----------------------------------------")
        print("Title    :", task["title"])
        print("Subject  :", task["subject"])
        print("Due Date :", task["due date"])
        print("Priority :", task["priority"])
        print("Status   :", task["status"])
        print("----------------------------------------")

    print("Pending tasks displayed successfully!")


def view_completed_tasks():

    completed_tasks = get_completed_tasks()

    if len(completed_tasks) == 0:
        print("No completed tasks")
        return

    print("\n========================================")
    print("          COMPLETED TASKS")
    print("========================================")

    for number, task in enumerate(completed_tasks, start=1):
        print(f"\nTask #{number}")
        print("----------------------------------------")
        print("Title    :", task["title"])
        print("Subject  :", task["subject"])
        print("Due Date :", task["due date"])
        print("Priority :", task["priority"])
        print("Status   :", task["status"])
        print("----------------------------------------")

    print("Completed tasks displayed successfully!")


def complete_task():

    task_title = input("Enter the task title you completed: ")
    if task_title.strip() == "":
        print("task title cannot be empty")
        return

    for task in tasks:
        if task["title"] == task_title:
            task["status"] = "completed"
            save_data()
            print("Task completed successfully")
            return

    print("Task not found")


def show_menu():
    print("\n========================================")
    print("      STUDENT TASK & STUDY MANAGER")
    print("========================================")
    print("1. Add Subject")
    print("2. Add Task")
    print("3. View Tasks")
    print("4. Complete Task")
    print("5. Delete Subject")
    print("6. Delete Task")
    print("7. View Pending Tasks")
    print("8. View Completed Tasks")
    print("9. View Overdue Tasks")
    print("10. search task ")
    print("11. Add Study Session")
    print("12. View Study Sessions")
    print("13. Progress Report")
    print("14. Exit")
    print("========================================")


def main():
    show_menu()

    while True:

        try:
            choice = int(input("Enter your choice (1-14): "))
            if choice == 1:
                add_subject()

            elif choice == 2:
                title = input("Enter task title: ")
                subject = input("Enter subject: ")
                due_date = input("Enter due date (DD-MM-YYYY): ")
                priority = input("Enter priority: ")

                success, message = add_task(title, subject, due_date, priority)
                print(message)
            elif choice == 3:
                view_tasks()
            elif choice == 4:
                complete_task()
            elif choice == 5:
                subject = input("Enter the subject you want to delete: ")
                success, message = delete_subject(subject)
                print(message)
            elif choice == 6:
                title = input("Enter the task title you want to delete: ")
                success, message = delete_task(title)
                print(message)
            elif choice == 7:
                view_pending_tasks()
            elif choice == 8:
                view_completed_tasks()
            elif choice == 9:
                view_overdue_tasks()
            elif choice == 10:
                view_search_tasks()
            elif choice == 11:
                subject = input("Enter subject: ")
                duration = input("Enter study duration in minutes: ")

                success, message = add_study_session(subject, duration)
                print(message)
            elif choice == 12:
                view_study_sessions()
            elif choice == 13:
                progress_report()
            elif choice == 14:
                print("Exiting Student Task & Study Manager...")
                print("Thank you for using Student Task & Study Manager!")
                break
            
            else:
                print("Invalid choice. Please select a number from 1 to 14.")
        except ValueError:
            print("Please enter a number only.")


if __name__ == "__main__":
    load_data()
    main()
