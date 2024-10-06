from flask import Flask, render_template_string, request, make_response, render_template, jsonify, Blueprint
from flask_restful import Resource, Api,reqparse, abort
from .trending import TrendingRestaurants

trending_bp = Blueprint('trending', __name__)
api = Api(trending_bp)

parser = reqparse.RequestParser()
parser.add_argment('zipcode', type=str, required=True, help='zipcode is required')

class trending_restaurants(Resource):
    def get(self):
        args = parser.parse_args()
        payload_input = {'zipcode':args['zipcode']}
        trending = TrendingRestaurants(payload_input)

        return jsonify(trending.get_trending_restaurants())
    
api.add_resource(trending_restaurants, '/api/trending_restaurants')
    


