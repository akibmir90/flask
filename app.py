from flask import Flask, render_template, request, jsonify
import os
from inference import generate_animation

app = Flask(__name__)

@app.route('/')
def home():
    img_list = ['boy.jpg', 'girl.jpg', 'landscape.jpg']  # Add actual image names here
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
