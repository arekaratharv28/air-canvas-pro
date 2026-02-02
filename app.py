from flask import Flask, render_template, request, jsonify, send_from_directory
import base64
import os
from datetime import datetime

app = Flask(__name__)

# Configuration
SAVE_FOLDER = 'captured_art'
if not os.path.exists(SAVE_FOLDER):
    os.makedirs(SAVE_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    try:
        data = request.json
        image_data = data['image'].replace('data:image/png;base64,', '')
        image_bytes = base64.b64decode(image_data)
        
        # Save with timestamp
        filename = f"art_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        filepath = os.path.join(SAVE_FOLDER, filename)
        
        with open(filepath, 'wb') as f:
            f.write(image_bytes)
            
        return jsonify({"message": "Securely Archived", "filename": filename})
    except Exception as e:
        return jsonify({"message": f"Error: {str(e)}"}), 500

# API to get list of images
@app.route('/gallery')
def get_gallery():
    files = sorted(os.listdir(SAVE_FOLDER), reverse=True) # Newest first
    return jsonify(files)

# Route to serve the actual image files
@app.route('/art/<filename>')
def serve_art(filename):
    return send_from_directory(SAVE_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True, port=5000)