from flask import Flask, render_template


app = Flask(__name__)


# the render_template function is used to run html files in the Flask,
# we need to put the html files in a folder called 'templates' and other files like images, css, icons etc in 'static'
@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

