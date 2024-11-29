from flask import jsonify, Blueprint
from flask_restful import Resource, Api
from .restaurant.delete_saved_restaurant import DeleteSavedRestaurantLogic

delete_saved_restaurant_bp = Blueprint('delete_saved_restaurant', __name__)
api = Api(delete_saved_restaurant_bp)

class DeleteSavedRestaurant(Resource):
    def delete(self, userId, restaurantId):
        # Create an instance of the DeleteSavedRestaurantLogic class
        delete_restaurant_logic = DeleteSavedRestaurantLogic(user_id=userId, restaurant_id=restaurantId)
        
        # Call the method to delete the restaurant and get the response
        response, status_code = delete_restaurant_logic.delete_restaurant()

        return jsonify(response), status_code

api.add_resource(DeleteSavedRestaurant, '/api/saved-restaurants/<string:userId>/<string:restaurantId>')
