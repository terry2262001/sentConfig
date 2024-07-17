from flask import Flask, request, jsonify
import time
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@app.route('/fcm_config', methods=['POST'])
def get_fcm_config():
    app.logger.info(f"Received request with data: {request.json}")
    
    start_time = time.time()
    
    if request.method != 'POST':
        return jsonify({"error": "Method not allowed"}), 405

    data = request.json
    token = data.get('token')
    if token != 'abc':
        return jsonify({"error": "Invalid or missing token"}), 401

    # Create a dictionary with the FCM report configuration
    fcm_config = {
        "remote": {
            "fcm_token_report_url": "https://example.com/fcm/report",
            "fcm_report_body_template": "{\"device_name\": \"##deviceName##\", \"fcm_device_token\": \"##token##\"}",
            "fcm_report_body_type": "application/json",
            "fcm_report_header_content_type": "application/json",
            "fcm_report_header_auth": "Bearer YOUR_AUTH_TOKEN",
            "pref_remote_fcm_report_method": "POST"
        },
        "reply": {
            "a":"value",
            "b":"value"
        }
    }
    
    end_time = time.time()
    app.logger.info(f"Request processed in {end_time - start_time} seconds")
    
    return jsonify(fcm_config)

@app.errorhandler(Exception)
def handle_exception(e):
    app.logger.error(f"An error occurred: {str(e)}")
    return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)