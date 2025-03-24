to_do_list = []

def to_do():
    task = input("Add task: ").strip()
    to_do_list.append((task))

def complete():
    finished = input("completed task: ")
    if finished in to_do_list:
        to_do_list.remove(finished)
    print(f"{finished} Has been completed")
    print(to_do_list)

def main():
    while True:
        choice = input("1.Add to list\n2.Finished tasks\nchoice: ")
        if choice == 1:
            to_do()
        elif choice == 2:
            complete()
        else:
            break

main()

