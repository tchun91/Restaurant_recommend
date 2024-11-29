from flask import Flask, jsonify, Blueprint, request
from flask_restful import Resource, Api, reqparse
from .reviews.review import ReviewProcessor

reviews_bp = Blueprint('reviews', __name__)
api = Api(reviews_bp)

# Mocked database for reviews (can be replaced by a real database)
reviews_data = []

parser = reqparse.RequestParser()
parser.add_argument('userId', type=str, required=True, help='User ID is required')
parser.add_argument('restaurantId', type=str, required=True, help='Restaurant ID is required')
parser.add_argument('rating', type=float, required=True, help='Rating must be a number between 1 and 5.')
parser.add_argument('reviewText', type=str, required=True, help='Review text is required')

class WriteReview(Resource):
    def post(self):
        args = parser.parse_args()

        # Create the review processor
        review_processor = ReviewProcessor(
            user_id=args['userId'],
            restaurant_id=args['restaurantId'],
            rating=args['rating'],
            review_text=args['reviewText'],
            reviews_data=reviews_data
        )

        # Validate the input
        is_valid, error_message = review_processor.validate_input()
        if not is_valid:
            return jsonify({"message": error_message}), 400

        # Check if the user has already submitted a review for this restaurant
        if review_processor.check_existing_review():
            return jsonify({"message": "User has already submitted a review for this restaurant."}), 400

        # Save the new review
        new_review = review_processor.save_review()
        return jsonify({
            "message": "Review submitted successfully.",
            "review": new_review
        })

api.add_resource(WriteReview, '/api/reviews')