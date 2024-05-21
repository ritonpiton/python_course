def is_valid_number_input(n, min_value, max_value):
    return n.isdigit() and min_value <= int(n) <= max_value and bool(int(n))


def set_number():
    min_value = 1
    max_value = 999

    number = input(f"Enter a number (between {min_value} and {max_value}): ")

    while True:
        if is_valid_number_input(number, min_value, max_value):
            return int(number)
        else:
            number = input("Wrong input, please try again: ")


def main():
    number = set_number()

    print(number)


main()
