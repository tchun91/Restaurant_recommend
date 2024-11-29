from flask import Blueprint, jsonify
from flask_restful import Resource, Api, reqparse
from .restaurants.saved_restaurants import SavedRestaurants

saved_restaurants_bp = Blueprint('saved_restaurants', __name__)
api = Api(saved_restaurants_bp)

parser = reqparse.RequestParser()
parser.add_argument('isBookmarked', type=bool, required=False, help="Filter by bookmarked restaurants")

class GetSavedRestaurants(Resource):
    def get(self, userId):
        args = parser.parse_args()
        is_bookmarked = args.get('isBookmarked', None)

        # Create an instance of the SavedRestaurants class and fetch saved restaurants
        saved_restaurants = SavedRestaurants(user_id=userId, is_bookmarked=is_bookmarked)
        restaurants = saved_restaurants.get_saved_restaurants()

        return jsonify({"savedRestaurants": restaurants})

api.add_resource(GetSavedRestaurants, '/api/saved-restaurants/<string:userId>')