from . import user_input
from typing import List, Dict
from collections import Counter

class TrendingCategory:
    """
    This class calculates trending categories based on zipcode
    """
    def __init__(
            self,
            trending_input: dict = user_input,
            db_con = None
    ):
        self.zipcode = trending_input['zipcode']
        self.db_con = db_con

    def get_trending_categories(self):
        restaurants = self._get_restaurants_by_zipcode()
        
        return self._calculate_trending(restaurants)

    def _get_restaurants_by_zipcode(self):
        # Implement db query
        return []

    def _calculate_trending(self, restaurants: List[Dict]):

        cuisine_count = Counter(restaurant['cuisine'] for restaurant in restaurants)
        trending = sorted(cuisine_count.items(), key=lambda x: (-x[1], x[0]))
        
        output = [
            {"name": cuisine, "rank": index + 1}
            for index, (cuisine, count) in enumerate(trending)
        ]
        
        return output