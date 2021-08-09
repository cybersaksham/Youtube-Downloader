from flask import Flask, render_template
import json

with open("config.json") as f:
    data = json.load(f)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=data["debug"])
