from flask import Blueprint, jsonify, request
from datetime import datetime

api = Blueprint('api', __name__)

dummy_restaurants = [
    {
        "id": "1",
        "name": "Pasta Paradise",
        "cuisine": "Italian",
        "location": "123 Main St, Springfield",
        "rating": 4.5,
        "price_range": "$$",
        "thumbnail": "https://example.com/thumbnails/pasta_paradise.jpg",
        "similarity_score": 0.9  
    },
    {
        "id": "2",
        "name": "Taco Town",
        "cuisine": "Mexican",
        "location": "456 Elm St, Springfield",
        "rating": 4.2,
        "price_range": "$",
        "thumbnail": "https://example.com/thumbnails/taco_town.jpg",
        "similarity_score": 0.85  
    },
    {
        "id": "3",
        "name": "Chow Mein Palace",
        "cuisine": "Chinese",
        "location": "789 Pine St, Springfield",
        "rating": 4.0,
        "price_range": "$",
        "thumbnail": "https://example.com/thumbnails/chow_mein_palace.jpg",
        "similarity_score": 0.8  
    },
    {
        "id": "4",
        "name": "Sushi Heaven",
        "cuisine": "Japanese",
        "location": "321 Oak St, Springfield",
        "rating": 4.7,
        "price_range": "$$$",
        "thumbnail": "https://example.com/thumbnails/sushi_heaven.jpg",
        "similarity_score": 0.75  
    },
    {
        "id": "5",
        "name": "Vegan Delight",
        "cuisine": "Vegan",
        "location": "654 Maple St, Springfield",
        "rating": 4.3,
        "price_range": "$$",
        "thumbnail": "https://example.com/thumbnails/vegan_delight.jpg",
        "similarity_score": 0.7  
    },
    {
        "id": "6",
        "name": "BBQ Nation",
        "cuisine": "Barbecue",
        "location": "987 Cedar St, Springfield",
        "rating": 4.6,
        "price_range": "$$",
        "thumbnail": "https://example.com/thumbnails/bbq_nation.jpg",
        "similarity_score": 0.65  
    },
    {
        "id": "7",
        "name": "Bakery Bliss",
        "cuisine": "Bakery",
        "location": "135 Walnut St, Springfield",
        "rating": 4.8,
        "price_range": "$",
        "thumbnail": "https://example.com/thumbnails/bakery_bliss.jpg",
        "similarity_score": 0.6  
    },
    {
        "id": "8",
        "name": "Burger Joint",
        "cuisine": "American",
        "location": "246 Birch St, Springfield",
        "rating": 4.4,
        "price_range": "$$",
        "thumbnail": "https://example.com/thumbnails/burger_joint.jpg",
        "similarity_score": 0.55  
    },
    {
        "id": "9",
        "name": "Curry Corner",
        "cuisine": "Indian",
        "location": "357 Spruce St, Springfield",
        "rating": 4.5,
        "price_range": "$",
        "thumbnail": "https://example.com/thumbnails/curry_corner.jpg",
        "similarity_score": 0.5  
    },
    {
        "id": "10",
        "name": "Pizzeria Uno",
        "cuisine": "Italian",
        "location": "468 Cherry St, Springfield",
        "rating": 4.9,
        "price_range": "$$",
        "thumbnail": "https://example.com/thumbnails/pizzeria_uno.jpg",
        "similarity_score": 0.95  
    }
]

################ 1. Main Page ################
# 1-1. Trending Restaurants
@api.route('/api/trending_restaurants', methods = ['GET'])
def trending_restaurants():
    zipcode = request.args.get('zipcode')
    
    # Add logic to fetch trending restaurants here
    
    # Sort the trending restaurants by rating desc and id asc
    trending = sorted(dummy_restaurants, key=lambda x: (-x['rating'], x['id']))
    output = [{
        "name": restaurant["name"], 
        "avg_review": restaurant["rating"],
        "rank": index + 1} for index, restaurant in enumerate(trending)]

    return jsonify(output)

################ 3. Search Bar ################
# 3-1. Search Bar
@api.route('/api/search', methods=['GET'])
def search():
    user_id = request.args.get('userId')  # User Id input
    query = request.args.get('query') # Search input
    filters = request.args.get('filters') # Filter information input

    # Add logic to fetch search results here
    filtered_results = [restaurant for restaurant in dummy_restaurants if query.lower() in restaurant['name'].lower()]

    # Data Preprocessing steps
    output = {
        "searchResults": [
            {
                "restaurantId": restaurant["id"],
                "name": restaurant["name"],
                "cuisine": restaurant["cuisine"],
                "location": restaurant["location"],
                "rating": restaurant["rating"],
                "PriceRange": restaurant["price_range"],
                "Thumbnail": restaurant["thumbnail"]
            }
            for restaurant in filtered_results
        ],
        "RecentSearches": [
            {"SearchTerm": query, "timestamp": datetime.now().isoformat()} 
        ]       
    }

    return jsonify(output)

# 3-2. You may also like
@api.route('/api/recommendations/content-based/<userId>', methods=['GET'])
def content_based_recommendations(userId):
    # Add logic to fetch recommended restaurants here
    # Calculate similarity scores 

    recommendations = dummy_restaurants[1:3]

    # Data Preprocessing steps
    output = {
        "recommendations": [
            {
                "restaurantId": restaurant["id"],
                "name": restaurant["name"],
                "cuisine": restaurant["cuisine"],
                "location": restaurant["location"],
                "rating": restaurant["rating"],
                "pricerange": restaurant["price_range"],
                "similarity_score": restaurant["similarity_score"],
                "thumbnail": restaurant["thumbnail"]
            }
            for restaurant in recommendations
        ]
    }

    return jsonify(output)

# 3-3. Others also liked
@api.route('/api/recommendations/collaborative/<userId>', methods=['GET'])
def collaborative_recommendations(userId):
    # Add logic to fetch recommended restaurants here
    # Calculate similarity scores 

    recommendations = dummy_restaurants[1:3]

    # Data Preprocessing steps
    output = {
        "recommendations": [
            {
                "restaurantId": restaurant["id"],
                "name": restaurant["name"],
                "cuisine": restaurant["cuisine"],
                "location": restaurant["location"],
                "rating": restaurant["rating"],
                "pricerange": restaurant["price_range"],
                "similarity_score": restaurant["similarity_score"],
                "thumbnail": restaurant["thumbnail"]
            }
            for restaurant in recommendations
        ]
    }

    return jsonify(output)
