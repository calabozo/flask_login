import flask
from flask import redirect, flash, url_for
from flask import render_template, request
from flask_login import login_user, LoginManager, login_required, logout_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Length

from models import User

login_manager = LoginManager()

app = flask.Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
login_manager.init_app(app)


class login_form(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(1, 64)])
    pwd = PasswordField(validators=[InputRequired(), Length(min=1, max=72)])


@login_manager.user_loader
def load_user(user_id):
    return User.get_user_from_id(user_id)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login/", methods=("GET", "POST"), strict_slashes=False)
def login():
    form = login_form()

    if form.validate_on_submit():
        try:
            user = User.get_user_from_name(name=form.username.data)
            # if check_password_hash(user.pwd, form.pwd.data):
            if user is not None and user.pwd == form.pwd.data:
                login_user(user)
                return redirect(url_for('index'))
            else:
                flash("Invalid Username or password!")
        except Exception as e:
            flash(e)

    return render_template("auth.html", form=form, title="Login form", btn_action="Login")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route("/web_sender/")
@login_required
def web_sender():
    return render_template('web_sender.html')


@app.route('/rest_api', methods=['POST'])
@login_required
def launch():
    from datetime import datetime
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    data = request.get_json()
    body_message = data['body_message']
    # Do something with the message
    return f'{current_time} Launched with message: {body_message}'


if __name__ == "__main__":
    # app.run(debug=True, use_debugger=True, threaded=False, use_reloader=False)
    app.run(debug=True)
