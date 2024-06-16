def read_file(file_path):
    # читает строки из файла и возвращает их в виде списка
    try:
        with open(file_path, 'r', encoding='utf-8') as input_file:
            return input_file.readlines()
    except FileNotFoundError:
        print(f'The file {file_path} was not found')
        return []
    except IOError:
        print(f'An error occurred while reading file: {file_path}')
        return []


def write_file(file_path, lines):
    # записывает строки в файл
    try:
        with open(file_path, 'w', encoding='utf-8') as output_file:
            output_file.writelines(lines)
    except IOError:
        print(f'An error occurred while writing file: {file_path}')
    print('Done. Results written to output.txt')


def main():
    file_path = '../task_3/output.txt'
    lines1 = read_file('input1.txt')
    lines2 = read_file('input2.txt')

    if not lines1 and not lines2:
        print('En error occurred while reading input files')
        write_file(file_path, [])
        return

    # удаляем символы перевода строки из строк и объединяем списки
    lines1 = [line.strip() for line in lines1]
    lines2 = [line.strip() for line in lines2]
    combined_lines = lines1 + lines2

    # сортируем
    combined_lines.sort()

    write_file(file_path, [line + '\n' for line in combined_lines])


main()
