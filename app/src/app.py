from flask import Flask
from flask_cors import CORS
from api.routes import api

app = Flask(__name__)
CORS(app) #To enbale for all domains on all routes
app.register_blueprint(api)

@app.route('/')
def home():
    return "Welcome to the Food Recsys API."

if __name__ == '__main__':
    app.run(debug=True)

