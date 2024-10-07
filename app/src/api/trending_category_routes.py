from flask import Blueprint, jsonify
from flask_restful import Api, Resource, reqparse
from .trending_category.trending_category import TrendingCategory

trending_category_bp = Blueprint('trending_category', __name__)
api = Api(trending_category_bp)

class TrendingCategoryResource(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('zipcode', type=str, required=True, help='Zipcode is required')
        
        args = parser.parse_args()

        trending_category = TrendingCategory(args['zipcode'])
        result = trending_category.get_trending_categories()
        
        return jsonify(result)

api.add_resource(TrendingCategoryResource, '/api/trending_category')