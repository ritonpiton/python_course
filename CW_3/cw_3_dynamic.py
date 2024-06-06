def read_input():
    capacity = int(input("Input backpack capacity: "))
    num_of_items = int(input("Input number of items: "))

    items_set = []
    for i in range(num_of_items):
        weight = int(input(f"Enter weight of {i + 1} item: "))
        value = int(input(f"Input price of {i + 1} item: "))
        items_set.append((weight, value))

    return num_of_items, capacity, items_set


def knapsack(num_of_items, capacity, items):
    # создаем таблицу:
    # создаём двумерный массив размерами capacity X num_of_items
    table = [[0] * (capacity + 1) for _ in range(num_of_items + 1)]

    # заполняем таблицу
    for i in range(1, num_of_items + 1):
        for j in range(1, capacity + 1):
            if items[i - 1][0] <= j:
                table[i][j] = max(table[i - 1][j], table[i - 1][j - items[i - 1][0]] + items[i - 1][1])
            else:
                table[i][j] = table[i - 1][j]

    available_weight_left = capacity
    selected_items = []
    # диапазон из чисел начиная num_of_items и заканчивая 0 (не включительно) с шагом -1
    for i in range(num_of_items, 0, -1):
        if table[i][available_weight_left] != table[i - 1][available_weight_left]:
            selected_items.append(items[i - 1])
            available_weight_left -= items[i - 1][0]

    return table[num_of_items][capacity], selected_items


def main():
    num_of_items, capacity, items = read_input()

    max_value, selected_items = knapsack(num_of_items, capacity, items)

    print(f'Maximum value: {max_value}')
    print(f'Selected itrems: {selected_items}')


main()