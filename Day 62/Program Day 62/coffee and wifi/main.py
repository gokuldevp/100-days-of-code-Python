from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv


# constants for choices for selectField
COFFEE = ("☕", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕", "✘")
WIFI = ("💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪", "✘")
POWER = ("🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌", "✘")

# creating a flask app , scream key and enabling app to use bootstrap
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    # creating Forms
    cafe = StringField('Cafe name', validators=[DataRequired()])
    url = StringField('Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL()])
    open = StringField('Opening Time e.g 6:30AM', validators=[DataRequired()])
    close = StringField('Closing Time  e.g 6PM', validators=[DataRequired()])
    coffee = SelectField('Coffee', choices=COFFEE, validators=[DataRequired()])
    wifi = SelectField('Wifi', choices=WIFI, validators=[DataRequired()])
    power = SelectField('Power', choices=POWER, validators=[DataRequired()])
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['POST', 'GET'])
def add_cafe():
    """open page add.html and in the page add items in the database"""
    form = CafeForm()
    if form.validate_on_submit():
        # adding form data to a csv file
        with open("cafe-data.csv", mode="a", encoding='utf-8') as csv_file:
            csv_file.write(f"\n{form.cafe.data},"
                           f"{form.url.data},"
                           f"{form.open.data},"
                           f"{form.close.data},"
                           f"{form.coffee.data},"
                           f"{form.wifi.data},"
                           f"{form.power.data}")
        # redirecting the page to cafes.html
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    # function to open cafes.html and show the csv file un the page
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


# run the app
if __name__ == '__main__':
    app.run(debug=True)
