from flask import Flask


app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper


def make_emphasis(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper


def make_underlined(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper


@app.route("/")
@make_bold
@make_emphasis
@make_underlined
def my_name():
    return f"gokul"





if __name__ == "__main__":
    # we use parameter debug=True for making the site change after saving file each time ,its default is False.
    # we can also edit our code in the browser using the debugger PIN
    app.run(debug=True)
