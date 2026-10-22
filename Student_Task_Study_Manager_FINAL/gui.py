import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from datetime import datetime
from PIL import Image, ImageTk
import storage
import subjects
import tasks
import study_sessions
import validation


try:
    storage.load_data()
except Exception:
    pass

window = tk.Tk()
window.title("Student Task & Study Manager")
window.geometry("750x800")
window.minsize(750, 700)
window.configure(bg="#EEF2FF")

def add_subject_gui():

    popup = tk.Toplevel(window)
    popup.title("Add Subject")
    popup.geometry("450x300")
    popup.configure(bg="#F8FAFC")
    popup.resizable(False, False)

    tk.Label(
        popup,
        text="📚 Add New Subject",
        font=("Arial", 20, "bold"),
        fg="#312E81",
        bg="#F8FAFC"
    ).pack(pady=25)

    tk.Label(
        popup,
        text="Subject Name",
        font=("Arial", 11, "bold"),
        bg="#F8FAFC"
    ).pack()

    subject_entry = tk.Entry(
        popup,
        font=("Arial", 13),
        width=30
    )
    subject_entry.pack(pady=10)

    def save_subject():

        subject = subject_entry.get().strip()

        if validation.is_empty(subject):
            messagebox.showwarning(
                "Invalid Subject",
                "Subject cannot be empty.",
                parent=popup
            )
            return

        success, message = subjects.add_subject(subject)

        if not success:
            messagebox.showwarning(
                "Duplicate Subject",
                message,
                parent=popup
            )
            return

        messagebox.showinfo(
            "Success",
            "Subject added successfully!",
            parent=popup
        )

        popup.destroy()

    tk.Button(
        popup,
        text="Add Subject",
        command=save_subject,
        font=("Arial", 11, "bold"),
        bg="#F97316",
        fg="white",
        width=20,
        height=2,
        relief="flat"
    ).pack(pady=20)

def delete_subject_gui():

    popup = tk.Toplevel(window)
    popup.title("Delete Subject")
    popup.geometry("450x300")
    popup.configure(bg="#F8FAFC")
    popup.resizable(False, False)

    tk.Label(
        popup,
        text="🗑️ Delete Subject",
        font=("Arial", 20, "bold"),
        fg="#DC2626",
        bg="#F8FAFC"
    ).pack(pady=25)

    if len(subjects.get_subjects()) == 0:

        tk.Label(
            popup,
            text="No subjects available.",
            font=("Arial", 13),
            bg="#F8FAFC"
        ).pack(pady=30)

        return

    tk.Label(
        popup,
        text="Select Subject",
        font=("Arial", 11, "bold"),
        bg="#F8FAFC"
    ).pack()

    selected_subject = tk.StringVar()
    selected_subject.set(subjects.get_subjects()[0])

    subject_menu = tk.OptionMenu(
        popup,
        selected_subject,
        *subjects.get_subjects()
    )

    subject_menu.config(
        font=("Arial", 11),
        width=25
    )

    subject_menu.pack(pady=15)

    def delete_selected_subject():

        subject = selected_subject.get()

        success, message = subjects.delete_subject(subject)

        if success:

            messagebox.showinfo(
                "Success",
                message,
                parent=popup
            )

            popup.destroy()

        else:

            messagebox.showwarning(
                "Delete Subject",
                message,
                parent=popup
            )

    tk.Button(
        popup,
        text="Delete Subject",
        command=delete_selected_subject,
        font=("Arial", 11, "bold"),
        bg="#DC2626",
        fg="white",
        width=20,
        height=2,
        relief="flat"
    ).pack(pady=20)
