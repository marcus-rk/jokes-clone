from flask import Flask, jsonify #
import random
from jokes_data import jokes

app = Flask(__name__)

@app.route('/', methods=['GET'])
def root():
    return jsonify({
        "service": "Joke Service",
        "version": "1.0.0",
        "description": "A RESTful API service that provides jokes",
        "documentation": "/api",
       "health": "/health"
    })

@app.route('/api', methods=['GET'])
def api_documentation():
    return jsonify({
        "endpoints": [
            {
                "path": "/",
                "method": "GET",
                "description": "Service information and available endpoints",
                "response": "JSON object with service details"
            },
            {
                "path": "/api",
                "method": "GET",
                "description": "API documentation with all available endpoints",
                "response": "JSON object with endpoint details"
            },
            {
                "path": "/api/jokes",
                "method": "GET",
                "description": "Get all available jokes",
                "response": "Array of joke objects"
            },
            {
                "path": "/api/jokes/random",
                "method": "GET",
                "description": "Get a random joke",
                "response": "Single joke object"
            },
            {
                "path": "/api/jokes/<id>",
                "method": "GET",
                "description": "Get a specific joke by ID",
                "response": "Single joke object or 404 error"
            },
            {
                "path": "/health",
                "method": "GET",
                "description": "Health check endpoint",
                "response": "JSON object with service health status"
            }
        ]
    })

@app.route('/api/jokes', methods=['GET'])
def get_all_jokes():
    return jsonify(jokes)

@app.route('/api/jokes/random', methods=['GET'])
def get_random_joke():
    return jsonify(random.choice(jokes))

@app.route('/api/jokes/<int:joke_id>', methods=['GET'])
def get_joke_by_id(joke_id):
    joke = next((joke for joke in jokes if joke['id'] == joke_id), None)
    if joke is None:
        return jsonify({"error": "Joke not found"}), 404
    return jsonify(joke)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run()
    
