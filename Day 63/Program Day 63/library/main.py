from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# CREATE TABLE
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False, unique=True)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Integer, nullable=False)


db.create_all()


@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        rating = request.form['rating']
        new_book = Book(title=title, author=author, rating=rating)
        try:
            # ADDING DATA TO TABLE
            db.session.add(new_book)
            db.session.commit()
        except IntegrityError:
            pass
        return redirect(url_for('home'))
    return render_template('add.html')


@app.route("/delete")
def delete():
    # DELETING ROWS FROM TABLE
    book_id = request.args.get("id")
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/edit", methods=["POST", "GET"])
def edit():
    if request.method == "POST":
        # UPDATING RATING FROM OF THE SELECTED ID
        book_id = request.args.get('id')
        book_to_edit = Book.query.get(book_id)
        book_to_edit.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))

    book_id = request.args.get('id')
    book_selected = Book.query.get(book_id)
    return render_template("edit.html", book=book_selected )


if __name__ == "__main__":
    app.run()
