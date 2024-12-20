class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob


class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name


class Mark:
    def __init__(self, course, student, mark):
        self.course = course
        self.student = student
        self.mark = mark


class StudentMarkManagement:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = []

    def add_student(self):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student date of birth (dd/mm/yyyy): ")
        self.students.append(Student(student_id, name, dob))

    def add_course(self):
        course_id = input("Enter course ID: ")
        name = input("Enter course name: ")
        self.courses.append(Course(course_id, name))

    def add_marks(self):
        print("\nAvailable courses:")
        for i, course in enumerate(self.courses):
            print(f"{i + 1}. {course.name} ({course.course_id})")

        course_index = int(input("Select a course by number: ")) - 1
        selected_course = self.courses[course_index]

        for student in self.students:
            mark = float(input(f"Enter mark for {student.name} ({student.student_id}): "))
            self.marks.append(Mark(selected_course, student, mark))

    def list_students(self):
        print("\nList of students:")
        for student in self.students:
            print(f"- {student.name} ({student.student_id}), DOB: {student.dob}")

    def list_courses(self):
        print("\nList of courses:")
        for course in self.courses:
            print(f"- {course.name} ({course.course_id})")

    def show_marks(self):
        print("\nAvailable courses:")
        for i, course in enumerate(self.courses):
            print(f"{i + 1}. {course.name} ({course.course_id})")

        course_index = int(input("Select a course by number: ")) - 1
        selected_course = self.courses[course_index]

        print(f"\nMarks for course: {selected_course.name} ({selected_course.course_id})")
        for mark in self.marks:
            if mark.course == selected_course:
                print(f"- {mark.student.name} ({mark.student.student_id}): {mark.mark}")

    def run(self):
        while True:
            print("\nOptions:")
            print("1. Add a student")
            print("2. Add a course")
            print("3. Add marks for a course")
            print("4. List all students")
            print("5. List all courses")
            print("6. Show student marks for a course")
            print("7. Exit")

            option = int(input("Select an option: "))
            if option == 1:
                self.add_student()
            elif option == 2:
                self.add_course()
            elif option == 3:
                self.add_marks()
            elif option == 4:
                self.list_students()
            elif option == 5:
                self.list_courses()
            elif option == 6:
                self.show_marks()
            elif option == 7:
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")


if __name__ == "__main__":
    smm = StudentMarkManagement()
    smm.run()
