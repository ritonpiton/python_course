def read_input():
    capacity = int(input("Input backpack capacity: "))
    num_of_items = int(input("Input number of items: "))

    items_set = []
    for i in range(num_of_items):
        weight = int(input(f"Enter weight of {i + 1} item: "))
        value = int(input(f"Input price of {i + 1} item: "))
        items_set.append((weight, value))

    return num_of_items, capacity, items_set


def item_fit(item, current_weight_of_backpack, capacity):
    return bool(item[0] <= capacity-current_weight_of_backpack)


def main():
    num_of_items, capacity, items = read_input()

    current_weight_of_backpack = 0
    current_price_of_backpack = 0
    current_backpack_state = []

    for i in range(num_of_items):
        if item_fit(items[i], current_weight_of_backpack, capacity):
            current_weight_of_backpack += items[i][0]
            current_price_of_backpack += items[i][1]
            current_backpack_state.append(items[i])
        
    print(f'Recommended backpack packaging: {current_backpack_state}')


main()
