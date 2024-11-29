from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Firebase credentials
FIREBASE_URL = "https://movement-iot-default-rtdb.firebaseio.com/randomNumber.json"
FIREBASE_SECRET = "i3xRb3mlEml6pKjwcp9mCnYeeLMHT4tqzXfgoEj9"

@app.route('/update', methods=['GET'])
def update():
    # Get the data from query string
    data = request.args.get('data')
    if not data:
        return jsonify({"error": "No data provided"}), 400

    # Send the data to Firebase
    firebase_payload = {"value": int(data)}
    firebase_url = f"{FIREBASE_URL}?auth={FIREBASE_SECRET}"
    
    try:
        response = requests.post(firebase_url, json=firebase_payload)
        if response.status_code == 200:
            return jsonify({"success": True, "firebase_response": response.json()})
        else:
            return jsonify({"success": False, "firebase_error": response.text}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
