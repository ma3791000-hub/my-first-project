import storage
import validation
def get_subjects():
    return storage.subjects


def add_subject(subject):
    subject = subject.strip()

    valid, message = validation.validate_not_empty(subject, "Subject")
    if not valid:
        return False, message

    if subject in storage.subjects:
        return False, "Subject already exists."

    storage.subjects.append(subject)
    storage.save_data()

    return True, "Subject added successfully!"
def delete_subject(subject):
    valid, message = validation.validate_not_empty(subject, "Subject")
    if not valid:
        return False, message

    if subject in storage.subjects:
        storage.subjects.remove(subject)
        storage.save_data()
        return True, "Subject deleted successfully!"

    return False, "Subject not found."
