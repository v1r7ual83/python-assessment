import csv
import json

class Exporter:
    def __init__(self):
        pass

    @staticmethod
    def export_data(reviews, format_type):
        file_name = 'data'
        data = [
            {
                "Review ID": review[0],
                "Rating": review[1],
                "Date": review[2],
                "Reviewer Location": review[3],
                "Park": review[4]
            }
            for review in reviews
        ]

        if format_type == "json":
            with open(f"{file_name}.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
            print(f"Data successfully exported as {file_name}.json")

        elif format_type == "csv":
            with open(f"{file_name}.csv", "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
            print(f"Data successfully exported as {file_name}.csv")

        elif format_type == "txt":
            with open(f"{file_name}.txt", "w", encoding="utf-8") as f:
                for review in data:
                    f.write(f"Review ID: {review['Review ID']}\n")
                    f.write(f"Rating: {review['Rating']}\n")
                    f.write(f"Date: {review['Date']}\n")
                    f.write(f"Reviewer Location: {review['Reviewer Location']}\n")
                    f.write(f"Park: {review['Park']}\n")
                    f.write("\n")
            print(f"Data successfully exported as {file_name}.txt")

        else:
            print("Invalid format! Choose from 'txt', 'csv', or 'json'.")

class Park:
    def __init__(self, name):
        self.name = name
        self.reviews = {}

    @property
    def reviews_count(self):
        return len(self.reviews)

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

    @property
    def avg_reviews_score(self):
        total = sum([review.rating for review in self.reviews.values()])
        count = len(self.reviews)
        return total / count if count > 0 else 0

    @property
    def reviewers_locations(self):
        locations = []
        for review in self.reviews.values():
            if review.reviewer_location not in locations:
                locations.append(review.reviewer_location)
        return locations

    def get_locations(self, limit = None):
        locations = {location: {'sum': 0, 'count': 0} for location in self.reviewers_locations}

        for review in self.reviews.values():
            if review.reviewer_location in locations:
                locations[review.reviewer_location]['sum'] += review.rating
                locations[review.reviewer_location]['count'] += 1

        for location in locations:
            s = locations[location]['sum']
            c = locations[location]['count']
            locations[location]['avg'] = round(s / c, 1) if c > 0 else 0

        sorted_locations = dict(sorted(locations.items(), key=lambda l: l[1]['avg'], reverse=True))

        if limit:
            return dict(list(sorted_locations.items())[:limit])
        return sorted_locations

    def get_avg_score_per_month(self):
        months = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]
        avg_scores = {i + 1: {'sum': 0, 'count': 0, 'name': month} for i, month in enumerate(months)}

        for review in self.reviews.values():
            if review.date == 'missing':
                continue

            month = int(review.date.split('-')[1])
            avg_scores[month]['count'] += 1
            avg_scores[month]['sum'] += review.rating

        for month in avg_scores.values():
            month['avg'] = round(month['sum'] / month['count'], 1) if month['count'] > 0 else 0

        return avg_scores

    def get_avg_score_for_year(self, yr):
        filtered_reviews = {review for review in self.reviews.values() if str(review.date).startswith(str(yr))}
        total = sum([review.rating for review in filtered_reviews])
        count = len(filtered_reviews)
        return round(total / count, 1) if count > 0 else 0

class Review:
    def __init__(self, review_id, rating, date, reviewer_location, park):
        self.review_id = review_id
        self.rating = rating
        self.date = date
        self.reviewer_location = reviewer_location
        self.park = park