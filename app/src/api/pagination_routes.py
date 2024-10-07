from flask import Blueprint, jsonify
from flask_restful import Resource, Api, reqparse

from .pagination.pagination import Pagination

pagination_bp = Blueprint('pagination', __name__)
api = Api(pagination_bp)

parser = reqparse.RequestParser()
parser.add_argument('page', type=int, default=1, help='Page number')
parser.add_argument('page_size', type=int, default=10, help='Number of items per page')

class PaginationResource(Resource):
    def get(self):
        args = parser.parse_args()
        pagination_input = {'page': args['page'], 'page_size': args['page_size']}
        pagination = Pagination(pagination_input)
        result = pagination.get_paginated_results()
        return jsonify(result)

api.add_resource(PaginationResource, '/api/search_results')