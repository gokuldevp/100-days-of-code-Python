from flask import Flask
from random import randint

# creating object app from class flask
app = Flask(__name__)

# finding a random number to guess from 0 to 10
find_num = randint(0, 10)


# creating home page
@app.route("/")
def home():
    return "<h1> Select a number from 0 to 9</h1>" \
           '<img src="https://media.giphy.com/media/qq7ef70oHLoAM/giphy.gif">'


@app.route("/<int:num>")
def result(num):

    # page for correct number
    if num == find_num:
        return "<h1 style='color:green'>You Are Right!</h1>" \
               '<img src="https://media.giphy.com/media/xkYkgcptz3OmI/giphy.gif" width=100%>'

    # page for low number
    elif num < find_num:
        return "<h1 style='color:blue'>Your Number is too Low! Try again?</h1>" \
               '<img src="https://media.giphy.com/media/3og0IPooGNUCe2fEFa/giphy.gif" width=100%>'

    # page for high number
    elif num > find_num:
        return "<h1 style='color:red'>Your Number is too High! Try again?</h1>" \
               '<img src="https://media.giphy.com/media/h4NlRPJCQAXOto7E4g/giphy.gif" width=100%>'


# running app
if __name__ == "__main__":
    app.run(debug=True)
