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
        self.branches = Process.get_branches(self.reviews)

        # This line is just used for testing
        # time.sleep(3)
        print('Loading completed.')

    def run(self):
        TUI.print_rows_amount(self.reviews)

        while True:
            self.main_menu()

    def main_menu(self):
        selected_option = TUI.handle_input(TUI.print_main_menu)

        if selected_option == 'A':
            TUI.print_confirmed_option('A - View Data')
            self.view_data_menu()
        elif selected_option == 'B':
            TUI.print_confirmed_option('B - Visualise Data')
            print(2)
        elif selected_option == 'X':
            TUI.print_confirmed_option('X - Exit')
            exit()
        else:
            print('Wrong input!')
            self.main_menu()

    def view_data_menu(self):
        selected_option = TUI.handle_input(TUI.print_view_data_menu)

        if selected_option == 'A':
            print(1)
        elif selected_option == 'B':
            print(2)
        elif selected_option == 'C':
            print(3)
        elif selected_option == 'D':
            print(4)
        else:
            print('Wrong Input!')
            self.view_data_menu()

if __name__ == '__main__':
    Main().run()