from . import user_input
from .. import dummy_restaurants

class content_based_recommendations:
    """
    logic to fetch recommended restaurants based on the user here
    """
    def __init__(self, user_rest_input: dict = user_input, db_con = None):
        self.userId = user_rest_input['userId']
        self.db_con = db_con

    def process_db(self):
        return None
    
    def recommend(self):
        recommendations = dummy_restaurants

        output = {
        "recommendations": [
            {
                "restaurantId": restaurant["id"],
                "name": restaurant["name"],
                "cuisine": restaurant["cuisine"],
                "location": restaurant["location"],
                "rating": restaurant["rating"],
                "pricerange": restaurant["price_range"],
                "similarity_score": restaurant["similarity_score"],
                "thumbnail": restaurant["thumbnail"]
            }
            for restaurant in recommendations
        ]
    }

        return output

