from datetime import datetime
import storage
import validation
def get_study_sessions():
    return storage.study_sessions
def get_total_study_minutes():
    return sum(session["duration"] for session in storage.study_sessions)
def add_study_session(subject, duration):
    valid, message = validation.validate_not_empty(subject, "Subject")
    if not valid:
        return False, message

    if subject not in storage.subjects:
        return False, "Subject not found."

    valid, message = validation.validate_duration(duration)
    if not valid:
        return False, message

    session = {
        "subject": subject,
        "duration": int(duration),
        "date": datetime.now().strftime("%d-%m-%Y")
    }

    storage.study_sessions.append(session)
    storage.save_data()

    return True, "Study session added successfully!"
