class PersonalizedRecommendations:
    def __init__(self, user_id, db_con):
        self.user_id = user_id
        self.db_con = db_con  

    def get_recommendations(self):
        # query the database for personalized recommendations
        recommendations_query = (
            self.db_con.query(Restaurant)
            .filter(Restaurant.user_id == self.user_id)  
            .filter(Restaurant.is_bookmarked == True)  # Example filter, modify as needed
        )
        
        recommendations = recommendations_query.all()  # assuming this returns a list of Restaurant objects

        # transform the results into a list of dictionaries
        return [
            {
                "restaurantId": restaurant.restaurant_id,
                "name": restaurant.name,
                "cuisine": restaurant.cuisine,
                "rating": {
                    "value": restaurant.rating_value,  
                    "count": restaurant.rating_count    
                },
                "thumbnail": restaurant.thumbnail
            }
            for restaurant in recommendations
        ]