def delete_task_gui():

    storage.load_data()

    popup = tk.Toplevel(window)
    popup.title("Delete Task")
    popup.geometry("500x350")
    popup.configure(bg="#F8FAFC")
    popup.resizable(False, False)

    popup.transient(window)
    popup.grab_set()
    popup.lift()
    popup.focus_force()

    tk.Label(
        popup,
        text="🗑️ Delete Task",
        font=("Arial", 20, "bold"),
        fg="#DC2626",
        bg="#F8FAFC"
    ).pack(pady=25)

    if len(tasks.get_tasks()) == 0:

        tk.Label(
            popup,
            text="No tasks available.",
            font=("Arial", 13),
            bg="#F8FAFC"
        ).pack(pady=30)

        return

    tk.Label(
        popup,
        text="Select Task",
        font=("Arial", 11, "bold"),
        bg="#F8FAFC"
    ).pack()

    selected_task = tk.StringVar()

    task_titles = [
        task["title"]
        for task in tasks.get_tasks()
    ]

    selected_task.set(task_titles[0])

    task_menu = tk.OptionMenu(
        popup,
        selected_task,
        *task_titles
    )

    task_menu.config(
        font=("Arial", 11),
        width=30
    )

    task_menu.pack(pady=15)

    def delete_selected_task():

        title = selected_task.get()

        success, message = tasks.delete_task(title)

        if success:

            messagebox.showinfo(
                "Success",
                message,
                parent=popup
            )

            popup.destroy()

        else:

            messagebox.showwarning(
                "Delete Task",
                message,
                parent=popup
            )

    tk.Button(
        popup,
        text="Delete Task",
        command=delete_selected_task,
        font=("Arial", 11, "bold"),
        bg="#DC2626",
        fg="white",
        width=20,
        height=2,
        relief="flat"
    ).pack(pady=20)
def add_task_gui():

    popup = tk.Toplevel(window)
    popup.title("Add Task")
    popup.geometry("500x500")
    popup.configure(bg="#F8FAFC")
    popup.resizable(False, False)

    tk.Label(
        popup,
        text="📝 Add New Task",
        font=("Arial", 20, "bold"),
        fg="#312E81",
        bg="#F8FAFC"
    ).pack(pady=20)

    tk.Label(
        popup,
        text="Task Title",
        font=("Arial", 10, "bold"),
        bg="#F8FAFC"
    ).pack()

    title_entry = tk.Entry(
        popup,
        font=("Arial", 12),
        width=35
    )
    title_entry.pack(pady=5)

    tk.Label(
        popup,
        text="Subject",
        font=("Arial", 10, "bold"),
        bg="#F8FAFC"
    ).pack()

    subject_entry = tk.Entry(
        popup,
        font=("Arial", 12),
        width=35
    )
    subject_entry.pack(pady=5)

    tk.Label(
        popup,
        text="Due Date (DD-MM-YYYY)",
        font=("Arial", 10, "bold"),
        bg="#F8FAFC"
    ).pack()

    date_entry = tk.Entry(
        popup,
        font=("Arial", 12),
        width=35
    )
    date_entry.pack(pady=5)

    tk.Label(
        popup,
        text="Priority",
        font=("Arial", 10, "bold"),
        bg="#F8FAFC"
    ).pack()

    priority_entry = tk.Entry(
        popup,
        font=("Arial", 12),
        width=35
    )
    priority_entry.pack(pady=5)

    def save_task():

        title = title_entry.get()
        subject = subject_entry.get()
        due_date = date_entry.get()
        priority = priority_entry.get()

        if title.strip() == "":
            messagebox.showwarning(
                "Invalid Input",
                "Task title cannot be empty.",
                parent=popup
            )
            return

        if subject.strip() == "":
            messagebox.showwarning(
                "Invalid Input",
                "Task subject cannot be empty.",
                parent=popup
            )
            return

        if due_date.strip() == "":
            messagebox.showwarning(
                "Invalid Input",
                "Due date cannot be empty.",
                parent=popup
            )
            return

        try:
            datetime.strptime(
                due_date,
                "%d-%m-%Y"
            )
        except ValueError:
            messagebox.showwarning(
                "Invalid Date",
                "Use date format DD-MM-YYYY.",
                parent=popup
            )
            return

        if priority.strip() == "":
            messagebox.showwarning(
                "Invalid Input",
                "Priority cannot be empty.",
                parent=popup
            )
            return

        success, message = tasks.add_task(
            title,
            subject,
            due_date,
            priority
        )

        if success:

            messagebox.showinfo(
                "Success",
                message,
                parent=popup
            )

            popup.destroy()

        else:

            messagebox.showwarning(
                "Invalid Input",
                message,
                parent=popup
            )

    tk.Button(
        popup,
        text="Add Task",
        command=save_task,
        font=("Arial", 11, "bold"),
        bg="#EC4899",
        fg="white",
        width=20,
        height=2,
        relief="flat"
    ).pack(pady=20)
