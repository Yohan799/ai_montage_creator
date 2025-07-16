from flask import Flask, render_template, request
import os
from utils.image_ranker import rank_images_by_prompt
from utils.music_selector import select_music_by_mood
from utils.video_creator import create_video_montage

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "static/output"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.form['prompt']
    files = request.files.getlist('images')

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    image_paths = []
    for file in files:
        path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(path)
        image_paths.append(path)

    selected_images = rank_images_by_prompt(image_paths, prompt)
    music_path = select_music_by_mood(prompt)
    video_path = create_video_montage(selected_images, music_path, OUTPUT_FOLDER)

    # Convert file system path to URL
    video_url = video_path.replace("\\", "/").replace("static/", "")


    return render_template('index.html', video_url=video_url)

if __name__ == '__main__':
    app.run(debug=True)
