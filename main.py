"""
This module is responsible for the overall program flow. It controls how the user interacts with the
program and how the program behaves. It uses the other modules to interact with the user, carry out
processing, and for visualising information.

Note:   any user input/output should be done in the module 'tui'
        any processing should be done in the module 'process'
        any visualisation should be done in the module 'visual'
"""

from process import Process
from tui import TUI

import time

class Main:
    def __init__(self):
        TUI.print_header()

        print('Loading...')
        self.reviews = Process.read_reviews()
        # This line is just used for testing
        # time.sleep(3)
        print('Loading completed.')

    def run(self):
        TUI.print_rows_amount(self.reviews)

        self.choose_main_menu()

    def choose_main_menu(self):
        TUI.print_main_menu()

        selected_option = TUI.handle_input()

        if selected_option == 'A':
            TUI.print_confirmed_option('A - View Data')
            print(1)
        elif selected_option == 'B':
            TUI.print_confirmed_option('B - Visualise Data')
            print(2)
        elif selected_option == 'X':
            TUI.print_confirmed_option('X - Exit')
            exit()
        else:
            print('Wrong input!')
            self.choose_main_menu()

if __name__ == '__main__':
    Main().run()