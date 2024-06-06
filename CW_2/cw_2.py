def is_valid_input(string):
    if string == '!':
        return string
    else:
        return string.isdigit() and bool(int(string) and int(string) <= 6)


def init_input():
    input_string = input('Input result: ')
    while not is_valid_input(input_string):
        input_string = input('Invalid input, try again: ')
    return input_string


def calculate_total(results):
    average = sum(results) / len(results)
    maximum = max(results)
    minimum = min(results)
    print(f'Average results: {average}')
    print(f'Maximum results: {maximum}')
    print(f'Minimum results: {minimum}')


def subsequence_search(arr: list):
    longest_sequence = []
    current_sequence = [arr[0]]

    for i in range(1, len(arr)):
        if arr[i] >= arr[i - 1]:
            current_sequence.append(arr[i])
        else:
            if len(current_sequence) > len(longest_sequence):
                longest_sequence = current_sequence
            current_sequence = [arr[i]]

    if len(current_sequence) > len(longest_sequence):
        longest_sequence = current_sequence

    return longest_sequence


def main():
    # print('You can enter a result of each roll and summarize an average, max and min: ')
    # print("(print '!' if you finished entering)")

    results_arr = [1, 2, 4, 6, 4, 1, 3, 4, 3, 1, 6, 5, 4, 3, 2, 1, 2, 4, 5, 6]

    # input_string = ''
    # while input_string != '!':
    #     input_string = init_input()
    #     if input_string != '!':
    #         results_arr.append(int(input_string))
    # calculate_total(results_arr)

    print(subsequence_search(results_arr))


main()
