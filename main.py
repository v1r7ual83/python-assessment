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
        self.parks = Process.get_parks(self.reviews)

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
            self.a()
        elif selected_option == 'B':
            TUI.print_confirmed_option('B - Visualise Data')
            print(2)
        elif selected_option == 'X':
            TUI.print_confirmed_option('X - Exit')
            exit()
        else:
            print('Wrong input!')
            self.main_menu()

    def a(self):
        selected_option = TUI.handle_input(TUI.print_view_data_menu)

        if selected_option == 'A':
            self.a_a()
        elif selected_option == 'B':
            self.a_b()
        elif selected_option == 'C':
            self.a_c()
        elif selected_option == 'D':
            print(4)
        else:
            print('Wrong Input!')
            self.a()

    def a_a(self):
        selected_option = TUI.handle_input(lambda: TUI.print_reviews_by_park_menu(self.parks.keys()))

        if selected_option in self.parks:
            TUI.print_reviews([review.__dict__ for review in self.parks[selected_option].reviews.values()])
        else:
            print('Wrong input!')
            self.a_a()

    def a_b(self):
        selected_park = TUI.handle_input(lambda: TUI.print_list(self.parks))

        if selected_park not in self.parks:
            print('Wrong input! Try again.')
            return self.a_b()

        while True:
            selected_location = TUI.handle_input(lambda: TUI.print_list(self.parks[selected_park].reviewer_locations))

            if selected_location in self.parks[selected_park].reviewer_locations:
                num_reviews = len(Process.filter_dic(self.parks[selected_park].reviews, {"reviewer_location": selected_location}))
                print(f'Number of reviews for {selected_park} park and {selected_location} reviewer location is: {num_reviews}.')
                break

            print('Wrong input! Try again.')

    def a_c(self):
        selected_park = TUI.handle_input(lambda: TUI.print_list(self.parks))

        if selected_park not in self.parks:
            print('Wrong input! Try again.')
            return self.a_c()

        while True:
            selected_year = TUI.handle_input(lambda: TUI.print_list(self.parks[selected_park].years))

            if selected_year in self.parks[selected_park].years:
                result = self.parks[selected_park].get_avg_score_for_year(selected_year)
                print(f'Average Score for year {selected_year} is {result}.')
                break

            print('Wrong input! Try again.')

    def number_of_reviews_by_park_and_reviewer_location(self):
        pass


if __name__ == '__main__':
    Main().run()
