student = []

def students():
    name = input("Student name: ")
    grade = input("Student grade: ")
    student.append((name,grade))

def display():
    print("Names and grades of students: ")
    for name, grade in student:
        print(f"{name}: {grade}")

def sorting_students_by_grades():
    student.sort(reverse= True)

def main():
    while True:
        choice= input("-----------------------------------------\n|\t\tStudent Management System       |\n-----------------------------------------\n|\t1.Add Student                       |\n|\t2.Display Students                  |\n|\t3.Sort Students                     |\n|\t4.Exit program                      |\n-----------------------------------------\nChoose choice: ")
        if choice == "1":
            students()
        elif choice == "2":
            display()
        elif choice == "3":
            sorting_students_by_grades()
        else:
            break

main()