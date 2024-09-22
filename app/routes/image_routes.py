from flask import Blueprint, request, jsonify, current_app
import os
from app.services.openai_service import get_openai_response
from app.utils.image_utils import save_image

image_bp = Blueprint('image_bp', __name__)

@image_bp.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    file = request.files['image']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    file_path = save_image(file, current_app.config['UPLOAD_FOLDER'])

    openai_response = get_openai_response(file_path)

    return jsonify({
        'message': 'Image uploaded successfully',
        'openai_response': openai_response
    }), 200
