from flask import Flask, render_template, request, jsonify
from inference import generate_animation
from common import your_inference_function

app = Flask(__name__)

@app.route('/')
def home():
    img_list = ['boy.jpg', 'girl.jpg']  # List of available image names, you need to add the actual names
    return render_template('index.html', img_list=img_list)

@app.route('/generate_animation', methods=['POST'])
def generate_animation_endpoint():
    if request.method == 'POST':
        image_name = request.form['image_name']
        audio_file = request.files['audio']
        animation_url = generate_animation(image_name, audio_file)
        return jsonify({'animation_url': animation_url})

if __name__ == '__main__':
    app.run(debug=True)
