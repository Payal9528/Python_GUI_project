# Python GUI Projects

This repository contains two beginner-friendly yet practical Python projects built with **Tkinter** for GUI applications.  
Both projects are designed to help learners understand how to create interactive desktop applications using Python.

---

## 🚀 Projects Included

### 1. Calculator (GUI)
A simple calculator application with a graphical user interface.

**Features:**
- Basic arithmetic operations (Addition, Subtraction, Multiplication, Division).
- Clear button to reset input.
- User-friendly layout with buttons for digits and operators.

**Tech Stack:**
- Python
- Tkinter (GUI library)

---

### 2. Student Management System (GUI + SQLite)
A complete student management application with database integration.

**Features:**
- Add new student records (Name, Roll No, Course, Email, Phone).
- View all students in a table.
- Delete student records.
- Clear input fields easily.
- Professional GUI with styled table and colored rows.
- SQLite database for persistent storage.

**Tech Stack:**
- Python
- Tkinter (GUI library)
- SQLite (Database)

---

## 📂 Project Structure
├── calculator.py
├── student_management_system.py
└── README.md

---

## 🛠️ How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/python-gui-projects.git

---

## 🛠️ How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ #python-gui-projects.git
cd python-gui-projects
  #Run the desired project:
python calculator.py
  #or
python student_management_system.py
🎯 Purpose
.To practice Python GUI development using Tkinter.

.To learn how to integrate databases (SQLite) with GUI applications.

.To build beginner-friendly projects that can be extended further.
🤝 Contributing
Contributions are welcome!
If you have ideas to improve the projects (like adding update/search functionality in Student Management System or advanced calculator features), feel free to fork the repo and submit a pull request.

<<<<<<< HEAD
📜 License
This project is licensed under the MIT License - see the [Looks like the result wasn't safe to show. Let's switch things up and try something else!] file for details.
=======
Run the project entrypoint (replace `main.py` with your entrypoint):

```bash
python main.py
```

If your project uses a package/module entrypoint:

```bash
python -m Python_GUI_project/simple_GUI_calc.py
```

## Project Structure

A suggested structure (update to match this repository):

```
Python_GUI_project/
├── README.md
├── requirements.txt
├── main.py                  # entrypoint for the GUI app
├── app/                     # python package (modules)
│   ├── __init__.py
│   ├── ui.py
│   └── controllers.py
├── assets/                  # images/screenshots/icons used in the GUI
├── docs/
└── tests/
```

## Development

- Follow PEP8 style guidelines.
- Run unit tests (if present) using your preferred test runner, e.g.

```bash
pytest
```

- To create a standalone executable (example using PyInstaller):

```bash
pip install pyinstaller
pyinstaller --onefile main.py
```

## Contributing

Contributions are welcome. Please:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Commit changes: `git commit -m "Add my feature"`
4. Push to fork and open a pull request

Include clear description of changes and screenshots where relevant.

## License

Add a license file (e.g., `LICENSE`) and update this section. If unsure, consider the MIT License:

```
MIT License
...
```

## Contact

Maintainer: Payal9528  
Project repository: https://github.com/Payal9528/Python_GUI_project
# Student Management System (Tkinter + SQLite)

A simple desktop Student Management System built with Python, Tkinter for the GUI, and SQLite for persistent storage. This project provides basic CRUD operations (Add, View, Delete) for student records via a clean and lightweight interface.

Repository: [Payal9528/Python_GUI_project](https://github.com/Payal9528/Python_GUI_project)

## Features
- Add student records (Name, Roll No, Course, Email, Phone)
- View stored students in a table (Treeview)
- Delete selected student records
- Persistent storage using an SQLite database (`students.db`)
- Minimal, easy-to-read Tkinter UI

## Files
- [Student_manage_sys.py](https://github.com/Payal9528/Python_GUI_project/blob/7c6cf899f743d28f899cfad966cde3bdebfb864c/Student_manage_sys.py) — main application script (Tkinter GUI + SQLite integration)

## Prerequisites
- Python 3.8+ recommended
- The following libraries are used (all are part of the Python standard library except where noted):
  - tkinter (GUI) — usually included with Python; on some Linux distributions you may need to install it separately (see Troubleshooting)
  - sqlite3 (database) — included with Python
  - ttk, messagebox — included in tkinter

## Installation / Setup
1. Clone the repository (or download the files):
   ```
   git clone https://github.com/Payal9528/Python_GUI_project.git
   cd Python_GUI_project
   ```

2. Ensure tkinter is available:
   - On Debian/Ubuntu:
     ```
     sudo apt update
     sudo apt install python3-tk
     ```
   - On Fedora:
     ```
     sudo dnf install python3-tkinter
     ```
   - On Windows and macOS, tkinter typically comes bundled with Python installers.

3. Run the application:
   ```
   python3 Student_manage_sys.py
   ```
   The application will create a local SQLite database file named `students.db` in the same directory (if it does not already exist).

## Usage
- Enter the student's details in the input fields and click "Add Student" to save the record.
- Select a row in the table and click "Delete Student" to remove a record.
- Click "Clear Fields" to reset the input form.
- Records are shown in the table below the form; the application automatically loads existing records from `students.db` on startup.

## Database
- Database file: `students.db`
- Table: `students`
- Columns:
  - id (INTEGER PRIMARY KEY AUTOINCREMENT)
  - name (TEXT NOT NULL)
  - roll (TEXT NOT NULL)
  - course (TEXT)
  - email (TEXT)
  - phone (TEXT)

To reset the database, delete `students.db` (a new empty DB will be created the next time the app runs).

## Troubleshooting
- If the GUI fails to start with an error about tkinter:
  - Ensure you have the tkinter package installed for your Python distribution (see Installation / Setup above).
- If records don't appear or database actions fail, check file permissions for the working directory and ensure Python can create/write `students.db`.

## Improvements / Ideas
- Edit / Update existing student records
- Search and filter functionality
- Export/import CSV
- Input validation (email format, phone number digits)
- Sortable table columns and pagination for large datasets
- Use virtual environment and package requirements (if adding third-party libs)

## Contributing
Contributions are welcome. Open an issue or submit a PR with changes or suggestions.

## License
Add a license of your choice (e.g., MIT). If you want, I can add a LICENSE file.

## Author
Payal9528 — GitHub: [https://github.com/Payal9528](https://github.com/Payal9528)

>>>>>>> 23ae82b0a7e49083511c16df44a59329e58e8f87