def add_study_session_gui():

    popup = tk.Toplevel(window)
    popup.title("Add Study Session")
    popup.geometry("500x350")
    popup.configure(bg="#F8FAFC")
    popup.resizable(False, False)

    tk.Label(
        popup,
        text="📖 Add Study Session",
        font=("Arial", 20, "bold"),
        fg="#312E81",
        bg="#F8FAFC"
    ).pack(pady=25)

    tk.Label(
        popup,
        text="Select Subject",
        font=("Arial", 11, "bold"),
        bg="#F8FAFC"
    ).pack()

    if len(subjects.get_subjects()) == 0:

        tk.Label(
            popup,
            text="No subjects available.",
            font=("Arial", 13),
            bg="#F8FAFC"
        ).pack(pady=30)

        return

    selected_subject = tk.StringVar()
    selected_subject.set(subjects.get_subjects()[0])

    subject_menu = tk.OptionMenu(
        popup,
        selected_subject,
        *subjects.get_subjects()
    )

    subject_menu.config(
        font=("Arial", 11),
        width=25
    )

    subject_menu.pack(pady=10)

    tk.Label(
        popup,
        text="Study Duration (minutes)",
        font=("Arial", 11, "bold"),
        bg="#F8FAFC"
    ).pack()

    duration_entry = tk.Entry(
        popup,
        font=("Arial", 12),
        width=30
    )

    duration_entry.pack(pady=10)

    def save_session():

        subject = selected_subject.get()
        duration = duration_entry.get()

        success, message = study_sessions.add_study_session(
            subject,
            duration
        )

        if success:

            messagebox.showinfo(
                "Success",
                message,
                parent=popup
            )

            popup.destroy()

        else:

            messagebox.showwarning(
                "Invalid Input",
                message,
                parent=popup
            )

    tk.Button(
        popup,
        text="Add Study Session",
        command=save_session,
        font=("Arial", 11, "bold"),
        bg="#8B5CF6",
        fg="white",
        width=22,
        height=2,
        relief="flat"
    ).pack(pady=20)



def view_study_sessions_gui():

    popup = tk.Toplevel(window)
    popup.title("Study Sessions")
    popup.geometry("650x500")
    popup.configure(bg="#F8FAFC")

    tk.Label(
        popup,
        text="📖 Study Sessions",
        font=("Arial", 20, "bold"),
        fg="#312E81",
        bg="#F8FAFC"
    ).pack(pady=15)

    if len(study_sessions.get_study_sessions()) == 0:

        tk.Label(
            popup,
            text="No study sessions available.",
            font=("Arial", 13),
            bg="#F8FAFC"
        ).pack(pady=40)

        return

    text_box = tk.Text(
        popup,
        font=("Consolas", 11),
        width=70,
        height=20
    )

    text_box.pack(
        padx=20,
        pady=10
    )

    for number, session in enumerate(
        study_sessions.get_study_sessions(),
        start=1
    ):

        text_box.insert(
            tk.END,
            f"Session #{number}\n"
        )

        text_box.insert(
            tk.END,
            "----------------------------------------\n"
        )

        text_box.insert(
            tk.END,
            f"Subject  : {session['subject']}\n"
        )

        text_box.insert(
            tk.END,
            f"Duration : {session['duration']} minutes\n"
        )

        text_box.insert(
            tk.END,
            f"Date     : {session['date']}\n\n"
        )

    text_box.config(
        state="disabled"
    )
def progress_report_gui():

    total_tasks = len(tasks.get_tasks())
    completed_tasks = len(
        tasks.get_completed_tasks()
    )
    pending_tasks = len(
        tasks.get_pending_tasks()
    )

    total_study_minutes = study_sessions.get_total_study_minutes()

    report_window = tk.Toplevel(window)
    report_window.title("Progress Report")
    report_window.geometry("500x450")
    report_window.configure(bg="#F8FAFC")

    tk.Label(
        report_window,
        text="📊 PROGRESS REPORT",
        font=("Segoe UI", 18, "bold"),
        bg="#F8FAFC"
    ).pack(pady=20)

    report_box = tk.Text(
        report_window,
        font=("Segoe UI", 12),
        width=40,
        height=12,
        bg="white"
    )

    report_box.pack(
        padx=20,
        pady=10
    )

    report_box.insert(
        tk.END,
        f"Total Tasks        : {total_tasks}\n\n"
        f"Completed Tasks    : {completed_tasks}\n\n"
        f"Pending Tasks      : {pending_tasks}\n\n"
        f"Study Time         : {total_study_minutes} minutes"
    )

    report_box.config(
        state="disabled"
    )
