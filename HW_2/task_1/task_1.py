def read_file():
    # чтение данных из input_fin.txt
    with open('input.txt', 'r') as input_file:
        return input_file.readlines()


def write_file(students, average_score):
    # записываем студентов с оценкой выше среднего в output.txt
    with open('output.txt', 'w') as output_file:
        for name, score in students:
            if score >= average_score:
                output_file.write(f'{name},{score}\n')

    print('Done. Results written to output.txt')


def proceed_data(lines):
    students = []
    total_score = 0
    valid_lines = 0

    for line in lines:
        try:
            name, score = line.strip().split(',')
            score = int(score)
            students.append((name, score))
            total_score += score
            valid_lines += 1
        except ValueError:
            print(f'Incorrect format in line: "{line.strip()}". Line was skipped')

    if valid_lines == 0:
        print('No valid lines in the file to process')
        return [], 0

    average_score = total_score / valid_lines

    return students, average_score


def main():
    try:
        lines = read_file()
        students, average_score = proceed_data(lines)
        write_file(students, average_score)

    except FileNotFoundError:
        print('The file input_fin.txt was not found')


main()
