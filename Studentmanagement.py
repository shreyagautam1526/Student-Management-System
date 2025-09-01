#Initialising dictionary
student_grades = {}

#Add student
def students_name(name,grade):
    student_grades[name] = grade
    print(f"Added {name} with {grade}")

#Update 
def update_student(name,grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"{name} has been updated with {grade}. ")
    
    else:
        print(f"{name} is not found")

#delete student
def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} has been deleted successfully")
    else:
        print(f"{name} is not found.")

#display
def display_all_students():
    if student_grades:
        for name,grade in student_grades.items():
            print(f"{name}:{grade}")
    else:
        print(f"No student is found/added")
display_all_students()

def menu():
    while True:
        print("\n Student Grade Management System")
        print("1.Add Student")
        print("2.Update Student")
        print("3.Delete Student")
        print("4.View Student")
        print("5.Exit")

        choice = int(input("Enter the options:"))
        if choice == 1:
            name = input("Enter the name:")
            grade = int(input("Enter the grades:"))
            students_name(name,grade)

        elif choice == 2:
            name = input("Enter the updated student name:")
            grade = int(input("Enter the grades:"))
            update_student(name,grade)

        elif choice == 3:
            name = input("Enter the name:")
            delete_student(name)

        elif choice == 4:
            display_all_students()

        elif choice == 5:
            print("Closing program...")
            break

        else:
            print("Invalid syntax")
menu()


