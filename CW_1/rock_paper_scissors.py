def is_input_valid(input_string):
    acceptable_answers = ['rock', 'paper', 'scissors']

    return bool(
        (input_string.lower() in acceptable_answers) and len(input_string) and not input_string.isspace())


def init_input(number):
    input_string = input(f'PLAYER {number} - Choose your hero (rock, paper or scissors): ')
    while not is_input_valid(input_string):
        input_string = input('Invalid input, try again: ')
    return input_string


def is_number_valid(input_number):
    return input_number.isdigit() and int(input_number) >= 2 and bool(int(input_number))


def init_users_number():
    input_number = input('Enter the number of players (no lower then 2): ')
    while not is_number_valid(input_number):
        input_number = input('Invalid input, try again: ')
    return int(input_number)


def determine_winner_sign(deck):
    rock_count = deck.count('rock')
    paper_count = deck.count('paper')
    scissors_count = deck.count('scissors')

    if (rock_count > 0 and paper_count > 0 and scissors_count > 0) or (rock_count or paper_count or scissors_count) == len(
            deck):
        return 'draw'
    elif rock_count > 0 and paper_count > 0:
        return 'paper'
    elif rock_count > 0 and scissors_count > 0:
        return 'rock'
    elif paper_count > 0 and scissors_count > 0:
        return 'scissors'
    else:
        return


def determine_winners_numbers(deck, winner_sign):
    winners_indexes = []
    for index, element in enumerate(deck):
        print(index)
        if element == winner_sign:
            winners_indexes.append(index+1)
    print(winners_indexes)
    return winners_indexes


def game():
    num_of_players = init_users_number()

    deck = []
    for i in range(0, num_of_players):
        deck.append(init_input(i+1))

    winner_sign = determine_winner_sign(deck)

    if winner_sign != 'draw':
        print(f'won users number: {determine_winners_numbers(deck, winner_sign)}')
    else:
        print('Its a draw')


game()