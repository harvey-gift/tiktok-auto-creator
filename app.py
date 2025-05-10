from flask import Flask, request, jsonify
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
import os

app = Flask(__name__)

@app.route("/generate", methods=["POST"])
def generate():
    base_clip = VideoFileClip("stock/clip.mp4").subclip(0, 5)
    text_overlay = TextClip("Hot Trend!", fontsize=70, color='white')
    text_overlay = text_overlay.set_position('center').set_duration(5)

    final = CompositeVideoClip([base_clip, text_overlay])
    sound = "sounds/sound1.mp3"
    final = final.set_audio(VideoFileClip(sound).audio)

    output_path = "static/generated_video.mp4"
    final.write_videofile(output_path, fps=24)

    return jsonify({"status": "success", "video_url": f"/{output_path}"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
