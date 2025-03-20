shopping = []

def add_to_list():
    items = input("Add items to list separated by a comma: ").strip()
    shopping.append((items))

def remove_from_list():
    fruit = input("Enter an item to remove: ").strip()
    if fruit in shopping:
        shopping.remove(fruit)
    print(f"{fruit} has been deleted")

def view_list():
    print(shopping)

def main():
    while True:
        choice = input("1.Add item to list\n2.Remove from list\n3.View list\nchoose choice: ")
        if choice == "1":
            add_to_list()
        elif choice == "2":
            remove_from_list()
        elif choice == "3":
            view_list()
        else:
            break

main()


