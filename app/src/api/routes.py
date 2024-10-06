from flask import Blueprint, jsonify, request
from datetime import datetime
from math import ceil

api_bp = Blueprint('api', __name__)

from . import dummy_restaurants

################ 1. Main Page ################
# 1-1. Trending Restaurants
@api_bp.route('/api/trending_restaurants', methods = ['GET'])
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

# 1-2. Trending Category
@api_bp.route('/api/trending_category', methods=['GET'])
def trending_category():
    zipcode = request.args.get('zipcode')
    
    #  Add logic to fetch trending categories based on zipcode
    # e.g. restaurants = db.query("SELECT * FROM restaurants WHERE zipcode = ?", zipcode)
    
    # Count occurrences of each cuisine type
    cuisine_count = {}
    for restaurant in dummy_restaurants:
        cuisine = restaurant['cuisine']
        cuisine_count[cuisine] = cuisine_count.get(cuisine, 0) + 1
    
    # Sort cuisines by count (descending) and name (ascending)
    trending = sorted(cuisine_count.items(), key=lambda x: (-x[1], x[0]))
    output = [{
        "name": cuisine, 
        "rank": index + 1
    } for index, (cuisine, count) in enumerate(trending)]
    
    return jsonify(output)

################ 3. Search Bar ################
# 3-1. Search Bar
@api_bp.route('/api/search', methods=['GET'])
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
@api_bp.route('/api/recommendations/content-based/<userId>', methods=['GET'])
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
@api_bp.route('/api/recommendations/collaborative/<userId>', methods=['GET'])
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

################ 4. Pagination ################
# 4-1. Pagination API
@api_bp.route('/api/search_results', methods=['GET'])
def search_results():
    # Get pagination parameters from the request
    page = int(request.args.get('page', 1))
    page_size = int(request.args.get('page_size', 10))

    # Need to replace with actual database query and optimize database query for large datasets
    all_results = dummy_restaurants
    
    # Calculate pagination values
    total_results = len(all_results)
    total_pages = ceil(total_results / page_size)
    
    # Ensure the requested page is within bounds
    if page < 1:
        page = 1
    elif page > total_pages:
        page = total_pages

    # Calculate start and end indices for slicing
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    # Slice the results for the current page
    paginated_results = all_results[start_index:end_index]

    # Can add implementing caching for frequently accessed pages
    
    response = {
        "total_results": total_results,
        "page": page,
        "page_size": page_size,
        "total_pages": total_pages,
        "results": paginated_results,
        "has_next": page < total_pages,
        "has_prev": page > 1
    }
    
    return jsonify(response)

################ 5. Restaurant Detail Page ################
# 5-3. General Info
@api_bp.route('/api/restaurants/<string:restaurant_id>', methods=['GET'])
def get_restaurant_info(restaurant_id):

    # Validation of restaurant_id
    if not restaurant_id:
        abort(400, description="Restaurant ID is required")

    # Find the restaurant in our dummy data
    restaurant = next((r for r in dummy_restaurants if r['id'] == restaurant_id), None)

    if not restaurant:
        abort(404, description=f"Restaurant with id {restaurant_id} not found")
    
    response = {
        "restaurantId": restaurant['id'],
        "name": restaurant['name'],
        "cuisine": restaurant['cuisine'],
        "location": restaurant['location'],
        "rating": restaurant['rating'],
        "priceRange": restaurant['price_range'],
        "thumbnail": restaurant['thumbnail']
    }
    
    return jsonify(response)
