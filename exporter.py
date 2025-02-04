class Park:
    def __init__(self, name):
        self.name = name
        self.reviews = {}

    @property
    def reviewer_locations(self):
        locations = []
        for review in self.reviews.values():
            if review.reviewer_location not in locations:
                locations.append(review.reviewer_location)
        return locations

    @property
    def years(self):
        yrs = []
        for review in self.reviews.values():
            if review.date == 'missing':
                continue

            yr = review.date.split('-')[0]
            if yr not in yrs:
                yrs.append(yr)
        return yrs

    def get_avg_score_for_year(self, yr):
        filtered_reviews = {review for review in self.reviews.values() if str(review.date).startswith(str(yr))}
        total = sum([review.rating for review in filtered_reviews])
        count = len(filtered_reviews)
        return total / count if count > 0 else 0

class Review:
    def __init__(self, review_id, rating, date, reviewer_location, park):
        self.review_id = review_id
        self.rating = rating
        self.date = date
        self.reviewer_location = reviewer_location
        self.park = park