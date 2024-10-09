class SavedRestaurants:
    def __init__(self, user_id: str, is_bookmarked: bool = None, db_con=None):
        self.user_id = user_id
        self.is_bookmarked = is_bookmarked
        self.db_con = db_con  

    def get_saved_restaurants(self):
        # fetching saved restaurants for the given user_id from the database
        saved_restaurants_query = (
            self.db_con.query(Restaurant)
            .filter(Restaurant.user_id == self.user_id)  # assuming a foreign key relationship
        )
        
        if self.is_bookmarked is not None:
            saved_restaurants_query = saved_restaurants_query.filter(Restaurant.is_bookmarked == self.is_bookmarked)
        
        return saved_restaurants_query.all()  

    def save_restaurant(self, restaurant_id: str):
        import datetime
        
        created_on = datetime.datetime.now()  # capture timestamp
        new_restaurant = Restaurant(
            user_id=self.user_id,
            restaurant_id=restaurant_id,
            created_on=created_on,
            is_bookmarked=True  # Default bookmarked
        )
        
        # save the restaurant to the database
        self.db_con.add(new_restaurant)  # assuming 'db_con' is database session
        self.db_con.commit()  # commit the transaction
        
        return {"message": "Restaurant saved successfully."}