from flask import Flask, render_template, request, jsonify, redirect, url_for
from inference import generate_animation
from common import your_inference_function

app = Flask(__name__)

@app.route('/')
def home():
    img_list = ['boy', ...]  # List of available image names, you need to add the actual names
    return render_template('index.html', img_list=img_list)

@app.route('/generate_animation', methods=['POST'])
def generate_animation_endpoint():
    if request.method == 'POST':
        image_name = request.form['image_name']
        audio_file = request.files['audio']
        animation_url = generate_animation(image_name, audio_file)
        if animation_url:
            return redirect(url_for('show_animation', animation_url=animation_url))
        else:
            return jsonify({'animation_url': None})

@app.route('/animation')
def show_animation():
    animation_url = request.args.get('animation_url')
    return render_template('animation.html', animation_url=animation_url)

if __name__ == '__main__':
    app.run(debug=True)
