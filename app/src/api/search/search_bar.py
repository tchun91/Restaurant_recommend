from datetime import datetime
from . import user_input
from .. import dummy_restaurants

class Search:
    def __init__(self, user_input):
        self.userId = user_input.get("userID")
        self.query = user_input.get("query")
        self.price_tier = user_input.get("filters", {}).get("price-tier")  
        self.category = user_input.get("filters", {}).get("category")  
        self.restaurants = [] 

    def search_bar_result(self):
        filtered_results = [restaurant for restaurant in dummy_restaurants if self.query.lower() in restaurant['name'].lower()]

        if self.price_tier:
            filtered_results = [restaurant for restaurant in filtered_results if restaurant["price_range"] == self.price_tier]

        if self.category:
            filtered_results = [restaurant for restaurant in filtered_results if restaurant["cuisine"].lower() == self.category.lower()]

        output = {
            "searchResults": [
                {
                    "restaurantId": restaurant["id"],
                    "name": restaurant["name"],
                    "cuisine": restaurant["cuisine"],
                    "location": restaurant["location"],
                    "rating": restaurant["rating"],
                    "PriceRange": restaurant["price_range"],
                    "Thumbnail": restaurant["thumbnail"]
                }
                for restaurant in filtered_results
            ],
            "RecentSearches": [
                {"SearchTerm": self.query, "timestamp": datetime.now().isoformat()}
            ]
        }

        return output
