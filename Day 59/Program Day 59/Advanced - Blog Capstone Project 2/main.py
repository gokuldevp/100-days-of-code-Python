from flask import Flask, render_template
import requests

API_URL = "https://api.npoint.io/5abcca6f4e39b4955965"

POST_IMG = ['img/post-bg.jpg', 'img/post-bg 2.jpg', 'img/post-bg 3.jpg']

posts = requests.get(API_URL).json()

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:post_id>")
def post(post_id):
    current_post = None
    for blog_post in posts:
        if blog_post['id'] == post_id:
            current_post = blog_post
    return render_template("post.html", blog_post=current_post, post_img_path=POST_IMG[int(post_id)-1])


if __name__ == '__main__':
    app.run(debug=True)
