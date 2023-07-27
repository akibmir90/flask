# inference.py

import glob
import os
from base64 import b64encode
from common import your_inference_function

def generate_animation(image_name, audio_file):
    # Assuming the audio file is saved in the 'driven_audio' folder
    audio_file.save(f'examples/driven_audio/{audio_file.filename}')

    img = f'examples/source_image/{image_name}.jpg'

    # Call the inference function directly instead of using subprocess.run()
    animation_path = your_inference_function(audio_file.filename, img)

    # Check if the animation was generated successfully
    if animation_path:
        # Animation was generated, read the video file and encode it
        mp4 = open(animation_path, 'rb').read()
        animation_url = "data:video/mp4;base64," + b64encode(mp4).decode()
        return animation_url
    else:
        # Animation was not generated successfully
        return None
