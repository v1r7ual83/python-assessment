class Park:
    def __init__(self, name):
        self.name = name
        self.reviews = {}

class Review:
    def __init__(self, review_id, rating, date, park):
        self.review_id = review_id
        self.rating = rating
        self.date = date
        self.park = park