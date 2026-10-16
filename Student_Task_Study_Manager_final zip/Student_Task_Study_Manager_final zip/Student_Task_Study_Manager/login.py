import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import os


def login():

    username = username_entry.get().strip()
    password = password_entry.get()

    if username == "":
        messagebox.showwarning("Missing Username", "Please enter your username.")
        username_entry.focus()
        return

    if password == "":
        messagebox.showwarning("Missing Password", "Please enter your password.")
        password_entry.focus()
        return

    if username == "admin" and password == "1234":

        messagebox.showinfo(
            "Login Successful", "Welcome to Student Task & Study Manager!"
        )

        window.destroy()

        # Open the main GUI
        gui_path = os.path.join(os.path.dirname(__file__), "gui.py")
        subprocess.Popen([sys.executable, gui_path])

    else:

        messagebox.showerror("Login Failed", "Invalid username or password.")

        password_entry.delete(0, tk.END)
        password_entry.focus()


def toggle_password():

    if password_entry.cget("show") == "*":

        password_entry.config(show="")
        show_password_button.config(text="🙈")

    else:

        password_entry.config(show="*")
        show_password_button.config(text="👁️")


window = tk.Tk()

window.title("Login - Student Task & Study Manager")
window.geometry("750x650")
window.minsize(750, 650)
window.configure(bg="#EEF2FF")
window.resizable(True, True)
tk.Label(window, text="🎓", font=("Segoe UI Emoji", 55), bg="#EEF2FF").pack(
    pady=(55, 5)
)


tk.Label(
    window,
    text="Student Task & Study Manager",
    font=("Arial", 26, "bold"),
    fg="#312E81",
    bg="#EEF2FF",
).pack(pady=5)


tk.Label(
    window, text="Welcome back!", font=("Arial", 13), fg="#6366F1", bg="#EEF2FF"
).pack(pady=(5, 35))
login_frame = tk.Frame(window, bg="white", width=500, height=350)

login_frame.pack()
login_frame.pack_propagate(False)


tk.Label(
    login_frame, text="🔐 Login", font=("Arial", 22, "bold"), fg="#312E81", bg="white"
).pack(pady=(30, 25))
tk.Label(
    login_frame, text="Username", font=("Arial", 11, "bold"), bg="white", fg="#334155"
).pack(anchor="w", padx=70)


username_entry = tk.Entry(
    login_frame, font=("Arial", 13), width=35, relief="solid", bd=1
)

username_entry.pack(pady=(7, 15))
tk.Label(
    login_frame, text="Password", font=("Arial", 11, "bold"), bg="white", fg="#334155"
).pack(anchor="w", padx=70)


password_frame = tk.Frame(login_frame, bg="white")

password_frame.pack(pady=(7, 20))


password_entry = tk.Entry(
    password_frame, font=("Arial", 13), width=29, show="*", relief="solid", bd=1
)

password_entry.pack(side="left")


show_password_button = tk.Button(
    password_frame,
    text="👁️",
    font=("Segoe UI Emoji", 11),
    command=toggle_password,
    bg="white",
    relief="flat",
    bd=0,
    cursor="hand2",
)

show_password_button.pack(side="left", padx=5)
tk.Button(
    login_frame,
    text="🔐  Login",
    font=("Arial", 12, "bold"),
    fg="white",
    bg="#4F46E5",
    activebackground="#4338CA",
    activeforeground="white",
    width=25,
    height=2,
    relief="flat",
    bd=0,
    cursor="hand2",
    command=login,
).pack()
tk.Label(
    window,
    text="Secure access to your study manager",
    font=("Arial", 9),
    fg="#64748B",
    bg="#EEF2FF",
).pack(pady=30)
username_entry.focus()
window.mainloop()
