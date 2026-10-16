# Developer Journal

## Milestone 1 – Project Idea and Requirements

### What I built
I decided to make a Student Task & Study Manager for students. The main idea was to manage subjects, tasks, deadlines, priorities and task status in one application.

### What I learned

I learned how to convert a simple project idea into different software requirements. I also understood what features are needed before starting the coding.

### What went wrong

In the beginning, it was not clear how to divide the whole project into small parts.

### How I fixed it

I divided the project into smaller milestones and worked on one part at a time.

### What I would improve

In the future, I would plan the complete structure before starting the implementation.

## Milestone 2 – Basic Python Program

### What I built

I created the basic Python program and started working with subjects and tasks. I used lists and dictionaries to keep the data.

### What I learned
I learned how functions, lists and dictionaries can be used together to build a small application.

### What went wrong
Sometimes I was confused about how data was stored inside dictionaries and how different functions used the same data.

### How I fixed it
I tested each function separately and checked the values stored in the lists and dictionaries.

### What I would improve
I would make the data structure clear before writing more functions.

## Milestone 3 – Subject and Task Management

### What I built
I added functions for adding subjects and adding tasks. Tasks contain information such as title, subject, due date, priority and status.

### What I learned
I learned how to create functions for different operations and how to store task information in dictionary form.

### What went wrong
I faced problems when entering task information and understanding how each value was saved.

### How I fixed it
I tested the functions with different inputs and checked the task data after adding it.

### What I would improve
I would add more input checking from the beginning.

## Milestone 4 – Task Status and Menu

### What I built
I added the task viewing and task completion functionality. I also created a menu so the user can select different operations.

### What I learned
I learned how a menu works with a loop and how the status of a task can be changed from pending to completed.

### What went wrong
At first, the program ended after some operations instead of showing the menu again.

### How I fixed it
I used a `while` loop so the menu continues running until the user selects the exit option.

### What I would improve
I would design the menu flow more clearly before implementing it.

## Milestone 5 – Data Storage

### What I built
I added JSON file storage so subjects and tasks can be saved in study_manager.json.

### What I learned
I learned how JSON can be used to store Python data and how data can be loaded again when the program starts.
### What went wrong
I faced a FileNotFoundError because the data file path was not correct.

### How I fixed it
I used the project directory path with os.path.join() and created the required data folder and JSON file.

### What I would improve
I would check the file and folder structure before running the program.

## Milestone 6 – Validation and Error Handling

### What I built
I added input validation and error handling to make the program safer to use.

### What I learned
I learned how `try` and `except` can prevent the program from stopping when the user enters an invalid value.

### What went wrong
Invalid input sometimes caused an error and stopped the program.

### How I fixed it

I used `try/except` and proper input checking so the user can try again.

### What I would improve

I would plan all possible invalid inputs before testing the program.

## Milestone 7 – Testing

### What I built
I created automated test files for subjects and tasks. I tested adding subjects, duplicate subjects, adding tasks and completing tasks.

### What I learned

I learned that testing helps find problems without checking everything manually every time.

### What went wrong
Some functions needed different test inputs, and I had to understand how `unittest` and `patch` work.

### How I fixed it

I created separate test cases and used mock inputs for functions that normally use input().

### What I would improve
I would write tests along with the functions instead of waiting until the end.

## Milestone 8 – GUI Development

### What I built

I converted the project into a graphical user interface using Tkinter. I added windows, buttons, input fields and popup messages for the main operations.

### What I learned

I learned that Tkinter is a Python library used to create graphical user interfaces. I also learned how button clicks can call Python functions.

### What went wrong

The GUI required a different way of handling input compared with the console version, and I had to connect the buttons with the existing functions.

### How I fixed it

I created separate GUI windows for different operations and connected them with the project functions.

### What I would improve

I would spend more time on the visual design and layout of the interface.

## Milestone 9 – Final Improvements

### What I built

I added extra features to improve the project. These include user login, search tasks, delete subject, delete task and the graphical interface.

### What I learned

I learned how additional features can be added to an existing application without changing its main purpose.

### What went wrong
Connecting the login screen and GUI with the existing project required some changes in how the application starts.

### How I fixed it
I separated the login and GUI into their own files and connected them with the main project.

### What I would improve

I would add more advanced features in a future version, but the current project meets the required functionality.

## Milestone 10 – Documentation and Final Testing

### What I built
I completed the project structure, tested the GUI features, ran the automated tests and created the README file and Developer Journal.

### What I learned
I learned that completing a software project is not only about writing code. Testing, documentation, error handling and user interface are also important parts of software development.

### What went wrong

During development, I faced different small errors related to file paths, data saving and program flow.

### How I fixed it
I tested the program step by step, checked the error messages and corrected the related code.

### What I would improve
In the future, I would plan the project earlier and keep better notes while developing each part.

## Final Reflection
This project helped me understand the complete basic software development process. I started with an idea and requirements, then created the Python logic, added data storage, validation and error handling, tested the functions and finally created a GUI and login system.
The most useful thing I learned was how different parts of a project work together. I also learned that testing and fixing errors are normal parts of software development.
Overall, I am satisfied with the final Student Task & Study Manager because it can store data, manage tasks and subjects, provide different task operations and give the user a simple graphical interface.
