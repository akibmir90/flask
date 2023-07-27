from flask import Flask, render_template, request, jsonify
import os
from inference import generate_animation

app = Flask(__name__)

@app.route('/')
def home():
    img_list = get_available_images()
    return render_template('index.html', img_list=img_list)

def get_available_images():
    # Get a list of available image names from the source_image folder
    current_directory = os.path.dirname(os.path.abspath(__file__))
    source_image_folder = os.path.join(current_directory, 'examples', 'source_image')
    img_list = [img_name.split('.')[0] for img_name in os.listdir(source_image_folder) if img_name.endswith('.png')]
    return img_list

@app.route('/generate_animation', methods=['POST'])
def generate_animation_endpoint():
    if request.method == 'POST':
        image_name = request.form['image_name']
        audio_file = request.files['audio']

        if not image_name or not audio_file:
            return jsonify({'error': 'Please select both an image and an audio file.'})

        if image_name not in get_available_images():
            return jsonify({'error': 'Invalid image selected. Please choose from the available images.'})

        animation_url = generate_animation(image_name, audio_file)
        return jsonify({'animation_url': animation_url})

if __name__ == '__main__':
    app.run(debug=True)
