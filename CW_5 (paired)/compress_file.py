import string
import json
from collections import Counter


def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as input_file:
            return input_file.read()
    except FileNotFoundError:
        print(f'The file {file_path} was not found')
        return []
    except IOError:
        print(f'An error occurred while reading file: {file_path}')
        return []


def find_word_positions(text, search_word):
    words = text.split()
    word_positions = [index for index, word in enumerate(words) if search_word in word]
    return word_positions


def find_high_memory_words(file, min_length=5, threshold=50):
    words = file.split()
    word_freq = Counter(words)

    word_memory_usage = {
        word: len(word) * freq
        for word, freq in word_freq.items()
        if len(word) >= min_length and len(word) * freq > threshold
    }

    return word_memory_usage


def create_rules(file, high_memory_words):
    output_file = 'rules.txt'

    for word in high_memory_words:
        high_memory_words[word] = find_word_positions(file, word)

    with open(output_file, 'w', encoding='utf-8') as output_file:
        json.dump(high_memory_words, output_file, separators=(',', ':'))

    return high_memory_words


def remove_words_at_positions(file, words_positions):
    words = file.split()

    positions_to_remove = sorted(set(pos for positions in words_positions.values() for pos in positions), reverse=True)

    for position in positions_to_remove:
        del words[position]

    new_text = ' '.join(words)
    with open('input_f.txt', 'w', encoding='utf-8') as output_file:
        output_file.write(new_text)

    return new_text


def main():
    input_file = 'input_i.txt'

    file = read_file(input_file)

    if not file:
        return

    high_memory_words = find_high_memory_words(file)
    rules = create_rules(file, high_memory_words)
    remove_words_at_positions(file, rules)


main()
