# app.py

from flask import Flask, render_template, request, jsonify, url_for
from inference import generate_animation
from common import your_inference_function

app = Flask(__name__)

@app.route('/')
def home():
    img_list = ['boy', '...']  # List of available image names, you need to add the actual names
    return render_template('index.html', img_list=img_list)

@app.route('/generate_animation', methods=['POST'])
def generate_animation_endpoint():
    if request.method == 'POST':
        image_name = request.form['image_name']
        audio_file = request.files['audio']
        animation_path = generate_animation(image_name, audio_file)
        return jsonify({'animation_url': url_for('animation_result', filename=animation_path)})

@app.route('/animation_result/<filename>')
def animation_result(filename):
    return render_template('animation.html', animation_url=url_for('static', filename=filename))

if __name__ == '__main__':
    app.run(debug=True)
