from flask import Flask
from flask_cors import CORS
from api.routes import api_bp
from api.recommender_routes import recommendation_bp
from api.chatbot_routes import chatbot_bp
from api.personalization_routes import personalization_bp
from api.trending_routes import trending_bp
app = Flask(__name__)
CORS(app) #To enbale for all domains on all routes
# Register the blueprint
app.register_blueprint(api_bp)
app.register_blueprint(recommendation_bp)
app.register_blueprint(chatbot_bp)
app.register_blueprint(personalization_bp)
app.register_blueprint(trending_bp)




@app.route('/')
def home():
    return "Welcome to the Food Recsys API."

if __name__ == '__main__':
    app.run(debug=True)

