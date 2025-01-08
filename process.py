"""
This module is responsible for processing the data.  It will largely contain functions that will recieve the overall dataset and 
perfrom necessary processes in order to provide the desired result in the desired format.
It is likely that most sections will require functions to be placed in this module.
"""

import csv

class Process:
    def __init__(self):
        pass

    @staticmethod
    def read_reviews():
        with open('data/disneyland_reviews.csv', 'r') as file:
            reader = csv.reader(file)
            reader.__next__()

            reviews = []
            for review in reader:
                reviews.append(review)

            return reviews

    @staticmethod
    def count_rows(rows):
        return len(rows)

    @staticmethod
    def get_branches(reviews):
        branches = []
        for review in reviews:
            branch = review[4] # Branch name
            if branch and branch not in branches:
                branches.append(branch)
        return branches