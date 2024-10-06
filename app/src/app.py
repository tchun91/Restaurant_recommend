from flask import Flask
from flask_cors import CORS
from api.routes import api
from api.recommender_routes import recommendation_bp
from api.chatbot_routes import chatbot_bp
app = Flask(__name__)
CORS(app) #To enbale for all domains on all routes
# Register the blueprint
app.register_blueprint(api)
app.register_blueprint(recommendation_bp)
app.register_blueprint(chatbot_bp)




@app.route('/')
def home():
    return "Welcome to the Food Recsys API."

if __name__ == '__main__':
    app.run(debug=True)

