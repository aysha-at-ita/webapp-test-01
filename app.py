import os
import json
import requests
from flask import Flask, request, jsonify
import pymysql
from datetime import datetime

# app = Flask("wix-webhook-handler")
app = Flask(__name__)

# def get_db_connection():
#     return pymysql.connect(
#         host='https://db-mysql-nyc3-52064-do-user-29460921-0.i.db.ondigitalocean.com',
#         user=os.environ.get('DB_USER'),
#         password=os.environ.get('DB_PASSWORD'),
#         database=os.environ.get('DB_NAME'),
#         port=25060,
#         ssl={'require': True}
    # )

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    # Get form data from Zapier
    webhook_data = request.get_json()
    print(f"Received webhook: {webhook_data}")
    
    # Extract form information
    # contact_name = webhook_data.get('contact_first_name', '')
    # form_data = webhook_data.get('form_data', {})
    # payload_type = webhook_data.get('payload_type', '')
    # wrap_in_array = webhook_data.get('wrap_in_array', '')
    # unflatten = webhook_data.get('unflatten', '')
    # url = webhook_data.get('url', '')
    # data = webhook_data.get('data', {})
    # headers = webhook_data.get('headers', {})
    # timestamp = datetime.now()
    
    # Connect to database
    # connection = get_db_connection()
    # cursor = connection.cursor()
    
    # Example: Insert form submission
    # insert_query = """
    # INSERT INTO form_submissions (contact_name, form_data, submission_date)
    # VALUES (%s, %s, %s)
    # """
    # insert_query = """
    # INSERT INTO form_submissions (payload_type, wrap_in_array, unflatten, url, data, headers)
    # VALUES (%s, %s, %s, %s, %s, %s)
    # """
    # # cursor.execute(insert_query, (contact_name, json.dumps(form_data), timestamp))
    # cursor.execute(insert_query, payload_type, wrap_in_array, unflatten, url, json.dumps(data), json.dumps(headers))
    
    # # Handle file uploads if present
    # if 'file_uploads' in webhook_data:
    #     for file_info in webhook_data['file_uploads']:
    #         # Download and save files to your DigitalOcean Volume
    #         download_file_to_volume(file_info)
    
    # connection.commit()
    # cursor.close()
    # connection.close()
    
    return jsonify({"status": "success", "message": "Webhook processed"}), 200
    
    # except Exception as e:
    #     print(f"Error processing webhook: {str(e)}")
    #     return jsonify({"status": "error", "message": str(e)}), 500

# def download_file_to_volume(file_info):
#     """Download file and save to DigitalOcean Volume"""

#     # Assuming your volume is mounted at /mnt/volume
#     volume_path = "/mnt/volume/uploads/"
#     os.makedirs(volume_path, exist_ok=True)
    
#     file_url = file_info.get('url')
#     filename = file_info.get('filename', 'upload.file')
    
#     # Download file
#     response = requests.get(file_url)
#     if response.status_code == 200:
#         filepath = os.path.join(volume_path, filename)
#         with open(filepath, 'wb') as f:
#             f.write(response.content)
#         print(f"File saved: {filepath}")
    
# except Exception as e:
#     print(f"Error downloading file: {str(e)}")

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

app.run(host='0.0.0.0', port=5001, debug=True)
