contacts = []

def get_name_and_number():
    name = input("Enter your name: ").strip()
    number = input("Enter your phone number: ").strip()
    contacts.append((name, number))

def search_option():
    search = input("search a contact: ")

    for name, number in contacts:
        if search == name:
            print(f"Name is {search} and Contact is {number}")




def display_all():
    contacts.sort()
    print(contacts)

def main():
    while True:
        choice = input("1.Add to contact list\n2.Search a contact\n3.Display list\nChoice: ")
        if choice == "1":
            get_name_and_number()
        elif choice == "2":
            search_option()
        elif choice == "3":
            display_all()
        else:
            break

main()