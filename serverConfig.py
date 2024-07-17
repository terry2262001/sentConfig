from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/fcm_config', methods=['POST'])
def get_fcm_config():
    # Check if the token is provided and correct
    data = request.json
    token = data.get('token')
    if token != 'abc':
        return jsonify({"error": "Invalid or missing token"}), 401

    # Create a dictionary with the FCM report configuration
    fcm_config = {
        "fcm_token_report_url": "https://example.com/fcm/report",
        "fcm_report_body_template": "{\"token\": \"$TOKEN\", \"app\": \"$PACKAGE\"}",
        "fcm_report_body_type": "application/json",
        "fcm_report_header_content_type": "application/json",
        "fcm_report_header_auth": "Bearer YOUR_AUTH_TOKEN",
        "pref_remote_fcm_report_method": "POST"
    }

    return jsonify(fcm_config)

if __name__ == '__main__':
    app.run(debug=True)