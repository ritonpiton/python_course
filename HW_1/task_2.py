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


def generate_text(number: int):
    units_words = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    teens_words = ["десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
    tens_words = ["", "десять", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
    hundreds_words = ["", "сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]

    words = []

    # разбиваем на сотни
    hundred = number // 100
    # разбиваем на десятки
    ten = (number % 100) // 10
    # разбиваем на единицы
    unit = number % 10

    if hundred > 0:
        words.append(hundreds_words[hundred])
    if ten == 1:
        words.append(teens_words[unit])
    else:
        if ten > 0:
            words.append(tens_words[ten])
        if unit > 0:
            words.append(units_words[unit])
    return " ".join(words)


def main():
    number = set_number()
    result = generate_text(number)
    print(result)


main()
