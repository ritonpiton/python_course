def greatest_common_divisor(a, b):
    if b == 0:
        return a
    else:
        return greatest_common_divisor(b, a % b)


def main():
    try:
        num1 = int(input('Enter first number: '))
        num2 = int(input('Enter second number: '))
        print(f'GCD of {num1} and {num2} is {greatest_common_divisor(num1, num2)}')
    except ValueError:
        print('Please enter an integer')


main()
