from flask import Flask, render_template
import requests


API_URL = "https://api.npoint.io/5abcca6f4e39b4955965"
all_posts = requests.get(API_URL).json()

app = Flask(__name__)


@app.route('/')
def home(posts=all_posts):
    return render_template("index.html", blog_posts=posts)


@app.route("/<int:post_id>")
def read(post_id, posts=all_posts):
    return render_template("post.html", post_id=post_id, blog_posts=posts)


if __name__ == "__main__":
    app.run(debug=True)
