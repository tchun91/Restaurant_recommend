from flask import Flask, render_template_string, request, make_response, render_template, jsonify, Blueprint
from flask_restful import Resource, Api,reqparse, abort



from .recommender.menu_recommender import recom_menu

recommendation_bp = Blueprint('recommendation', __name__)
api = Api(recommendation_bp)

parser = reqparse.RequestParser()
parser.add_argument('userId', type=str, required=True, help='User ID is required')
parser.add_argument('restaurantId', type=str, required=True, help='Restaurant ID is required')




class menu_recom(Resource):
    def get(self):

        args = parser.parse_args()
        payload_input = {'userId':args['userId'],'restaurantId':args['restaurantId']}
        recom_menu_cl=recom_menu(payload_input)

        return jsonify(recom_menu_cl.recommend())

api.add_resource(menu_recom,'/api/recommendations')
