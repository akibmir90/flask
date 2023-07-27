import glob
import os
import subprocess
from base64 import b64encode
import sys

def generate_animation(image_name, audio_file):
    # Get the absolute path of the current script's directory
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Create the 'driven_audio' folder if it doesn't exist
    driven_audio_folder = os.path.join(current_directory, 'examples', 'driven_audio')
    os.makedirs(driven_audio_folder, exist_ok=True)

    # Save the audio file to the 'driven_audio' folder
    audio_file_path = os.path.join(driven_audio_folder, audio_file.filename)
    audio_file.save(audio_file_path)

    # Get the absolute path of the image
    img_path = os.path.join(current_directory, 'examples', 'source_image', f'{image_name}.png')

    # Specify the command to run based on the Python interpreter in the environment
    python_interpreter = sys.executable
    command = [
        python_interpreter, 'inference.py', '--driven_audio', audio_file_path,
        '--source_image', img_path, '--result_dir', os.path.join(current_directory, 'results'),
        '--still', '--preprocess', 'full', '--enhancer', 'gfpgan'
    ]

    # Create the 'results' folder if it doesn't exist
    results_folder = os.path.join(current_directory, 'results')
    os.makedirs(results_folder, exist_ok=True)

    # Run the inference command
    subprocess.run(command)

    # Get the generated animation
    results = sorted(os.listdir(results_folder))
    mp4_files = glob.glob(os.path.join(results_folder, '*.mp4'))
    if not mp4_files:
        raise ValueError('No animation files were generated.')

    mp4_name = mp4_files[0]
    # Get the base64 encoded video data
    mp4 = open(mp4_name, 'rb').read()
    animation_url = "data:video/mp4;base64," + b64encode(mp4).decode()

    return animation_url
