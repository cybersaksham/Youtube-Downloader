from flask import Flask, render_template, request, jsonify
from pytube import YouTube
import json

with open("config.json") as f:
    data = json.load(f)

app = Flask(__name__)


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
            videos = list(yt.streams)
            dict__ = {}
            for index, video in enumerate(videos):
                dict__[index + 1] = {}
                str_video__ = str(video).split(" ")
                for item in str_video__:
                    if "mime_type" == item.split("=")[0]:
                        dict__[index + 1]["mime_type"] = item.split("=")[1].split("\"")[1]
                    if "res" == item.split("=")[0]:
                        dict__[index + 1]["res"] = item.split("=")[1].split("\"")[1]
                    if "type" == item.split("=")[0]:
                        dict__[index + 1]["type"] = item.split("=")[1].split("\"")[1]
                    if "abr" == item.split("=")[0]:
                        dict__[index + 1]["abr"] = item.split("=")[1].split("\"")[1]
            return jsonify(error=None, types=dict__)
        except Exception as e:
            return jsonify(error=str(e), types=None)


if __name__ == '__main__':
    app.run(debug=data["debug"])
