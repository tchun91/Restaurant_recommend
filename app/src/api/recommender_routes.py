from flask import Flask, render_template_string, request, make_response, render_template, jsonify, Blueprint
from flask_restful import Resource, Api,reqparse, abort



from .recommender.menu_recommender import recom_menu
from .recommender.content_based_recommender import content_based_recommendations
from .recommender.collaborative_recommender import collaborative_recommendations

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

# 3-2. You may also like
content_based_bp = Blueprint('content_baesd', __name__)
api = Api(content_based_bp)

parser = reqparse.ReQuestParser()
parser.add_argument('userId', type=str, required=True, help='User ID is required')

class content_recom(Resource):
    def get(self):
        args = parser.parse_args()
        payload_input = {'userId':args['userId']}
        content_based_recom = content_based_recommendations(payload_input)

        return jsonify(content_based_recom.recommend())

# 3-3. Others also like 
collaborative_based_bp = Blueprint('collaborative_based', __name__)
api = Api(collaborative_based_bp)

parser = reqparse.ReQuestParser()
parser.add_argument('userId', type=str, required=True, help='User ID is required')

class collaborative_recom(Resource):
    def get(self):
        args = parser.parse_args()
        payload_input = {'userId':args['userId']}
        collaborative_based_recom = collaborative_recommendations(payload_input)

        return jsonify(collaborative_based_recom.recommend())