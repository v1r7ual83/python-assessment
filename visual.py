"""
This module is responsible for visualising the data using Matplotlib.
Any visualisations should be generated via functions in this module.
"""

import matplotlib.pyplot as plt

class Visualise:
    def __init__(self):
        pass

    @staticmethod
    def a(parks):
        labels = [f'{k} ({v.reviews_count})' for k, v in parks.items()]
        sizes = [park.reviews_count for park in parks.values()]

        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels)

        plt.title('Most Reviewed Parks')
        plt.show()

    @staticmethod
    def b(parks):
        fig, ax = plt.subplots()

        names = parks.keys()
        avg_scores = [park.avg_reviews_score for park in parks.values()]

        ax.bar(names, avg_scores, label=names)

        ax.set_ylabel('Average Reviews Score')
        ax.set_title('Average Scores')

        plt.show()

    @staticmethod
    def c(park):
        fig, ax = plt.subplots()

        top_locations = park.get_top_locations(10)

        locations = top_locations.keys()
        avg_scores = [location['avg'] for location in top_locations.values()]



        ax.bar(locations, avg_scores, label=locations)

        ax.set_ylabel('Average Reviews Score')
        ax.set_title('Park Ranking by Nationality')

        plt.show()

    @staticmethod
    def d(park):
        fig, ax = plt.subplots()

        months = park.get_avg_score_per_month()

        months_names = [month['name'] for month in months.values()]
        avg_scores = [month['avg'] for month in months.values()]

        ax.bar(months_names, avg_scores, label=months_names)

        ax.set_ylabel('Average Reviews Score')
        ax.set_title('Most Popular Month by Park')

        plt.show()