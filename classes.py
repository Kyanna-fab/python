
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"



def main():
    while True:
        choice = input("1.Add person\n2.Exit\nchoice: ")
        if choice == "1":
            person1 = person(input("Enter name: "), input("Enter age: "))
        else:
            break

main()



