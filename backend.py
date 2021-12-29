from flask import Flask, render_template
import urllib.request, json
import requests

app = Flask(__name__)

@app.route("/")
def getposts():
    response = requests.get("https://akwuko-temp.herokuapp.com/story/1")
    print(response)
    return response.text


if __name__ == '__main__':
    app.run(debug=True)