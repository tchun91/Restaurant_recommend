from flask import Flask, render_template_string, request, make_response, render_template, jsonify, Blueprint
from flask_restful import Resource, Api,reqparse, abort



from .chatbot.user_chatbot import llm_m

chatbot_bp = Blueprint('chatbot', __name__)
api = Api(chatbot_bp)

parser = reqparse.RequestParser()
parser.add_argument('user_chat_input', type=str, required=True, help='user_chat_input is required')





class user_chatbot(Resource):
    def get(self):

        args = parser.parse_args()

        llm_chatbot=llm_m(args['user_chat_input'])

        output = {'model_response' : llm_chatbot.get_response()}
        return jsonify(output)

api.add_resource(user_chatbot,'/api/user_chatbot')
