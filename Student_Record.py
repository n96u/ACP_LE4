
import os

doc_path = os.path.expanduser("~/Documents")

if not os.path.exists(doc_path):
    os.makedirs(doc_path)


while True:
    print("\n====Student Record====")
    try:
        student_no = int(input(("Student No: ")))
    except ValueError:
        print("Invalid Input. Please Enter a valid data.")
    try:
        student_fullname = input(("Full Name: "))
    except ValueError:
        print("Invalid Input. Please Enter a valid data.")
    try:
        student_program = input(("Program: "))
    except ValueError:
        print("Invalid Input. Please Enter a valid data.")
    try:
        student_age = int(input(("Age: ")))
    except ValueError:
        print("Invalid Input. Please Enter a valid data.")
    try:
        student_gender = input(("Gender:"))
    except ValueError:
        print("Invalid Input. Please Enter a valid data.")
        student_birthday = input(("10/04/2025: "))
    try:
        contact_number = int(input(("Contact Number: ")))
    except ValueError:
        print("Invalid Input. Please Enter a valid data.")
    print("\n=======================\n")