def view_tasks_gui():

    popup = tk.Toplevel(window)
    popup.title("View Tasks")
    popup.geometry("650x500")
    popup.configure(bg="#F8FAFC")

    tk.Label(
        popup,
        text="👀 Your Tasks",
        font=("Arial", 20, "bold"),
        fg="#312E81",
        bg="#F8FAFC"
    ).pack(pady=15)

    if len(tasks.get_tasks()) == 0:

        tk.Label(
            popup,
            text="No tasks available.",
            font=("Arial", 13),
            bg="#F8FAFC"
        ).pack(pady=40)

        return

    text_box = tk.Text(
        popup,
        font=("Consolas", 11),
        width=70,
        height=20
    )

    text_box.pack(
        padx=20,
        pady=10
    )

    for number, task in enumerate(
        tasks.get_tasks(),
        start=1
    ):

        text_box.insert(
            tk.END,
            f"Task #{number}\n"
        )

        text_box.insert(
            tk.END,
            "----------------------------------------\n"
        )

        text_box.insert(
            tk.END,
            f"Title    : {task['title']}\n"
        )

        text_box.insert(
            tk.END,
            f"Subject  : {task['subject']}\n"
        )

        text_box.insert(
            tk.END,
            f"Due Date : {task['due date']}\n"
        )

        text_box.insert(
            tk.END,
            f"Priority : {task['priority']}\n"
        )

        text_box.insert(
            tk.END,
            f"Status   : {task['status']}\n\n"
        )

    text_box.config(
        state="disabled"
    )
def view_pending_tasks_gui():

    popup = tk.Toplevel(window)
    popup.title("Pending Tasks")
    popup.geometry("650x500")
    popup.configure(bg="#F8FAFC")

    tk.Label(
        popup,
        text="🟡 Pending Tasks",
        font=("Arial", 20, "bold"),
        fg="#B45309",
        bg="#F8FAFC"
    ).pack(pady=15)

    pending_tasks = tasks.get_pending_tasks()

    if len(pending_tasks) == 0:

        tk.Label(
            popup,
            text="No pending tasks.",
            font=("Arial", 13),
            bg="#F8FAFC"
        ).pack(pady=40)

        return

    text_box = tk.Text(
        popup,
        font=("Consolas", 11),
        width=70,
        height=20
    )

    text_box.pack(
        padx=20,
        pady=10
    )

    for number, task in enumerate(
        pending_tasks,
        start=1
    ):

        text_box.insert(
            tk.END,
            f"Task #{number}\n"
        )

        text_box.insert(
            tk.END,
            "----------------------------------------\n"
        )

        text_box.insert(
            tk.END,
            f"Title    : {task['title']}\n"
        )

        text_box.insert(
            tk.END,
            f"Subject  : {task['subject']}\n"
        )

        text_box.insert(
            tk.END,
            f"Due Date : {task['due date']}\n"
        )

        text_box.insert(
            tk.END,
            f"Priority : {task['priority']}\n"
        )

        text_box.insert(
            tk.END,
            f"Status   : {task['status']}\n\n"
        )

    text_box.config(
        state="disabled"
    )
def view_completed_tasks_gui():

    popup = tk.Toplevel(window)
    popup.title("Completed Tasks")
    popup.geometry("650x500")
    popup.configure(bg="#F8FAFC")

    tk.Label(
        popup,
        text="✅ Completed Tasks",
        font=("Arial", 20, "bold"),
        fg="#047857",
        bg="#F8FAFC"
    ).pack(pady=15)

    completed_tasks = tasks.get_completed_tasks()

    if len(completed_tasks) == 0:

        tk.Label(
            popup,
            text="No completed tasks.",
            font=("Arial", 13),
            bg="#F8FAFC"
        ).pack(pady=40)

        return

    text_box = tk.Text(
        popup,
        font=("Consolas", 11),
        width=70,
        height=20
    )

    text_box.pack(
        padx=20,
        pady=10
    )

    for number, task in enumerate(
        completed_tasks,
        start=1
    ):

        text_box.insert(
            tk.END,
            f"Task #{number}\n"
        )

        text_box.insert(
            tk.END,
            "----------------------------------------\n"
        )

        text_box.insert(
            tk.END,
            f"Title    : {task['title']}\n"
        )

        text_box.insert(
            tk.END,
            f"Subject  : {task['subject']}\n"
        )

        text_box.insert(
            tk.END,
            f"Due Date : {task['due date']}\n"
        )

        text_box.insert(
            tk.END,
            f"Priority : {task['priority']}\n"
        )

        text_box.insert(
            tk.END,
            f"Status   : {task['status']}\n\n"
        )

    text_box.config(
        state="disabled"
    )
