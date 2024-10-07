from flask import Blueprint, jsonify, abort
from flask_restful import Resource, Api, reqparse

from .restaurant_info.restaurant_info import RestaurantInfo

restaurant_info_bp = Blueprint('restaurant_info', __name__)
api = Api(restaurant_info_bp)

parser = reqparse.RequestParser()
parser.add_argument('restaurant_id', type=str, required=True, help='Restaurant ID is required')

class RestaurantInfoResource(Resource):
    def get(self):
        args = parser.parse_args()
        
        restaurant_input = {'restaurant_id': args['restaurant_id']}
        restaurant_info = RestaurantInfo(restaurant_input)
        result = restaurant_info.get_restaurant_info()
        
        return jsonify(result)

api.add_resource(RestaurantInfoResource, '/api/restaurants')