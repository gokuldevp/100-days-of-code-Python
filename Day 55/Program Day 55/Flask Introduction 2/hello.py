from flask import Flask


# creating a object app using the class Flask
app = Flask(__name__)


# using python Decorator Function and using @ to call that function
# @app.route("/") is used to open the home page
@app.route("/")
def hello_world():
    return "Hello World"


# "/bye" open the page address after the www.home.com/bye
@app.route("/bye")
def say_bye():
    return "Good Bye"


# we can us <parameter> to make the path dynamic
@app.route("/<name>")
def my_name(name):
    return f"My name is {name}"


# we can add other static or dynamic name to path after <parameter>, also we can use <datatype:parameter to predefine the parameter>
@app.route("/<name>/<int:age>")
def my_name_age(name, age):
    return f"My name is {name} and I am {age} year's old."


# we can add <path: parameter> to make every thing at the end of the path parameter including /
@app.route("/username/<path:username>")
def my_username(username):
    return f"My name is {username} "


# we can render HTML files in Flask by jest returning the HTML file in return
# we can use \ to add next line in the html lines
@app.route("/html")
def my_html():
    return '<h1>Hello Testing Html</h1>' \
           '<p>Naruto</p>' \
           '<img src="https://media.giphy.com/media/4gsjHZMPXdlGo/giphy.gif">'


print(__name__)

if __name__ == "__main__":
    # we use parameter debug=True for making the site change after saving file each time ,its default is False.
    # we can also edit our code in the browser using the debugger PIN
    app.run(debug=True)