def student_profile_gui():

    profile_window = tk.Toplevel(window)
    profile_window.title("Student Profile")
    profile_window.geometry("600x820")
    profile_window.resizable(False, False)
    profile_window.configure(bg="#F8FAFC")

    profile_window.transient(window)
    profile_window.lift()
    profile_window.focus_force()

    tk.Label(
        profile_window,
        text="👤 STUDENT PROFILE",
        font=("Arial", 22, "bold"),
        bg="#F8FAFC",
        fg="#312E81"
    ).pack(pady=(12, 8))

    photo_label = tk.Label(
        profile_window,
        text="No Photo Selected",
        font=("Arial", 10),
        bg="#E2E8F0",
        width=24,
        height=8
    )

    photo_label.pack(pady=3)

    profile = storage.get_student_profile()

    selected_photo = {
        "path": profile.get("photo", "")
    }

    def load_saved_photo():

        photo_path = profile.get("photo", "")

        if photo_path:

            try:

                photo = Image.open(photo_path)

                photo.thumbnail(
                    (180, 180),
                    Image.Resampling.LANCZOS
                )

                photo_image = ImageTk.PhotoImage(photo)

                photo_label.config(
                    image=photo_image,
                    text="",
                    width=180,
                    height=180
                )

                photo_label.image = photo_image

            except Exception:

                photo_label.config(
                    image="",
                    text="No Photo Selected",
                    width=24,
                    height=8
                )

    load_saved_photo()

    form_frame = tk.Frame(
        profile_window,
        bg="#F8FAFC"
    )

    form_frame.pack(
        fill="x",
        padx=70,
        pady=(3, 0)
    )

    tk.Label(
        form_frame,
        text="Student Name",
        font=("Arial", 10, "bold"),
        bg="#F8FAFC"
    ).pack(anchor="w")

    name_entry = tk.Entry(
        form_frame,
        font=("Arial", 11)
    )

    name_entry.pack(
        fill="x",
        pady=(2, 5)
    )

    tk.Label(
        form_frame,
        text="Roll Number",
        font=("Arial", 10, "bold"),
        bg="#F8FAFC"
    ).pack(anchor="w")

    roll_entry = tk.Entry(
        form_frame,
        font=("Arial", 11)
    )

    roll_entry.pack(
        fill="x",
        pady=(2, 5)
    )

    tk.Label(
        form_frame,
        text="Semester",
        font=("Arial", 10, "bold"),
        bg="#F8FAFC"
    ).pack(anchor="w")

    semester_entry = tk.Entry(
        form_frame,
        font=("Arial", 11)
    )

    semester_entry.pack(
        fill="x",
        pady=(2, 5)
    )

    tk.Label(
        form_frame,
        text="Program",
        font=("Arial", 10, "bold"),
        bg="#F8FAFC"
    ).pack(anchor="w")

    program_entry = tk.Entry(
        form_frame,
        font=("Arial", 11)
    )

    program_entry.pack(
        fill="x",
        pady=(2, 5)
    )

    name_entry.insert(
        0,
        profile.get("name", "")
    )

    roll_entry.insert(
        0,
        profile.get("roll_no", "")
    )

    semester_entry.insert(
        0,
        profile.get("semester", "")
    )

    program_entry.insert(
        0,
        profile.get("program", "")
    )

    button_frame = tk.Frame(
        profile_window,
        bg="#F8FAFC"
    )

    button_frame.pack(
        pady=(8, 5)
    )

    def enable_edit():

        name_entry.config(state="normal")
        roll_entry.config(state="normal")
        semester_entry.config(state="normal")
        program_entry.config(state="normal")

        change_photo_button.config(
            state="normal"
        )

        save_button.config(
            state="normal"
        )

        edit_button.config(
            state="disabled"
        )

    def choose_photo():

        file_path = filedialog.askopenfilename(
            title="Select Student Photo",
            filetypes=[
                (
                    "Image Files",
                    "*.png *.jpg *.jpeg *.gif *.bmp"
                ),
                (
                    "All Files",
                    "*.*"
                )
            ],
            parent=profile_window
        )

        if file_path:

            try:

                photo = Image.open(file_path)

                photo.thumbnail(
                    (180, 180),
                    Image.Resampling.LANCZOS
                )

                photo_image = ImageTk.PhotoImage(
                    photo
                )

                photo_label.config(
                    image=photo_image,
                    text="",
                    width=180,
                    height=180
                )

                photo_label.image = photo_image

                selected_photo["path"] = file_path

            except Exception as error:

                messagebox.showerror(
                    "Photo Error",
                    f"Could not open image: {error}",
                    parent=profile_window
                )

    def save_profile():

        name = name_entry.get().strip()
        roll_no = roll_entry.get().strip()
        semester = semester_entry.get().strip()
        program = program_entry.get().strip()

        success, message = storage.save_student_profile(
            name,
            roll_no,
            semester,
            program
        )

        if success:

            if selected_photo["path"]:

                storage.save_profile_photo(
                    selected_photo["path"]
                )

            messagebox.showinfo(
                "Profile Saved",
                message,
                parent=profile_window
            )

            name_entry.config(state="disabled")
            roll_entry.config(state="disabled")
            semester_entry.config(state="disabled")
            program_entry.config(state="disabled")

            change_photo_button.config(
                state="disabled"
            )

            save_button.config(
                state="disabled"
            )

            edit_button.config(
                state="normal"
            )

        else:

            messagebox.showerror(
                "Invalid Information",
                message,
                parent=profile_window
            )

    edit_button = tk.Button(
        button_frame,
        text="✏️ EDIT PROFILE",
        command=enable_edit,
        font=("Arial", 10, "bold"),
        bg="#6366F1",
        fg="white",
        activebackground="#4F46E5",
        activeforeground="white",
        width=20,
        height=1,
        relief="flat",
        cursor="hand2"
    )

    edit_button.pack(pady=2)

    change_photo_button = tk.Button(
        button_frame,
        text="📷 CHANGE PHOTO",
        command=choose_photo,
        font=("Arial", 10, "bold"),
        bg="#8B5CF6",
        fg="white",
        activebackground="#7C3AED",
        activeforeground="white",
        width=20,
        height=1,
        relief="flat",
        cursor="hand2"
    )

    change_photo_button.pack(pady=2)

    save_button = tk.Button(
        button_frame,
        text="💾 SAVE PROFILE",
        command=save_profile,
        font=("Arial", 10, "bold"),
        bg="#14B8A6",
        fg="white",
        activebackground="#0F766E",
        activeforeground="white",
        width=20,
        height=1,
        relief="flat",
        cursor="hand2"
    )

    save_button.pack(pady=2)

    close_button = tk.Button(
        button_frame,
        text="CLOSE",
        command=profile_window.destroy,
        font=("Arial", 10, "bold"),
        bg="#64748B",
        fg="white",
        activebackground="#475569",
        activeforeground="white",
        width=15,
        height=1,
        relief="flat",
        cursor="hand2"
    )

    close_button.pack(pady=2)

    if profile.get("name", "") == "":

        enable_edit()

    else:

        name_entry.config(state="disabled")
        roll_entry.config(state="disabled")
        semester_entry.config(state="disabled")
        program_entry.config(state="disabled")

        change_photo_button.config(
            state="disabled"
        )

        save_button.config(
            state="disabled"
        )
