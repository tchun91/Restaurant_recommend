from . import user_input

class RestaurantInfo:
    """
    This class retrieves general information about a restaurant
    """
    def __init__(self, restaurant_input = user_input, db_con = None):
        self.restaurant_id = restaurant_input['restaurant_id']
        self.db_con = db_con

    def get_restaurant_info(self):
        restaurant = self._get_restaurant_from_db()
        
        if not restaurant:
            return None
        
        return {
            "restaurantId": restaurant['id'],
            "name": restaurant['name'],
            "cuisine": restaurant['cuisine'],
            "location": restaurant['location'],
            "rating": restaurant['rating'],
            "priceRange": restaurant['price_range'],
            "thumbnail": restaurant['thumbnail']
        }

    def _get_restaurant_from_db(self):
        # Implement db query
        return None