import os
import glob
from base64 import b64encode
from common import your_inference_function

def generate_animation(image_name, audio_file):
    # Assuming the audio file is saved in the 'driven_audio' folder
    audio_file.save(f'examples/driven_audio/{audio_file.filename}')

    img = f'examples/source_image/{image_name}.jpg'

    # Call the inference function directly instead of using subprocess.run()
    your_inference_function(audio_file.filename, img)

    results = sorted(os.listdir('./results/'))
    mp4_files = glob.glob('./results/*.mp4')

    if mp4_files:
        mp4_name = mp4_files[0]
        mp4 = open(f'{mp4_name}', 'rb').read()
        animation_url = "data:video/mp4;base64," + b64encode(mp4).decode()
        return animation_url
    else:
        return None
