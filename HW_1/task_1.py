def is_valid_number_input(n):
    return n.isdigit() and bool(int(n))


def set_number():
    number = input(f"Enter a number: ")

    while True:
        if is_valid_number_input(number):
            return int(number)
        else:
            number = input("Wrong input, please try again: ")


def init_triangle(number):
    for i in range(number):
        spaces = " " * (number - i - 1)
        stars = "*" * (2 * i + 1)
        print(spaces + stars)


def main():
    number = set_number()
    init_triangle(number)


main()
