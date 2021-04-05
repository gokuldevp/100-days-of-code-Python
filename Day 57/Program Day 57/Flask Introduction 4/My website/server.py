from flask import Flask, render_template
from random import randint
import requests
import datetime


app = Flask(__name__)
N_POINT_URL = "https://api.npoint.io/5abcca6f4e39b4955965"


@app.route("/")
def home():
    random_number = randint(0, 100)
    current_date = datetime.date.today().year
    return render_template("index.html", r_num=random_number, date=current_date)


@app.route("/blog")
def blog():
    all_blogposts = requests.get(N_POINT_URL).json()
    return render_template("Blog.html", all_blogposts=all_blogposts)


if __name__ == "__main__":
    app.run(debug=True)

# we can pass in parameters in render template function for python code to work in html
# we use {{ }} for writing python in html and {% %} for writhing python syntax with multiple lines
# we can also use url_for('function_name') for adding links using python
# we can give parameter to url_for('function', parameter) for adding parameter for link posts
