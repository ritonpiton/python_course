import string


def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as input_file:
            return input_file.read().translate(str.maketrans('', '', string.punctuation)).lower()
    except FileNotFoundError:
        print(f'The file {file_path} was not found')
        return []
    except IOError:
        print(f'An error occurred while reading file: {file_path}')
        return []


def count_words_in_file(file):
    return len(file.split())


def find_word(file, word):
    file_words = file.split()
    return file_words.count(word)


def count_words(file):
    unique_words = list(set(file.split()))
    words_dictionary = dict((i, unique_words.count(i)) for i in unique_words)

    for key in words_dictionary:
        words_dictionary[key] = find_word(file, key)

    return words_dictionary


def main():
    file_path = 'input.txt'

    file = read_file(file_path)

    words_counts = count_words_in_file(file)
    print('Word counts: ', words_counts)

    search_word = input('Search word: ')
    search_word_count = find_word(file, search_word)
    print(f'Found {search_word_count} times')

    words_dictionary = count_words(file)
    sorted_dictionary = (sorted(words_dictionary.items(), key=lambda item: item[1], reverse=True))
    print(sorted_dictionary[:10])


main()
