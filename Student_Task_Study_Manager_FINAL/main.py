import storage
import subjects
import tasks
import study_sessions


def print_task_list(title, task_list, footer):
    print("\n========================================")
    print(title)
    print("========================================")

    for number, task in enumerate(task_list, start=1):
        print(f"\nTask #{number}")
        print("----------------------------------------")
        print("Title    :", task["title"])
        print("Subject  :", task["subject"])
        print("Due Date :", task["due date"])
        print("Priority :", task["priority"])
        print("Status   :", task["status"])
        print("----------------------------------------")

    print(footer)


def view_tasks():
    task_list = tasks.get_tasks()
    if len(task_list) == 0:
        print("No tasks available")
        return
    print_task_list("              YOUR TASKS", task_list, "Tasks displayed successfully!")


def view_pending_tasks():
    task_list = tasks.get_pending_tasks()
    if len(task_list) == 0:
        print("No pending tasks")
        return
    print_task_list("           PENDING TASKS", task_list, "Pending tasks displayed successfully!")


def view_completed_tasks():
    task_list = tasks.get_completed_tasks()
    if len(task_list) == 0:
        print("No completed tasks")
        return
    print_task_list("          COMPLETED TASKS", task_list, "Completed tasks displayed successfully!")


def view_overdue_tasks():
    task_list = tasks.get_overdue_tasks()
    if len(task_list) == 0:
        print("No overdue tasks")
        return
    print_task_list("            OVERDUE TASKS", task_list, "Overdue tasks displayed successfully!")


def view_search_tasks():
    keyword = input("Enter task title or subject to search: ")
    results = tasks.search_tasks(keyword)
    if len(results) == 0:
        print("No matching tasks not found.")
        return
    print_task_list("            SEARCH RESULTS", results, "Search completed successfully!")


def view_study_sessions():
    session_list = study_sessions.get_study_sessions()

    if len(session_list) == 0:
        print("No study sessions available.")
        return

    print("\n========================================")
    print("          STUDY SESSIONS")
    print("========================================")

    for number, session in enumerate(session_list, start=1):
        print(f"\nSession #{number}")
        print("----------------------------------------")
        print("Subject  :", session["subject"])
        print("Duration :", session["duration"], "minutes")
        print("Date     :", session["date"])
        print("----------------------------------------")

    print("Study sessions displayed successfully!")


def progress_report():
    print("\n========================================")
    print("           PROGRESS REPORT")
    print("========================================")
    print("Total Tasks        :", len(tasks.get_tasks()))
    print("Completed Tasks    :", len(tasks.get_completed_tasks()))
    print("Pending Tasks      :", len(tasks.get_pending_tasks()))
    print("Study Time         :", study_sessions.get_total_study_minutes(), "minutes")
    print("========================================")
    print("Progress report function completed.")


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
                subject = input("Enter your subject: ")
                success, message = subjects.add_subject(subject)
                print(message)
            elif choice == 2:
                title = input("Enter task title: ")
                subject = input("Enter subject: ")
                due_date = input("Enter due date (DD-MM-YYYY): ")
                priority = input("Enter priority: ")
                success, message = tasks.add_task(title, subject, due_date, priority)
                print(message)
            elif choice == 3:
                view_tasks()
            elif choice == 4:
                title = input("Enter the task title you completed: ")
                success, message = tasks.complete_task(title)
                print(message)
            elif choice == 5:
                subject = input("Enter the subject you want to delete: ")
                success, message = subjects.delete_subject(subject)
                print(message)
            elif choice == 6:
                title = input("Enter the task title you want to delete: ")
                success, message = tasks.delete_task(title)
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
                success, message = study_sessions.add_study_session(subject, duration)
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
    storage.load_data()
    main()
