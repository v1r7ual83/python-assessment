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