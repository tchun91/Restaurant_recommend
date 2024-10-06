from datetime import datetime

class TrendingRestaurants:
    """
    logic to fetch and process trending restaurants
    """

    def __init__(self, zipcode=None, restaurants=[]):
        self.zipcode = zipcode
        self.restaurants = restaurants

    def get_trending_restaurants(self):
        trending = sorted(self.restaurants, key=lambda x: (-x['rating'], x['id']))
        output = [{
            "name": restaurant["name"], 
            "avg_review": restaurant["rating"],
            "rank": index + 1
        } for index, restaurant in enumerate(trending)]
        
        return output