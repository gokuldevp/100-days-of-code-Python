from flask import Flask, render_template, request
import requests
from smtplib import SMTP
import os

MY_EMAIL = "mikedavid9998@gmail.com"
MY_PASSWORD = os.environ.get("MY_PASSWORD")


def send_mail(name, email, phone, message):
    with SMTP("smtp.gmail.com") as connection:
        email_message = f"Subject:Contact Me\n\nName: {name}\nE-Mail: {email}\nPhone Number: {phone}\nMessage: {message}"
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=email_message
        )


API_URL = "https://api.npoint.io/5abcca6f4e39b4955965"
posts = requests.get(API_URL).json()

POST_IMG = ['img/post-bg.jpg', 'img/post-bg 2.jpg', 'img/post-bg 3.jpg']

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        data = request.form
        send_mail(data.get('name'), data.get('email'), data.get('phone'), data.get('message'))
        # print(data["name"])
        # print(data["email"])
        return render_template("contact.html", msg=True)

    return render_template("contact.html", msg=False)


@app.route("/post/<int:post_id>")
def post(post_id):
    current_post = None
    for blog_post in posts:
        if blog_post['id'] == post_id:
            current_post = blog_post

    return render_template("post.html", blog_post=current_post, post_img_path=POST_IMG[int(post_id)-1])


if __name__ == '__main__':
    app.run(debug=True)
