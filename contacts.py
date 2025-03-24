contacts = []

def get_name_and_number():
    names = input("Enter your name: ")
    phone_number = input("Enter your phone number: ")
    contacts.append((names,phone_number))

def search_option():
    search = input("search a contact: ")
    for contact in contacts:
        if search == contact:
            print(f"Name: {contact}:Phone: {contact}")
    else:
        print(f"{search} not found")

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