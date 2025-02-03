"""
This module is responsible for processing the data.  It will largely contain functions that will recieve the overall dataset and 
perfrom necessary processes in order to provide the desired result in the desired format.
It is likely that most sections will require functions to be placed in this module.
"""

import csv
from exporter import Park, Review

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
    def get_parks(reviews):
        parks = {}

        for review in reviews:
            review_id, rating, date, reviewer_location, park = review

            if park not in parks:
                parks[park] = Park(park)

            if review_id not in parks[park].reviews:
                parks[park].reviews[review_id] = Review(int(review_id), int(rating), date, reviewer_location, park)

        return parks

    @staticmethod
    def get_reviews_by_park(branch_name, reviews):
        return [review for review in reviews if review[4] == branch_name]

    """
    @staticmethod
    def get_reviews
        pass
    """