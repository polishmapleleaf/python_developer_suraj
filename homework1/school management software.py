

students = []
teachers = []
homeroom_teachers = []

def display_main_menu():
    print("\n Available commands ")
    print("Enter 'create' - To create a new user ")
    print("Enter 'manage' - To Manage existing users ")
    print("Enter 'end' - To exit the program ")

def create_user():
    while True:
        print(" choose user type to create: ")
        print(" student"
              "\n teacher"
              "\n homeroom teacher"
              "\n end")
        user_type = input(" enter user type: ").strip().lower()

        if user_type == "student":
            first_name = input("enter students first name: ").strip()
            last_name = input("enter students last name: ").strip()
            class_name = input("enter students class name: ").strip()
            students.append({'first name' : first_name, 'last name' : last_name, 'class name' : class_name })
            print(f"student {first_name} {last_name} added to class {class_name}")

        elif user_type == 'teacher':
            first_name = input("enter teacher first name: ").strip()
            last_name = input("enter teacher last name: ").strip()
            subject = input("enter subject: ").strip()
            class_list = []
            print(" enter class names - enter empty line to finish ")
            while True:
                cls = input("class name ").strip()
                if cls == "":
                    break
                class_list.append(cls)
            teachers.append({'first name' : first_name, 'last name' : last_name, 'subject' : subject, 'classes' : class_list})
            print(f"teacher {first_name} {last_name} added with subject {subject} for classes {class_list}")

        elif user_type =="homeroom teacher":
            first_name = input("enter homeroom teacher first name: ").strip()
            last_name = input("enter homeroom teacher last name: ").strip()
            class_name = input("enter homeroom teacher class name: ").strip()
            homeroom_teachers.append({'first name ': first_name, 'last name ': last_name, 'class name ' : class_name})
            print(f" homeroom teacher {first_name} {last_name} assigned to class {class_name}")

        elif user_type == 'end':
            break
        else:
            print("invalid user type, try again ")



def manage_users():
    while True:
        print("\n Choose your options to manage from the list:"
              "\n class"
              "\n student"
              "\n teacher"
              "\n homeroom teacher"
              "\n end")
        option = input("Enter option: ").strip().lower()

        if option == 'class':
            class_name = input("Enter class name: ").strip()
            print(f"\n Students in {class_name}:")
            found = False
            for student in students:
                if student['class name'] == class_name:
                    print(f" - {student['first name']} {student['last name']}")
                    found = True

            for ht in homeroom_teachers:
                if ht['class name '] == class_name:
                    print(f" homeroom teacher: {ht['first name ']} {ht['last name ']}")
                    found = True

            if not found:
                print(f" no data found for {class_name} class")

        elif option == 'student':
            first_name = input("Enter student's first name: ").strip()
            last_name = input("Enter student's last name: ").strip()
            student_classes = [s['class name'] for s in students if s['first name'] == first_name and s['last name'] == last_name]

            if student_classes:
                print(f"\n{first_name} {last_name} attends: {', '.join(student_classes)}")
                print("Taught by:")
                for teacher in teachers:
                    for cls in teacher['classes']:
                        if cls in student_classes:
                            print(f" - {teacher['first name']} {teacher['last name']} ({teacher['subject']})")
            else:
                print("Student not found.")

        elif option == 'teacher':
            first_name = input("Teacher's first name: ").strip()
            last_name = input("Teacher's last name: ").strip()
            found = False
            for teacher in teachers:
                if teacher['first name'] == first_name and teacher['last name'] == last_name:
                    print(f"\n{first_name} {last_name} teaches {teacher['subject']} in classes: {', '.join(teacher['classes'])}")
                    found = True
                    break
            if not found:
                print("Teacher not found.")

        elif option == 'homeroom teacher':
            first_name = input("Homeroom teacher's first name: ").strip()
            last_name = input("Homeroom teacher's last name: ").strip()
            found = False
            for ht in homeroom_teachers:
                if ht['first name '] == first_name and ht['last name '] == last_name:
                    class_name = ht['class name ']
                    print(f"\n{first_name} {last_name} leads class {class_name}")
                    print("Students:")
                    for student in students:
                        if student['class name'] == class_name:
                            print(f" - {student['first name']} {student['last name']}")
                    found = True
                    break
            if not found:
                print("Homeroom teacher not found.")

        elif option == 'end':
            break

        else:
            print("Invalid option. Try again.")


def main():
    print("\nWelcome to School Database Management System")
    while True:
        try:
            display_main_menu()
            command = input("Enter command: ").strip().lower()

            if command == 'create':
                create_user()
            elif command == 'manage':
                manage_users()
            elif command == 'end':
                print("Thanks for using our system.....")
                break
            else:
                print("Invalid command, please try again")

        except ValueError as ve:
            print(f"ValueError: {ve}. Please enter valid input.")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == '__main__':
    main()

