from datetime import datetime
def is_empty(value):
    return value.strip() == ""
def validate_not_empty(value, field_name):
    if is_empty(value):
        return False, f"{field_name} cannot be empty."
    return True, ""
def validate_date(date_text):
    try:
        datetime.strptime(date_text, "%d-%m-%Y")
    except ValueError:
        return False, "Invalid date format. Use DD-MM-YYYY"
    return True, ""
def validate_duration(duration):
    try:
        duration = int(duration)
    except ValueError:
        return False, "Duration must be a number."

    if duration <= 0:
        return False, "Duration must be greater than 0."

    return True, ""
