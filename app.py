from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Initialize OpenAI client using environment variable
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.json.get('text', '')
    
    try:
        response = client.moderations.create(input=text)
        result = response.results[0]
        
        # Sort categories alphabetically and format scores
        scores = dict(sorted(result.category_scores.model_dump().items()))
        formatted_scores = {}
        for category, score in scores.items():
            if '/' not in category:  # Only show the underscore versions
                category_name = category.replace('_', ' ').title()
                if score is None:
                    score_str = "N/A"
                elif score < 0.01:
                    score_str = "≈ 0"
                else:
                    score_str = f"{score:.6f}"
                formatted_scores[category_name] = score_str
        
        return jsonify({
            'success': True,
            'flagged': result.flagged,
            'model': response.model,
            'id': response.id,
            'scores': formatted_scores
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    os.makedirs('templates', exist_ok=True)
    
    # Get port from environment variable or default to 5000
    port = int(os.environ.get('PORT', 5000))
    
    # In development, use debug mode and listen only on localhost
    # In production (like Docker), bind to all interfaces
    if os.environ.get('FLASK_ENV') == 'production':
        app.run(host='0.0.0.0', port=port)
    else:
        app.run(debug=True, port=port) 