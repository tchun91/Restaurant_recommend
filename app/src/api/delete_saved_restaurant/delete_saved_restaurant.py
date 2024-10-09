class DeleteSavedRestaurantLogic:
    def __init__(self, user_id, restaurant_id, db_con):
        self.user_id = user_id
        self.restaurant_id = restaurant_id
        self.db_con = db_con  

    def delete_restaurant(self):
        # query to find the saved restaurant by user_id and restaurant_id
        restaurant_to_delete = (
            self.db_con.query(Restaurant)
            .filter(Restaurant.user_id == self.user_id)
            .filter(Restaurant.restaurant_id == self.restaurant_id)
            .first()  # fetch the first matching record
        )

        if restaurant_to_delete:
            self.db_con.delete(restaurant_to_delete)  # delete the restaurant
            self.db_con.commit()  # commit the transaction
            return {"message": "Restaurant removed successfully."}, 200
        else:
            return {"message": "Restaurant not found."}, 404
