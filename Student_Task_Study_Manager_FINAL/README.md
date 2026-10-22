# Student Task & Study Manager

## Project Overview
Student Task & Study Manager is a Python-based application developed to help students organize their academic work in one place. The system provides a simple way to manage subjects and study-related tasks while keeping the information saved for future use.
The project was developed as a practical Python application with a graphical user interface, data storage, input validation, error handling, and automated testing.

## Main Features
The application provides the following features:
* User Login
* Add Subject
* Delete Subject
* Add Task
* Delete Task
* View All Tasks
* View Pending Tasks
* View Completed Tasks
* Search Tasks
* Complete Tasks
* progress report
* study sessions 
* profile 
* overdue task
* Exit Application
* Persistent Data Storage
* Graphical User Interface
* Input Validation
* Error Handling
* Automated Testing

## Technologies Used
The project was developed using the following technologies:
* Python
* Tkinter
* Pillow (PIL) for profile photo display
* JSON
* unittest

## Project Structure
Student_Task_Study_Manager/
│
├── main.py
├── login.py
├── gui.py
├── subjects.py
├── tasks.py
├── study_sessions.py
├── storage.py
├── validation.py
│
├── data/
│   └── study_manager.json
│
├── tests/
│   ├── test_subjects.py
│   └── test_tasks.py
│
└── README.md

## Description of Main Files
The code is divided into separate modules so that each file has one clear job. This makes the project easier to read, test, and maintain. The user interface and the functionality of the application were not changed during this restructuring.
### main.py
This file contains only the console menu display and the calls to the appropriate functions from the other modules. It does not manage the data directly.
### login.py
This file provides the login screen of the application. The user must enter valid login details before accessing the main application.
### gui.py
This file contains the graphical user interface built with Tkinter. It provides buttons and windows for the different operations. It uses the shared functions from the other modules instead of directly modifying the data lists.
### subjects.py
This file manages the subject list, including getting, adding, and deleting subjects.
### tasks.py
This file manages tasks. It includes adding, deleting, completing, and searching tasks, and filtering pending, completed, and overdue tasks.
### study_sessions.py
This file handles adding study sessions and listing them, and also calculates the total study time used in the progress report.
### storage.py
This file handles loading data from and saving data to the JSON file. It also holds the shared data lists and the student profile saving functions.
### validation.py
This file handles empty-field validation, date format checks (DD-MM-YYYY), and study duration checks.
### study_manager.json
This file is used to store subjects, tasks, study sessions, and the student profile. JSON storage allows the application data to remain available after the program is closed.
### tests/
The tests folder contains automated tests created using Python's unittest framework. These tests are used to check important parts of the application logic.

## Login Information
The current login credentials for the application are:
**Username:** `admin` 
**Password:** `1234`
After entering the correct credentials, the main Student Task & Study Manager interface opens.

## How to Run the Application
Follow these steps to run the application:

1. Open the `Student_Task_Study_Manager` project folder.
2. Make sure Python is installed on the computer.
3. Open the project in a Python-supported editor such as Visual Studio Code.
4. Run `login.py`.
5. Enter the username and password.
6. After successful login, the main application window will open.
7. Use the available buttons to manage subjects and tasks.

## Data Storage
The application stores its data in the following file:
```text
data/study_manager.json
```
Subjects, tasks, study sessions, and the student profile are saved in JSON format by `storage.py`. Whenever a new subject or task is added, or a task is completed or deleted, the stored data is updated.
This makes it possible to close the application and access the previously saved information when it is opened again.

## Input Validation

Input validation has been included to prevent incorrect or incomplete information from being entered.
For example:

* Empty subject names are not accepted.
* Duplicate subjects are prevented.
* Empty task titles are not accepted.
* Empty task subjects are not accepted.
* Empty due dates are not accepted.
* Incorrect date formats are rejected.
* Empty priority values are not accepted.
* Study duration must be a positive number.
* Invalid menu choices are handled properly.

The GUI also displays appropriate warning or error messages when invalid information is entered.

## Error Handling
The project uses error handling to make the application more reliable.
For example, `try` and `except` are used when processing dates and menu choices so that invalid input does not cause the program to stop unexpectedly.
The GUI also uses message boxes to inform the user about successful operations, invalid input, missing information, and other errors.

## Testing

Automated testing was implemented using Python's `unittest` framework.
The testing files are located in:
```text
tests/
```

The tests cover important operations such as:

* Adding a subject
* Preventing duplicate subjects
* Adding a task
* Completing a task
* Handling a non-existing task
* Searching tasks
* Rejecting an invalid date format
* Rejecting empty subjects and deleting a subject
The graphical user interface was also manually tested. The implemented GUI features were checked individually, including adding, deleting, viewing, searching, and completing subjects and tasks.
The final GUI was tested successfully and the implemented features were working as expected.

## User Interface

The application provides a graphical interface designed to make the system easier to use.
The main interface provides separate buttons for common operations, including:
* Add Subject
* Delete Subject
* Delete Task
* Add Task
* View Tasks
* Pending Tasks
* Completed Tasks
* Search Tasks
* Complete Task
* progress report
* study sessions 
* profile 
* overdue task
* Exit
Separate popup windows are used for different operations so that the user can perform each task clearly.

## Project Development
The project was developed step by step, starting from the basic application logic and gradually adding data storage, validation, testing, and the graphical interface. In the final stage, the code was refactored into separate modules (subjects, tasks, study sessions, storage, and validation) to improve its structure and maintainability.
During development, different parts of the application were tested and corrected before moving to the next stage. This helped ensure that the final version was stable and easier to use.

## Conclusion
Student Task & Study Manager provides a practical solution for managing student subjects and academic tasks. The project combines Python programming with GUI development, JSON data storage, input validation, error handling, and automated testing.
The final application provides the required task management features through a simple graphical interface and saves the user's data for later use.
