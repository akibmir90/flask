from flask import Flask, render_template, request, jsonify
import os
from inference import generate_animation

app = Flask(__name__)

def get_available_images():
    # Get the absolute path of the current script's directory
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Get the absolute path of the 'SadTalker_Flask_App' directory
    app_directory = os.path.abspath(os.path.join(current_directory, os.pardir))

    # Get the absolute path of the 'examples/source_image' folder
    source_image_folder = os.path.join(app_directory, 'examples', 'source_image')

    # List all image names in the folder with .jpg extension
    img_list = [img_name.split('.')[0] for img_name in os.listdir(source_image_folder) if img_name.endswith('.jpg')]
    return img_list

@app.route('/')
def home():
    img_list = get_available_images()
    return render_template('index.html', img_list=img_list)

@app.route('/generate_animation', methods=['POST'])
def generate_animation_endpoint():
    if request.method == 'POST':
        image_name = request.form['image_name']
        audio_file = request.files['audio']

        if image_name and audio_file:
            animation_url = generate_animation(image_name, audio_file)
            return jsonify({'animation_url': animation_url})
        else:
            return jsonify({'error': 'Please select both an image and an audio file.'})

if __name__ == '__main__':
    app.run(debug=True)
