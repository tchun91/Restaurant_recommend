from flask import Flask, render_template_string, request, make_response, render_template, jsonify, Blueprint
from flask_restful import Resource, Api,reqparse, abort

from .search import Search

search_bar_bp = Blueprint('search', __name__)
api = Api(search_bar_bp)

parser = reqparse.RequestParser()
parser.add_argument('userID', type=str, required=True, help='User ID is required')
parser.add_argument('query', type=str, required=True, help='Query is required')
parser.add_argument('filters', type=dict, required=False, help='Filters for the search')

parser.add_argument('filters[price-tier]', type=str, required=False, help='Price tier is optional')
parser.add_argument('filters[category]', type=str, required=False, help='Category is optional')

# 3-1 Search Bar
class search(Resource):
    def get(self):
        args = parser.parse_args()
        payload_input = {'userId': args['userID'],'query': args['query'],
            'filters': {
                'price-tier': args['filters']['price-tier'] if args['filters'] else None,
                'category': args['filters']['category'] if args['filters'] else None,
            }
        }
        search = Search(payload_input)

        return jsonify(search.search_bar_result())
    
api.add_resource(search, '/api/search')