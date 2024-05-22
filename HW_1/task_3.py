def is_valid_number_input(n):
    return n.isdigit() and bool(int(n))


def set_number():
    number = input(f"Enter a number: ")

    while True:
        if is_valid_number_input(number):
            return number
        else:
            number = input("Wrong input, please try again: ")


def sum_digits(number):
    num_str = str(number)
    return sum(map(int, num_str))


def main():
    number = set_number()
    result = sum_digits(number)
    while len(str(result)) > 1:
        result = sum_digits(result)
    print(result)


main()
