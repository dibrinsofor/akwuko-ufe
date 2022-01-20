from flask import Flask, render_template, jsonify
import urllib.request, json
import requests

app = Flask(__name__)

@app.route("/", methods=["GET"])
def getposts():
    response = requests.get("https://akwuko-temp.herokuapp.com/api/story/")
    data = json.loads(response.content)
    return render_template("index.html", data=data)


if __name__ == '__main__':
    app.run(debug=True)