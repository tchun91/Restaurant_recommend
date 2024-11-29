from flask import Blueprint, jsonify
from flask_restful import Resource, Api
from .recommendations.personalized_recommendations import PersonalizedRecommendations

personalized_recommendations_bp = Blueprint('personalized_recommendations', __name__)
api = Api(personalized_recommendations_bp)

class GetPersonalizedRecommendations(Resource):
    def get(self, userId):
        # Create an instance of the PersonalizedRecommendations class and fetch recommendations
        personalized_rec = PersonalizedRecommendations(user_id=userId)
        recommendations = personalized_rec.get_recommendations()

        return jsonify({"recommendations": recommendations})

api.add_resource(GetPersonalizedRecommendations, '/api/recommendations/<string:userId>')