from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import os
import requests


TMDB_API_KEY = os.environ.get("API_KEY")
MOVIE_DATA_BY_TITLE_URL = "https://api.themoviedb.org/3/search/movie?"


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class EditForm(FlaskForm):
    """Create Edit Form."""
    rating = FloatField("Your Rating Out of 10, eg: 7.5 :", validators=[DataRequired()])
    review = StringField("Your Review :", validators=[DataRequired()])
    update = SubmitField("Update Movie")


class AddForm(FlaskForm):
    """Create Add Form."""
    title = StringField("Movie Name :", validators=[DataRequired()])
    add = SubmitField("Add Movie")


# creating a database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Movie.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# creating a Table in the database
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False, unique=True)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True, unique=True)
    review = db.Column(db.String(300), nullable=True)
    img_url = db.Column(db.String(250), nullable=False, unique=True)


db.create_all()

# # add a new entry to the database with the following values:
# # After adding the new_movie the code needs to be commented out/deleted.So you are not trying to add the same movie twice.
# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# db.session.add(new_movie)
# db.session.commit()


# open home page
@app.route("/")
def home():
    """reading data from the table to be display and giving the data to the page index.html"""
    all_movies = Movie.query.order_by(Movie.rating).all()
    for num in range(len(all_movies)):
        pass
        all_movies[num].ranking = len(all_movies) - num
    return render_template("index.html", movies=all_movies)


# add a new movie to the database
@app.route("/add", methods=["POST", "GET"])
def add():
    form = AddForm()
    if form.validate_on_submit():
        title = request.form["title"]
        return redirect(url_for('select', title=title))
    return render_template("add.html", form=form)


# selecting movie from the list.
@app.route("/select")
def select():
    response = requests.get(url=MOVIE_DATA_BY_TITLE_URL,
                            params={
                                "query": request.args.get("title"),
                                "api_key": TMDB_API_KEY,
                            })
    movie_details = response.json()["results"]
    return render_template("select.html", movies=movie_details)


# find the details of movie
@app.route("/find")
def find():
    """Find teh details of the movie based on the movie id got from add.html and add the detail of movie to the database."""
    movie_id = request.args.get('m_id')
    movie_data_by_id_url = f"https://api.themoviedb.org/3/movie/{movie_id}?"
    response = requests.get(url=movie_data_by_id_url,
                            params={
                                'api_key': TMDB_API_KEY
                            })
    movie_details = response.json()
    new_movie = Movie(
        title=movie_details["original_title"],
        year=movie_details["release_date"].split('-')[0],
        description=movie_details["overview"],
        img_url=f"https://image.tmdb.org/t/p/w500/{movie_details['poster_path']}"
    )
    try:
        db.session.add(new_movie)
        db.session.commit()
    except IntegrityError:
        return redirect(url_for('home'))
    return redirect(url_for('edit', m_id=new_movie.id))


# open edit page
@app.route("/edit", methods=["GET", "POST"])
def edit():
    """Getting hold of the id to be updated and update the rating and review of that record according to the form."""
    form = EditForm()
    movie_id = request.args.get("m_id")
    movie_to_be_updated = Movie.query.get(movie_id)
    if form.validate_on_submit():
        movie_to_be_updated.rating = request.form["rating"]
        movie_to_be_updated.review = request.form["review"]
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", form=form, movie=movie_to_be_updated)


@app.route("/delete")
def delete():
    """Get hold of the id of record to be deleted and delete that record."""
    movie_id = request.args.get("m_id")
    movie = Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
