from flask import Flask, render_template, jsonify
import os
import requests
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

def get_linkedin_data(endpoint):
    access_token = os.getenv('LINKEDIN_ACCESS_TOKEN')
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(endpoint, headers=headers)
    return response.json() if response.status_code == 200 else None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/linkedin')
def linkedin():
    try:
        profile = get_linkedin_data('https://api.linkedin.com/v2/userinfo')
        return jsonify({
            "profile": profile,
            "experience": []  # Keeping structure for potential future use
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)