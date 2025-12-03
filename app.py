from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# The data source URL from the assignment
SOURCE_URL = "https://november7-730026606190.europe-west1.run.app/messages"

# We will store the data here so it is instant to access
DATA_CACHE = []

def fetch_data():
    """Downloads the data once when the app starts."""
    global DATA_CACHE
    print("Downloading data... please wait.")
    try:
        response = requests.get(SOURCE_URL)
        if response.status_code == 200:
            DATA_CACHE = response.json()
            print(f"Success! Loaded {len(DATA_CACHE)} messages.")
        else:
            print(f"Failed to load data. Status Code: {response.status_code}")
    except Exception as e:
        print(f"Error fetching data: {e}")

# Call this immediately so data is ready before the first search
fetch_data()

@app.route('/search', methods=['GET'])
def search():
    # 1. Get query parameters
    query = request.args.get('q', '').lower()
    page = int(request.args.get('page', 1))   # Default to page 1
    limit = int(request.args.get('limit', 5)) # Default to 5 items per page

    if not query:
        return jsonify({"error": "Please provide a query, e.g., /search?q=hello"}), 400

    # 2. Filter the data
    all_matches = [
        msg for msg in DATA_CACHE 
        if query in msg.lower()
    ]

    # 3. Apply Pagination (Slice the list)
    start_index = (page - 1) * limit
    end_index = start_index + limit
    page_results = all_matches[start_index:end_index]

    # 4. Return the results with metadata (helpful for the frontend)
    return jsonify({
        "results": page_results,
        "page": page,
        "limit": limit,
        "total_matches": len(all_matches)
    })

if __name__ == '__main__':
    app.run(debug=True)