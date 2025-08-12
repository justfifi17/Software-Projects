import json

class DataAccess:
    @staticmethod
    def read_grades_data():
        try:
            with open("Grades.dat", 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            print("Error: Invalid data format in Grades.dat file.")
            return {}

    @staticmethod
    def write_grades_data(data):
        try:
            with open("Grades.dat", 'w') as f:
                json.dump(data, f)
        except Exception as e:
            print("Error occurred while writing to Grades.dat:", e)

    @staticmethod
    def read_policy_data():
        try:
            with open("policy.dat", 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print("Policy file not found!")
            return {}
        except json.JSONDecodeError:
            print("Error: Invalid data format in policy.dat file.")
            return {}
        
    @staticmethod
    def write_policy_data(data):
        try:
            with open("policy.dat", 'w') as f:
                json.dump(data, f)
        except Exception as e:
            print("Error occurred while writing to policy.dat:", e)

class Student:
    def __init__(self, student_id, last_name, first_name):
        self.student_id = int(student_id)
        self.last_name = last_name
        self.first_name = first_name
        self.grades = {}

    def add_grade(self, grade_type, grade):
        self.grades[grade_type] = grade

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "last_name": self.last_name,
            "first_name": self.first_name,
            "grades": self.grades
        }

    @classmethod
    def from_dict(cls, data):
        student = cls(data["student_id"], data["last_name"], data["first_name"])
        student.grades = data.get("grades", {})
        return student

    def display(self):
        return f"Student ID: {self.student_id}, Name: {self.last_name}, {self.first_name}"

class GradePolicy:
    def __init__(self):
        self.assignments = 0
        self.tests = 0
        self.final_exams = 0
        self.weights = {}

    def set_policy(self, assignments, tests, final_exams, weights):
        self.assignments = assignments
        self.tests = tests
        self.final_exams = final_exams
        self.weights = weights

    def get_policy(self):
        # Returns the current grading policy data
        return {
            "assignments": self.assignments,
            "tests": self.tests,
            "final_exams": self.final_exams,
            "weights": self.weights
        }

class Gradebook:
    def __init__(self):
        self.students = {int(k): v for k, v in DataAccess.read_grades_data().items()}
        self.grade_policy = GradePolicy()
        self.load_policy()

    def load_policy(self):
        policy_data = DataAccess.read_policy_data()
        if policy_data:
            self.grade_policy.set_policy(**policy_data)

    def setup_semester(self):
        assignments = int(input("Number of programming assignments (0-6): "))
        tests = int(input("Number of tests (0-4): "))
        final_exams = int(input("Number of final exams (0-1): "))
        weights = {
            'assignments': int(input("Weight for assignments (%): ")),
            'tests': int(input("Weight for tests (%): ")),
            'final_exams': int(input("Weight for final exams (%): "))
        }
        self.grade_policy.set_policy(assignments, tests, final_exams, weights)
        DataAccess.write_policy_data(self.grade_policy.get_policy())

    def add_student(self):
        try:
            student_id = int(input("Enter student ID (1-9999): "))
            last_name = input("Enter student's last name: ")
            first_name = input("Enter student's first name: ")
            if student_id in self.students:
                print("Student ID already exists!")
                return
            student = Student(student_id, last_name, first_name)
            self.students[student_id] = student.to_dict()
            DataAccess.write_grades_data(self.students)
            print(f"Student added: ID {student_id}, Name: {last_name}, {first_name}")
        except ValueError:
            print("Invalid input for student ID. Please ensure it is a number.")

    def record_programming_assignment(self):
        self.record_grade('P', self.grade_policy.assignments)

    def record_test_score(self):
        self.record_grade('T', self.grade_policy.tests)

    def record_final_exam_score(self):
        self.record_grade('F', self.grade_policy.final_exams)

    def record_grade(self, grade_type, number_of_grades):
        if not self.students:
            print("No students added yet!")
            return

        student_id = input("Enter student ID to record grades for: ").strip()
        try:
            student_id = int(student_id)
            if student_id not in self.students:
                print("Student ID not found!")
                return
        except ValueError:
            print("Invalid student ID. Please enter a valid number.")
            return

        if number_of_grades == 0:
            print(f"No {grade_type} grades to record.")
            return

        student_info = self.students.get(student_id)
        if student_info is None:
            print("Student ID does not exist.")
            return

        student = Student.from_dict(student_info)

        for i in range(1, number_of_grades + 1):
            grade_key = f"{grade_type}{i}"
            grade = input(f"Enter {grade_type} grade {i} for {student.display()}: ")
            try:
                grade = int(grade)
                if 0 <= grade <= 100:
                    student.grades[grade_key] = grade
                else:
                    print("Grade must be between 0 and 100.")
                    continue
            except ValueError:
                print("Invalid grade. Please enter a number.")
                continue

        # Update the student information with new grades
        self.students[student_id] = student.to_dict()
        DataAccess.write_grades_data(self.students)
        print(f"{grade_type} grades recorded successfully for student ID {student_id}.")


    def change_grade(self):
        student_id = input("Enter student ID to change grade for: ")
        try:
            student_id = int(student_id)
            if student_id not in self.students:
                print("Student ID not found!")
                return
        except ValueError:
            print("Invalid student ID. Please enter a valid number.")
            return

        grade_type = input("Enter the type of score to change (P, T, or F): ").upper()
        if grade_type not in ['P', 'T', 'F']:
            print("Invalid grade type!")
            return

        # Extract the number of grades of the chosen type
        num_grades = {
            'P': self.grade_policy.assignments,
            'T': self.grade_policy.tests,
            'F': self.grade_policy.final_exams
        }.get(grade_type, 0)

        if num_grades == 0:
            print(f"No {grade_type} grades set up to change.")
            return

        # Retrieve and list the grades for the selected type
        grades = self.students[student_id]['grades']
        print(f"Current {grade_type} grades:")
        for i in range(1, num_grades + 1):
            grade_key = f"{grade_type}{i}"
            if grade_key in grades:
                print(f"{grade_key}: {grades[grade_key]}")
            else:
                print(f"{grade_key}: Not set")

        # Ask which grade to change
        grade_number = input(f"Enter {grade_type} grade number to change (1-{num_grades}): ")
        try:
            grade_number = int(grade_number)
            if not (1 <= grade_number <= num_grades):
                print(f"Invalid grade number. Please enter a number between 1 and {num_grades}.")
                return
        except ValueError:
            print("Invalid grade number. Please enter a valid number.")
            return

        new_grade = input(f"Enter the new score for {grade_type}{grade_number}: ")
        try:
            new_grade = int(new_grade)
            if not (0 <= new_grade <= 100):
                print("Invalid grade. Please enter a number between 0 and 100.")
                return
        except ValueError:
            print("Invalid input for grade. Please enter a number.")
            return

        # Apply the change
        grade_key = f"{grade_type}{grade_number}"
        self.students[student_id]['grades'][grade_key] = new_grade
        DataAccess.write_grades_data(self.students)
        print(f"Grade for {grade_key} updated successfully.")

    def calculate_final_grades(self):
        if not self.students:
            print("No students added yet!")
            return

        weights = self.grade_policy.weights
        if sum(weights.values()) != 100:
            print("Total weights do not sum to 100%. Please check your grade policy settings.")
            return

        for student_id, student_info in self.students.items():
            student = Student.from_dict(student_info)
            final_grade = 0

            grade_types = {
                'assignments': 'P',
                'tests': 'T',
                'final_exams': 'F'
            }

            for grade_type_key, prefix in grade_types.items():
                num_grades = getattr(self.grade_policy, f"{grade_type_key}", 0)
                sum_of_grades = 0
                valid_grades_count = 0  # To count valid grades found

                for i in range(1, num_grades + 1):
                    grade_key = f"{prefix}{i}"
                    if grade_key in student.grades:
                        sum_of_grades += student.grades[grade_key]
                        valid_grades_count += 1

                if valid_grades_count > 0:
                    average_grade = sum_of_grades / valid_grades_count
                    weighted_grade = average_grade * (weights[grade_type_key] / 100)
                    final_grade += weighted_grade

            self.students[student_id]['final_grade'] = final_grade

        DataAccess.write_grades_data(self.students)
        print("Final grades calculated and updated for all students.")

    

    def output_grade_data(self):
        order_by = input("Order by name or ID (name/ID): ").lower()
        if order_by not in ["name", "id"]:
            print("Invalid ordering option. Please choose 'name' or 'ID'.")
            return

        # Helper function to sort by name
        def sort_by_name(student):
            return (student['last_name'], student['first_name'])

        # Helper function to sort by ID
        def sort_by_id(student):
            return int(student['student_id'])

        if order_by == "name":
            sorted_students = sorted(self.students.values(), key=sort_by_name)
        else:
            sorted_students = sorted(self.students.values(), key=sort_by_id)

        print("Student Grades:")
        for student in sorted_students:
            print(f"ID: {student['student_id']}, Name: {student['last_name']} {student['first_name']}, Final Grade: {student.get('final_grade', 'Not calculated')}")




class Menu:
    def display_menu(self):
        print("(S) Set up new semester")
        print("(A) Add student")
        print("(P) Record programming assignment grades")
        print("(T) Record test grades")
        print("(F) Record final exam grades")
        print("(C) Change a grade")
        print("(G) Calculate final grades")
        print("(O) Output grade data")
        print("(Q) Quit")

    def get_choice(self):
        return input("Enter your choice: ").upper()

def main():
    gradebook = Gradebook()
    menu = Menu()
    while True:
        menu.display_menu()
        choice = menu.get_choice()
        if choice == 'Q':
            break
        elif choice == 'S':
            gradebook.setup_semester()
        elif choice == 'A':
            gradebook.add_student()
        elif choice == 'P':
            gradebook.record_programming_assignment()
        elif choice == 'T':
            gradebook.record_test_score()
        elif choice == 'F':
            gradebook.record_final_exam_score()
        elif choice == 'C':
            gradebook.change_grade()
        elif choice == 'G':
            gradebook.calculate_final_grades()
        elif choice == 'O':
            gradebook.output_grade_data()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

