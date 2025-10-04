import os

doc_path = os.path.expanduser("~/Documents")
if not os.path.exists(doc_path):
    os.makedirs(doc_path)



while True:

    #Display the menu options
    print("\n====Main Menu====\n" +
          "1. Register Student\n" +
          "2. Open Student Record\n" +
          "3. Exit")

    try:
        user_input = int(input("Enter your choice: "))
        if user_input == 1:
            print("\n====Student Registration====")
            student_no = int(input("Student No: "))
            last_name = input("Last Name: ")
            first_name = input("First Name: ")
            middle_initial = input("Middle Initial: ")
            program = input("Program: ")
            age = input("Age: ")
            gender = input("Gender: ")
            birthday = input("Birthday MM/DD/YYYY: ")
            contact_no = input("Contact Number: ")

            data = [
                f"Student No.: {student_no}",
                f"Full Name: {last_name.capitalize()}, {first_name.capitalize()} {middle_initial.capitalize()}.",
                f"Program: {program.upper()}",
                f"Age: {age}",
                f"Gender: {gender.capitalize()}",
                f"Birthday: {birthday}",
                f"Contact No.: {contact_no}"
            ]

            # Save to a text file in Documents folder
            file_path = os.path.join(doc_path, f"{student_no}.txt")
            with open(file_path, "w") as f:
                for line in data:
                    f.write(line + "\n")

            print(f"Student record saved to {file_path}")

        elif user_input == 2:
            print("\n====Open Student Record====")
            student_no = input("Enter Student No: ")
            file_path = os.path.join(doc_path, f"{student_no}.txt")
            try:
                with open(file_path, "r") as f:
                    print("\n====Student Record====")
                    for line in f:
                        print(line.strip())
            except FileNotFoundError:
                print("Error: Student record not found.")

        elif user_input == 3:
            print("Goodbye!")
            break

    except ValueError:
        print("Invalid input. Please enter a valid number.")
