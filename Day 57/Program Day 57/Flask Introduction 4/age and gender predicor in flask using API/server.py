from flask import Flask, render_template
import requests

GENDER_URL = "https://api.genderize.io?"
AGE_URL = "https://api.agify.io?"

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Enter your Name In URL as /name to show your predicted age and Gender"


@app.route("/<name>")
def guess(name):
    gender = requests.get(GENDER_URL, params={"name": f"{name}"}).json()["gender"]
    age = requests.get(AGE_URL, params={"name": f"{name}"}).json()["age"]
    return render_template("index.html", age=age, gender=gender, name=name)


if __name__ == '__main__':
    app.run(debug=True)