def view_overdue_tasks_gui():

    overdue_tasks = tasks.get_overdue_tasks()

    result_window = tk.Toplevel(window)
    result_window.title("Overdue Tasks")
    result_window.geometry("600x500")
    result_window.configure(bg="#F8FAFC")

    tk.Label(
        result_window,
        text="🔴 OVERDUE TASKS",
        font=("Segoe UI", 18, "bold"),
        bg="#F8FAFC"
    ).pack(pady=20)

    result_box = tk.Text(
        result_window,
        font=("Segoe UI", 11),
        width=60,
        height=18,
        bg="white"
    )

    result_box.pack(
        padx=20,
        pady=10
    )

    if len(overdue_tasks) == 0:

        result_box.insert(
            tk.END,
            "No overdue tasks."
        )

    else:

        for number, task in enumerate(
            overdue_tasks,
            start=1
        ):

            result_box.insert(
                tk.END,
                f"Task #{number}\n"
                f"Title    : {task['title']}\n"
                f"Subject  : {task['subject']}\n"
                f"Due Date : {task['due date']}\n"
                f"Priority : {task['priority']}\n"
                f"Status   : {task['status']}\n"
                f"{'-' * 45}\n\n"
            )

    result_box.config(
        state="disabled"
    )
def search_tasks_gui():

    popup = tk.Toplevel(window)
    popup.title("Search Tasks")
    popup.geometry("650x500")
    popup.configure(bg="#F8FAFC")

    tk.Label(
        popup,
        text="🔎 Search Tasks",
        font=("Arial", 20, "bold"),
        fg="#312E81",
        bg="#F8FAFC"
    ).pack(pady=15)

    tk.Label(
        popup,
        text="Enter task title or subject",
        font=("Arial", 11, "bold"),
        bg="#F8FAFC"
    ).pack()

    search_entry = tk.Entry(
        popup,
        font=("Arial", 12),
        width=35
    )

    search_entry.pack(pady=10)

    result_box = tk.Text(
        popup,
        font=("Consolas", 11),
        width=70,
        height=15,
        state="disabled"
    )

    result_box.pack(
        padx=20,
        pady=10
    )

    def search():

        keyword = search_entry.get().strip().lower()

        result_box.config(
            state="normal"
        )

        result_box.delete(
            "1.0",
            tk.END
        )

        results = tasks.search_tasks(keyword)

        if len(results) == 0:

            result_box.insert(
                tk.END,
                "No matching tasks found."
            )

        else:

            for number, task in enumerate(
                results,
                start=1
            ):

                result_box.insert(
                    tk.END,
                    f"Task #{number}\n"
                )

                result_box.insert(
                    tk.END,
                    "----------------------------------------\n"
                )

                result_box.insert(
                    tk.END,
                    f"Title    : {task['title']}\n"
                )

                result_box.insert(
                    tk.END,
                    f"Subject  : {task['subject']}\n"
                )

                result_box.insert(
                    tk.END,
                    f"Due Date : {task['due date']}\n"
                )

                result_box.insert(
                    tk.END,
                    f"Priority : {task['priority']}\n"
                )

                result_box.insert(
                    tk.END,
                    f"Status   : {task['status']}\n\n"
                )

        result_box.config(
            state="disabled"
        )

    tk.Button(
        popup,
        text="Search",
        command=search,
        font=("Arial", 11, "bold"),
        bg="#38BDF8",
        fg="white",
        width=20,
        height=2,
        relief="flat"
    ).pack(pady=10)
