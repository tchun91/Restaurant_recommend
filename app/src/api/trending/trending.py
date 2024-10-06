from datetime import datetime
from . import user_input
from .. import dummy_restaurants

class TrendingRestaurants:
    """
    logic to fetch and process trending restaurants
    """

    def __init__(self, user_input):
        self.zipcode = user_input.get("zipcode")
        self.restaurants = [] 

    def get_trending_restaurants(self):
        trending = sorted(dummy_restaurants, key=lambda x: (-x['rating'], x['id']))
        output = [{
            "name": restaurant["name"], 
            "avg_review": restaurant["rating"],
            "rank": index + 1
        } for index, restaurant in enumerate(trending)]
        
        return output