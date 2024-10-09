from flask import Flask
from flask_cors import CORS
from api.routes import api_bp
from api.recommender_routes import recommendation_bp
from api.chatbot_routes import chatbot_bp
from api.personalization_routes import personalization_bp
from api.trending_routes import trending_bp
from api.recommender_routes import collaborative_based_bp
from api.recommender_routes import content_based_bp
from api.search_routes import search_bar_bp
app = Flask(__name__)
CORS(app) #To enbale for all domains on all routes
# Register the blueprint

# 1-1
app.register_blueprint(trending_bp)

# 1-2
app.register_blueprint(trending_category_bp)

# 3-1
app.register_blueprint(search_bar_bp)
# 3-2
app.register_blueprint(content_based_bp)
# 3-3
app.register_blueprint(collaborative_based_bp)

# 4-1
app.register_blueprint(pagination_bp)

# 5-1
app.register_blueprint(reviews_bp)

# 5-3
app.register_blueprint(restaurant_info_bp)

app.register_blueprint(api_bp)
app.register_blueprint(recommendation_bp)
app.register_blueprint(chatbot_bp)
app.register_blueprint(personalization_bp)

# 6-2 
app.register_blueprint(saved_restaurants_bp)
#6-4
app.register_blueprint(personalized_recommendations_bp)
#6-5
app.register_blueprint(delete_saved_restaurant_bp)

@app.route('/')
def home():
    return "Welcome to the Food Recsys API."

if __name__ == '__main__':
    app.run(debug=True)