def complete_task_gui():

    popup = tk.Toplevel(window)
    popup.title("Complete Task")
    popup.geometry("500x350")
    popup.configure(bg="#F8FAFC")
    popup.resizable(False, False)

    tk.Label(
        popup,
        text="✅ Complete Task",
        font=("Arial", 20, "bold"),
        fg="#047857",
        bg="#F8FAFC"
    ).pack(pady=25)

    if len(tasks.get_tasks()) == 0:

        tk.Label(
            popup,
            text="No tasks available.",
            font=("Arial", 13),
            bg="#F8FAFC"
        ).pack(pady=30)

        return

    tk.Label(
        popup,
        text="Select Task",
        font=("Arial", 11, "bold"),
        bg="#F8FAFC"
    ).pack()

    selected_task = tk.StringVar()

    task_titles = [
        task["title"]
        for task in tasks.get_tasks()
    ]

    selected_task.set(task_titles[0])

    task_menu = tk.OptionMenu(
        popup,
        selected_task,
        *task_titles
    )

    task_menu.config(
        font=("Arial", 11),
        width=30
    )

    task_menu.pack(pady=15)

    def complete_selected_task():

        title = selected_task.get()

        success, message = tasks.complete_task(title)

        if success:

            messagebox.showinfo(
                "Success",
                "Task completed successfully!",
                parent=popup
            )

            popup.destroy()

            return

        messagebox.showwarning(
            "Task Not Found",
            "Task not found.",
            parent=popup
        )

    tk.Button(
        popup,
        text="Mark as Completed",
        command=complete_selected_task,
        font=("Arial", 11, "bold"),
        bg="#059669",
        fg="white",
        width=22,
        height=2,
        relief="flat"
    ).pack(pady=20)
def exit_application():

    answer = messagebox.askyesno(
        "Exit",
        "Are you sure you want to exit?"
    )

    if answer:
        window.destroy()
tk.Label(
    window,
    text="🎓",
    font=("Segoe UI Emoji", 48),
    bg="#EEF2FF"
).pack(
    pady=(25, 0)
)


tk.Label(
    window,
    text="Student Task & Study Manager",
    font=("Arial", 25, "bold"),
    fg="#312E81",
    bg="#EEF2FF"
).pack(pady=5)


tk.Label(
    window,
    text="Organize • Study • Complete",
    font=("Arial", 12),
    fg="#6366F1",
    bg="#EEF2FF"
).pack(
    pady=(0, 30)
)
profile_button_image = None


