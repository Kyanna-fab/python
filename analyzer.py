student = []

def input_names_and_marks():
  names = input("Enter student name: ").split()
  marks = float(input("Enter student's marks: "))
  student.append((names , marks))

marks = ()
average = sum(marks) / len(marks)

def displaying_high_and_low_mark():
  highest = max(marks)
  lowest = min(marks)

def main():
  while True:
    choice = input("1.Input student name and mark\n2.Calculate average mark\n3.Display marks\n4.Exit\nchoice: ")
    if choice == "1":
      input_names_and_marks()
    elif choice == "2":
      print(average)
    elif choice == "3":
      displaying_high_and_low_mark()
    else:
        break


main()