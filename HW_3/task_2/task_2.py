import json


def read_sales_data(file_path):
    try:
        with open(file_path, 'r') as input_file:
            data = json.load(input_file)
        return data
    except FileNotFoundError:
        print(f'The file {file_path} was not found')
        return {}
    except json.JSONDecodeError as e:
        print(f'An error occurred while reading file: "{e}"')
        return {}


def summarize_sales(sales_data):
    total_sales = {}
    for store, products in sales_data.items():
        for product, quantity in products.items():
            if product in total_sales:
                total_sales[product] += quantity
            else:
                total_sales[product] = quantity
    return total_sales


def write_sales_data(total_sales, file_path):
    with open(file_path, 'w') as output_file:
        json.dump(total_sales, output_file, indent=4)


def main():
    input_file = 'input.txt'
    output_file = 'output.txt'

    file = read_sales_data(input_file)
    total_sales = summarize_sales(file)
    write_sales_data(total_sales, output_file)


main()
