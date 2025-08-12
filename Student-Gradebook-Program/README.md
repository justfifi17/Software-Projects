# Instructor Gradebook Program 📚

Welcome to **Instructor Gradebook Program**! This is my first draft command-line, menu-driven system designed to make your life as an instructor a whole lot easier. With it, you can manage student information, record grades, define grading policies, and calculate final scores with ease.

## Features 🌟

- **Manage Students**: Add students to your course with IDs and names.
- **Set Grading Policy**: Configure the number and weights of assignments, tests, and the final exam.
- **Record Grades**: Enter grades for assignments, tests, and the final exam.
- **Modify Grades**: Change grades if you need to make adjustments.
- **Final Grade Calculation**: Automatically calculate each student's final grade based on your defined grading policy.
- **Grade Output**: View grade data sorted by student name or student ID.

## Installation 🛠️

Follow these steps to get the Instructor Gradebook Program running on your machine:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/YourUsername/GradebookProgram.git
2. Navigate into the project directory:
   ```bash
   cd GradebookProgram
3. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv\Scripts\activate
4. Install the required dependencies (if any):
   ```bash
   pip install -r requirements.txt
5. Run the program:
   ```bash
   python gradebook.py
### Note: Replace your Username with your actual GitHub username in the clone command.

## How to Use ⚙️
The program operates via a simple command-line menu where you choose what to do by entering single-letter commands. Here’s a rundown of the available commands:

### Commands:
- S: Set up a new semester (start fresh by defining assignments, tests, and final exam weights).
- A: Add a student (enter the student's ID and name).
- P: Record programming assignment scores.
- T: Record test scores.
- F: Record the final exam score.
- C: Change a specific student's grade (for any assignment, test, or final exam).
- G: Calculate final grades for all students.
- O: Output grade data (sorted alphabetically by last name or by student ID).
- Q: Quit the program (don’t forget to save your progress!).

## Example menu:
```bash
(S) Set up new semester
(A) Add student
(P) Record programming assignment grades
(T) Record test grades
(F) Record final exam grades
(C) Change a grade
(G) Calculate final grades
(O) Output grade data
(Q) Quit

Enter your choice:
```

### Pro Tip: This is how it will look like in the beginning, so you must first set up the grading policy (using S) at the start of each semester before adding students or recording grades.

## Data Handling 💾
- Student grades are stored in a file named Grades.dat, which contains all student information and their recorded grades.
- The course structure (like the number of assignments and their weight in the final grade) is saved in policy.dat.
  
## File Formats 📑
You can use simple text-based files (CSV or JSON) for storing grades and policy data, making it easy to read, edit, or back up.

## Design Overview 🎨
This project follows an object-oriented design to represent real-world entities like:

- Student: Stores student ID, name, and grade information.
- GradePolicy: Stores course structure and weights of assessments.
- Gradebook: Manages the overall process, including student information, grades, and final grade calculations.
  
## Future Plans 🚀
- Adding a graphical user interface (GUI) for more user-friendly interactions.
- Expanding features for more flexible grading options (like dropping lowest scores).
- Integration with cloud storage for data backup.

Feel free to explore the code, make improvements, or adapt it to your own courses! If you have any issues or suggestions, don’t hesitate to reach out.

Happy grading! 🎉






