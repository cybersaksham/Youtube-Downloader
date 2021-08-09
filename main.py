from flask import Flask, render_template, request, jsonify, send_file, session
from pytube import YouTube
from io import BytesIO
from tempfile import TemporaryDirectory
import logging
import sys
import json

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

with open("config.json") as f:
    data = json.load(f)

app = Flask(__name__)
app.config["SECRET_KEY"] = data["SECRET_KEY"]


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/get_types', methods=["POST"])
def get_types():
    # Getting Types of video based on entered url
    if request.method == "POST":
        try:
            # Collecting data from form
            url__ = request.form["urlInput"]
            yt = YouTube(url__)
            videos = list(yt.streams.filter(progressive=True))
            session["url"] = url__
            return jsonify(error=None, types=[str(video.resolution) for video in videos])
        except:
            return jsonify(error="Some Error Occurred", types=None)


@app.route('/download', methods=["POST"])
def download():
    # Downloading Video
    if request.method == "POST":
        if "url" in session:
            try:
                url__ = session["url"]
                res__ = request.form["resolution"]

                with TemporaryDirectory() as tmp_dir:
                    print(tmp_dir)
                    download_path = YouTube(url__).streams.filter(res=res__, progressive=True) \
                        .first().download(tmp_dir)
                    vid_name = download_path.split("\\")[-1]
                    with open(download_path, "rb") as f1:
                        file_bytes = f1.read()

                    return send_file(BytesIO(file_bytes), attachment_filename=vid_name, as_attachment=True)
            except:
                logging.exception('Failed download')
                return 'Video download failed!'
        else:
            return "Enter URL"


if __name__ == '__main__':
    app.run(debug=data["debug"])
