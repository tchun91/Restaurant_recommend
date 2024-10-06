from flask import Flask, render_template_string, request, make_response, render_template, jsonify, Blueprint
from flask_restful import Resource, Api, reqparse, abort


from personalization.save_restaurant import save_restaurant

personalization_bp = Blueprint('personalization', __name__)
api = Api(personalization_bp)

parser = reqparse.RequestParser()
parser.add_argument('userId', type=str, required=False, help='User ID is required')
parser.add_argument('restaurantId', type=str, required=False, help='Restaurant ID is required')

class save_restaurant_user(Resource):
    def post(self):
        args = parser.parse_args()

        payload_input = {'userId':args['userId'],'restaurantId':args['restaurantId']}
        personal_restaurant_cl=save_restaurant(payload_input)

        pr_cl = personal_restaurant_cl(args['user_chat_input'])
        #Save log
        pr_cl.save_logging()
        #Save to service db
        pr_cl.save_restaurant()
        return None


api.add_resource(save_restaurant_user, '/api/saved_restaurant')
