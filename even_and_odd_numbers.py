def separate_numbers():
    user_input = input("Enter a list of numbers separated by spaces: ")
    numbers = list(map(int, user_input.split()))
    odd_numbers = []
    even_numbers = []

    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)

    odd_tuple = tuple(odd_numbers)
    even_tuple = tuple(even_numbers)

    print("Odd numbers tuple:", odd_tuple)
    print("Even numbers tuple:", even_tuple)


separate_numbers()