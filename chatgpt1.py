def input_number_of_students():
    num_students = int(input("Enter the number of students in the class: "))
    return num_students

def input_student_information():
    students = []
    num_students = input_number_of_students()
    for _ in range(num_students):
        student_id = input("Enter student ID: ")
        student_name = input("Enter student name: ")
        student_dob = input("Enter student date of birth (dd/mm/yyyy): ")
        students.append((student_id, student_name, student_dob))
    return students

def input_number_of_courses():
    num_courses = int(input("Enter the number of courses: "))
    return num_courses

def input_course_information():
    courses = []
    num_courses = input_number_of_courses()
    for _ in range(num_courses):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        courses.append((course_id, course_name))
    return courses

def input_marks(students, courses):
    marks = {}
    for course_id, course_name in courses:
        print(f"Entering marks for course: {course_name} ({course_id})")
        marks[course_id] = {}
        for student_id, student_name, _ in students:
            mark = float(input(f"Enter mark for {student_name} ({student_id}): "))
            marks[course_id][student_id] = mark
    return marks

def list_courses(courses):
    print("\nList of courses:")
    for course_id, course_name in courses:
        print(f"- {course_name} ({course_id})")

def list_students(students):
    print("\nList of students:")
    for student_id, student_name, student_dob in students:
        print(f"- {student_name} ({student_id}), DOB: {student_dob}")

def show_student_marks(marks, courses, students):
    print("\nAvailable courses:")
    for i, (course_id, course_name) in enumerate(courses):
        print(f"{i + 1}. {course_name} ({course_id})")
    
    course_index = int(input("Select a course by number: ")) - 1
    selected_course = courses[course_index][0]

    print(f"\nMarks for course: {courses[course_index][1]} ({selected_course})")
    for student_id, student_name, _ in students:
        mark = marks[selected_course].get(student_id, "N/A")
        print(f"- {student_name} ({student_id}): {mark}")

def main():
    print("Welcome to the Student Mark Management System!")
    students = input_student_information()
    courses = input_course_information()
    marks = input_marks(students, courses)

    while True:
        print("\nOptions:")
        print("1. List all courses")
        print("2. List all students")
        print("3. Show student marks for a course")
        print("4. Exit")

        option = int(input("Select an option: "))
        if option == 1:
            list_courses(courses)
        elif option == 2:
            list_students(students)
        elif option == 3:
            show_student_marks(marks, courses, students)
        elif option == 4:
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
    
    #def show_the_list(list):
        #for i in enumerate(list):
           # print(i)