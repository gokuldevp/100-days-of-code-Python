from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap


class LoginForm(FlaskForm):
    """The class for creating forms and validating the form"""
    email = StringField(label='email', validators=[DataRequired(), Email()])
    password = PasswordField(label='password', validators=[DataRequired(), Length(min=8, max=16)])
    submit = SubmitField(label='Log In')


app = Flask(__name__)
app.secret_key = "123 abc 456"
# Giving access to Bootstrap templates to Flask app
Bootstrap(app=app)


@app.route("/")
def home():
    """Home page"""
    return render_template('index.html')


@app.route("/login", methods=['POST', 'GET'])
def login():
    """Login page takes user email and password, Then return page success.html for valid users and denied.html for invalid users"""
    login_form = LoginForm()
    if request.method == "POST":
        if login_form.validate_on_submit():
            if login_form.email.data == "admin@gmail.com" and login_form.password.data == "1234567890":
                return render_template('success.html')
            else:
                return render_template('denied.html')
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
