import datetime

class ReviewProcessor:
    def __init__(self, user_id, restaurant_id, rating, review_text, reviews_data):
        self.user_id = user_id
        self.restaurant_id = restaurant_id
        self.rating = rating
        self.review_text = review_text
        self.reviews_data = reviews_data

    def validate_input(self):
        # Validate that all fields are present
        if not all([self.user_id, self.restaurant_id, self.rating, self.review_text]):
            return False, "All fields are required."

        # Validate that the rating is a number between 1 and 5
        if not isinstance(self.rating, (int, float)) or not (1 <= self.rating <= 5):
            return False, "Rating must be a number between 1 and 5."

        return True, None

    def check_existing_review(self):
        # Check if the user has already submitted a review for the restaurant
        for review in self.reviews_data:
            if review["userId"] == self.user_id and review["restaurantId"] == self.restaurant_id:
                return True  # Review already exists
        return False

    def save_review(self):
        # If no existing review, add the new one
        new_review = {
            "userId": self.user_id,
            "restaurantId": self.restaurant_id,
            "rating": self.rating,
            "reviewText": self.review_text
        }
        self.reviews_data.append(new_review)
        return new_review