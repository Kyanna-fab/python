grocery = []
marks = []
def making_the_list():
    list = input("Enter items to your grocery list: ").strip()
    grocery.append((list))

def remove_item():
    i = input("Which item would you like to remove: ").strip()
    if i in grocery:
        grocery.remove(i)
    print(grocery)

def main():
    while True:
        choice = input("1.Make list\n2.Remove item\n3.Exit\nchoice ")
        if choice == "1":
            making_the_list()
        elif choice =="2":
           remove_item()
        else:
            break

main()
