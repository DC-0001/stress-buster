from flask import Flask, request, jsonify, render_template 
from mira_sdk import MiraClient
from image_fetch import fetch_calming_images
from sound_player import play_random_sound

app = Flask(__name__)

# Initialize Mira Client
client = MiraClient(config={"API_KEY": "sb-c95bfa51f34759b65fd6a11f2a8be1e7"})

@app.route('/')
def main_page():
    return render_template('index.html', message={} )

@app.route('/test')
def test_page():
    return jsonify({"a":2})

@app.route('/run-therapy', methods=['POST'])
def run_therapy():
    data = request.get_json()
    user_input = data['user_input']
    print(user_input)
    # Prepare test input for flow
    test_input = {
        "user_input": user_input
    }

    try:
        # Run first flow (mood tracking)
        response = client.flow.execute('@dc-0001/stress-buster', test_input)
        print("returing response")
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/submit-feedback', methods=['POST'])
def submit_feedback():
    data = request.get_json()
    therapy_feedback = data['therapy_feedback']
    
    # Prepare input for second flow
    input_data = {
        "therapy_steps": "example steps from the previous flow",  # Replace with actual result
        "therapy_feedback": therapy_feedback
    }

    try:
        # Run second flow (personalization)
        result = client.flow.execute('@dc-0001/therapy-personalisation', input_data)
        
        # Fetch calming images
        images = fetch_calming_images()

        return jsonify({
            "finalResult": result,
            "images": images
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
