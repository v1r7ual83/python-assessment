"""
TUI is short for Text-User Interface. This module is responsible for communicating with the user.
The functions in this module will display information to the user and/or retrieve a response from the user.
Each function in this module should utilise any parameters and perform user input/output.
A function may also need to format and/or structure a response e.g. return a list, tuple, etc.
Any errors or invalid inputs should be handled appropriately.
Please note that you do not need to read the data file or perform any other such processing in this module.
"""

from process import Process

class TUI:
    def __init__(self):
        pass

    @staticmethod
    def print_header():
        header = 'Disneyland Review Analyser'
        print('-' * len(header))
        print(header)
        print('-' * len(header))

    @staticmethod
    def print_reviews(reviews):
        for review in reviews:
            print(' '.join([f'{str(k).capitalize().replace('_', ' ')}: {v}.' for k, v in review.items()]), end='')
            print()

    @staticmethod
    def print_rows_amount(reviews):
        amount_of_rows = Process.count_rows(reviews)
        print(f'There are {amount_of_rows} rows.')


    @staticmethod
    def print_main_menu():
        print('Please enter the letter which corresponds with your desired menu choice:')
        print('\t [A] View Data')
        print('\t [B] Visualise Data')
        print('\t [C] Export Data')
        print('\t [X] Exit')

    @staticmethod
    def print_view_data_menu():
        print('Please enter one of the following options:')
        print('\t [A] View Reviews by Park')
        print('\t [B] Number of Reviews by Park and Reviewer Location')
        print('\t [C] Average Score per year by Park')
        print('\t [D] Average Score per Park by Reviewer Location')

    @staticmethod
    def print_visualise_data():
        print('Please enter one of the following options:')
        print('\t [A] Most Reviewed Parks')
        print('\t [B] Average Scores')
        print('\t [C] Park Ranking by Nationality')
        print('\t [D] Most Popular Month by Park')

    @staticmethod
    def print_exported_data_types():
        print('Please enter one of the following options:')
        print('\t 1. txt')
        print('\t 2. csv')
        print('\t 3. json')

    @staticmethod
    def print_confirmed_option(option):
        print(f'You have chosen option {option}')

    @staticmethod
    def handle_input(cb):
        while True:
            cb()
            i = input().strip()

            if len(i) == 0:
                print('No input detected! Try again.')
                continue
            return i

    @staticmethod
    def print_list(items):
        for item in items:
            print(f'\t-> {item}')

    @staticmethod
    def print_reviews_by_park_menu(branches):
        print('For which branch would you like to see the reviews? (Type name of the branch)')
        TUI.print_list(branches)