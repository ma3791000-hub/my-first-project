import json
import os

import validation

FILE_PATH = os.path.join(os.path.dirname(__file__), "data", "study_manager.json")
subjects = []
tasks = []
study_sessions = []
student_profile = {}
def load_data():
    with open(FILE_PATH, "r") as file:
        data = json.load(file)

    subjects.clear()
    tasks.clear()
    study_sessions.clear()
    student_profile.clear()

    subjects.extend(data.get("subjects", []))
    tasks.extend(data.get("tasks", []))
    study_sessions.extend(data.get("study_sessions", []))
    student_profile.update(data.get("student_profile", {}))


def save_data():
    with open(FILE_PATH, "w") as file:
        json.dump({
            "subjects": subjects,
            "tasks": tasks,
            "study_sessions": study_sessions,
            "student_profile": student_profile
        }, file, indent=4)


def get_student_profile():
    return student_profile


def save_student_profile(name, roll_no, semester, program):
    fields = [
        (name, "Name"),
        (roll_no, "Roll number"),
        (semester, "Semester"),
        (program, "Program"),
    ]

    for value, field_name in fields:
        valid, message = validation.validate_not_empty(value, field_name)
        if not valid:
            return False, message

    student_profile["name"] = name
    student_profile["roll_no"] = roll_no
    student_profile["semester"] = semester
    student_profile["program"] = program

    save_data()

    return True, "Student profile saved successfully!"


def save_profile_photo(photo_path):
    student_profile["photo"] = photo_path
    save_data()
