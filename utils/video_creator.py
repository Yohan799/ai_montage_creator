
from moviepy.editor import *
from utils.caption_generator import generate_captions
import os
import uuid

def create_video_montage(image_paths, music_path, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    duration_per_image = 2

    # Generate captions
    captioned_images = generate_captions(image_paths)

    clips = []
    for path, caption in captioned_images:
        img_clip = ImageClip(path).set_duration(duration_per_image).resize(width=720)
        txt_clip = TextClip(caption, fontsize=28, color='white', font='Arial-Bold', bg_color='black', size=img_clip.size)
        txt_clip = txt_clip.set_duration(duration_per_image).set_position(('center', 'bottom'))

        clips.append(CompositeVideoClip([img_clip, txt_clip]))

    montage = concatenate_videoclips(clips, method="compose")

    if music_path:
        audio = AudioFileClip(music_path).set_duration(montage.duration)
        montage = montage.set_audio(audio)

    output_filename = f"montage_{uuid.uuid4().hex}.mp4"
    output_path = os.path.join(output_folder, output_filename)

    montage.write_videofile(output_path, fps=24, codec='libx264')
    return output_path