def update_profile_button():

    global profile_button_image

    profile_name = storage.get_student_profile().get(
        "name",
        ""
    ).strip()

    photo_path = storage.get_student_profile().get(
        "photo",
        ""
    )
    if photo_path:

        try:

            photo = Image.open(photo_path)

            photo.thumbnail(
                (45, 45),
                Image.Resampling.LANCZOS
            )

            profile_button_image = ImageTk.PhotoImage(
                photo
            )
            if profile_name:

                profile_button.config(
                    image=profile_button_image,
                    text=profile_name + "\nProfile",
                    compound="top",
                    width=100,
                    height=75,
                    font=("Segoe UI", 9, "bold")
                )

            else:

                profile_button.config(
                    image=profile_button_image,
                    text="Profile",
                    compound="top",
                    width=100,
                    height=75,
                    font=("Segoe UI", 9, "bold")
                )

            return

        except Exception:

            pass
    if profile_name:

        profile_button.config(
            image="",
            text="👤\n" + profile_name + "\nProfile",
            compound="top",
            width=16,
            height=3,
            font=("Segoe UI", 9, "bold")
        )

    else:

        profile_button.config(
            image="",
            text="👤\nProfile",
            compound="top",
            width=12,
            height=3,
            font=("Segoe UI", 9, "bold")
        )
profile_button = tk.Button(
    window,
    text="👤\nProfile",
    font=("Segoe UI", 9, "bold"),
    bg="#FFFFFF",
    fg="#1E293B",
    activebackground="#E2E8F0",
    activeforeground="#1E293B",
    relief="flat",
    cursor="hand2",
    command=student_profile_gui,
    width=12,
    height=3
)

profile_button.place(
    relx=1.0,
    x=-20,
    y=15,
    anchor="ne"
)
update_profile_button()
button_frame = tk.Frame(
    window,
    bg="#EEF2FF"
)

button_frame.pack(pady=10)


def create_button(
    icon,
    text,
    bg_color,
    command,
    row,
    column
):

    button = tk.Button(
        button_frame,
        text=f"{icon}   {text}",
        font=("Segoe UI Emoji", 10, "bold"),
        fg="white",
        bg=bg_color,
        activebackground=bg_color,
        activeforeground="white",
        width=24,
        height=2,
        relief="flat",
        bd=0,
        cursor="hand2",
        command=command
    )

    button.grid(
        row=row,
        column=column,
        padx=10,
        pady=7
    )

    return button
create_button(
    "📚",
    "Add Subject",
    "#F97316",
    add_subject_gui,
    0,
    0
)

create_button(
    "🗑️",
    "Delete Subject",
    "#DC2626",
    delete_subject_gui,
    0,
    1
)

create_button(
    "🗑️",
    "Delete Task",
    "#DC2626",
    delete_task_gui,
    0,
    2
)

create_button(
    "📝",
    "Add Task",
    "#EC4899",
    add_task_gui,
    1,
    0
)

create_button(
    "👀",
    "View Tasks",
    "#6366F1",
    view_tasks_gui,
    1,
    1
)

create_button(
    "🟡",
    "Pending Tasks",
    "#F59E0B",
    view_pending_tasks_gui,
    1,
    2
)

create_button(
    "✅",
    "Completed Tasks",
    "#059669",
    view_completed_tasks_gui,
    2,
    0
)

create_button(
    "🔎",
    "Search Tasks",
    "#38BDF8",
    search_tasks_gui,
    2,
    1
)

create_button(
    "🔴",
    "Overdue Tasks",
    "#EF4444",
    view_overdue_tasks_gui,
    2,
    2
)

create_button(
    "✔️",
    "Complete Task",
    "#10B981",
    complete_task_gui,
    3,
    0
)

create_button(
    "📖",
    "Add Study Session",
    "#8B5CF6",
    add_study_session_gui,
    3,
    1
)

create_button(
    "📚",
    "View Study Sessions",
    "#7C3AED",
    view_study_sessions_gui,
    3,
    2
)

create_button(
    "📊",
    "Progress Report",
    "#0EA5E9",
    progress_report_gui,
    4,
    0
)

create_button(
    "🚪",
    "Exit",
    "#64748B",
    exit_application,
    4,
    1
)
tk.Label(
    window,
    text="Student Productivity System • Python GUI",
    font=("Arial", 9),
    fg="#64748B",
    bg="#EEF2FF"
).pack(pady=25)
window.mainloop()
