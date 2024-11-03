import tkinter as tk
from tkinter import messagebox

# Class to handle student data
class StudentManager:
    def __init__(self, filename="C:/Users/cylea/SCHOOL L5/for Ms.Preeet/exercise 3/StudentMarks.txt"):  # Full path to the file
        self.filename = filename
        self.students = []
        self.load_data()
        self.calculate_totals()

    def load_data(self):
        try:
            with open(self.filename, 'r') as file:
                lines = file.readlines()
                self.num_students = int(lines[0].strip())  # First line is the number of students
                for line in lines[1:]:
                    code, name, m1, m2, m3, exam = line.strip().split(',')
                    self.students.append({
                        'code': int(code),
                        'name': name,
                        'coursework': [int(m1), int(m2), int(m3)],
                        'exam': int(exam)
                    })
        except FileNotFoundError:
            messagebox.showerror("Error", f"File '{self.filename}' not found. Please check the file location.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def calculate_totals(self):
        for student in self.students:
            student['total_coursework'] = sum(student['coursework'])
            student['total_score'] = student['total_coursework'] + student['exam']
            student['percentage'] = (student['total_score'] / 160) * 100
            student['grade'] = self.get_grade(student['percentage'])

    @staticmethod
    def get_grade(percentage):
        if percentage >= 70:
            return 'A'
        elif percentage >= 60:
            return 'B'
        elif percentage >= 50:
            return 'C'
        elif percentage >= 40:
            return 'D'
        else:
            return 'F'

    def get_highest_score(self):
        return max(self.students, key=lambda x: x['total_score'])

    def get_lowest_score(self):
        return min(self.students, key=lambda x: x['total_score'])


# Class for the GUI (Graphical User Interface)
class StudentManagerApp:
    def __init__(self, root, manager):
        self.root = root
        self.manager = manager
        self.root.title("Student Manager")  # Set the window title
        self.root.configure(bg="pink")  # Set background color to pastel pink
        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text="Student Manager", font=("Arial", 16), bg="pink")
        self.title_label.pack(pady=10)

        # Button to view all student records
        self.view_all_button = tk.Button(self.root, text="View All Student Records", command=self.view_all_records, bg="lightblue")
        self.view_all_button.pack(pady=5)

        # Button to view individual student record
        self.view_individual_button = tk.Button(self.root, text="View Individual Student Record", command=self.view_individual_record, bg="lightblue")
        self.view_individual_button.pack(pady=5)

        # Button to show the student with the highest score
        self.highest_score_button = tk.Button(self.root, text="Show Student with Highest Score", command=self.show_highest_score, bg="lightblue")
        self.highest_score_button.pack(pady=5)

        # Button to show the student with the lowest score
        self.lowest_score_button = tk.Button(self.root, text="Show Student with Lowest Score", command=self.show_lowest_score, bg="lightblue")
        self.lowest_score_button.pack(pady=5)

    def view_all_records(self):
        # Create a new window to display all students' records
        all_records = tk.Toplevel(self.root)
        all_records.title("All Student Records")
        all_records.configure(bg="pink")

        # Display each student's information
        for student in self.manager.students:
            student_info = f"{student['name']} - Code: {student['code']} - Total: {student['total_score']} - Exam: {student['exam']} - Grade: {student['grade']}"
            label = tk.Label(all_records, text=student_info, fg="blue" if student['grade'] != 'F' else "red", bg="pink")
            label.pack()

    def view_individual_record(self):
        # New window to select and view an individual student's record
        individual_record = tk.Toplevel(self.root)
        individual_record.title("Select Student")
        individual_record.configure(bg="pink")

        tk.Label(individual_record, text="Choose a student:", bg="pink").pack(pady=5)

        # List of buttons to choose a student by name
        for i, student in enumerate(self.manager.students, 1):
            button = tk.Button(individual_record, text=f"{i}. {student['name']}", command=lambda s=student: self.show_individual_record(s), bg="lightblue")
            button.pack(pady=2)

    def show_individual_record(self, student):
        # Display the selected student's details
        student_info = f"Name: {student['name']}\nCode: {student['code']}\nTotal Score: {student['total_score']}\nExam Mark: {student['exam']}\nGrade: {student['grade']}"
        messagebox.showinfo("Student Record", student_info)

    def show_highest_score(self):
        # Show the student with the highest score
        top_student = self.manager.get_highest_score()
        student_info = f"Top Scorer: {top_student['name']}\nTotal Score: {top_student['total_score']}\nGrade: {top_student['grade']}"
        messagebox.showinfo("Highest Scoring Student", student_info)

    def show_lowest_score(self):
        # Show the student with the lowest score
        bottom_student = self.manager.get_lowest_score()
        student_info = f"Lowest Scorer: {bottom_student['name']}\nTotal Score: {bottom_student['total_score']}\nGrade: {bottom_student['grade']}"
        messagebox.showinfo("Lowest Scoring Student", student_info)


# Create the main window and initialize the manager with the correct file path
root = tk.Tk()
manager = StudentManager("C:/Users/cylea/SCHOOL L5/for Ms.Preeet/exercise 3/StudentMarks.txt")  # Replace with the actual path to your file
app = StudentManagerApp(root, manager)
root.mainloop()
