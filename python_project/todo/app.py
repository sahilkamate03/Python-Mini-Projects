from datetime import datetime, date
from flask import Flask, jsonify, redirect, render_template, request, url_for, flash, session, abort
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from authlib.integrations.flask_client import OAuth
from authlib.common.security import generate_token
from oauthlib.oauth2 import WebApplicationClient
import requests

import os
import json

from form import todoForm, UpdatetodoForm
from model import User, Todo

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('TODO_FLASK_SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

db = SQLAlchemy(app)
oauth = OAuth(app)


today = str(date.today()).split('-')
today = '_'.join(today)


GOOGLE_CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET')
GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration"
)

client = WebApplicationClient(GOOGLE_CLIENT_ID)


def get_google_provider_cfg():
    return requests.get(GOOGLE_DISCOVERY_URL).json()


@app.route("/login")
def login():
    # Find out what URL to hit for Google login
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    # Use library to construct the request for Google login and provide
    # scopes that let you retrieve user's profile from Google
    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=request.base_url + "/callback",
        scope=["openid", "email", "profile"],
    )
    return redirect(request_uri)


@app.route("/login/callback")
def callback():
    # Get authorization code Google sent back to you
    code = request.args.get("code")
    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]

    # Prepare and send a request to get tokens! Yay tokens!
    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
    )

    # Parse the tokens!
    client.parse_request_body_response(json.dumps(token_response.json()))
    # Now that you have tokens (yay) let's find and hit the URL
    # from Google that gives you the user's profile information,
    # including their Google profile image and email
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)

    # You want to make sure their email is verified.
    # The user authenticated with Google, authorized your
    # app, and now you've verified their email through Google!
    if userinfo_response.json().get("email_verified"):
        print(userinfo_response.json())
        unique_id = userinfo_response.json()["sub"]
        users_email = userinfo_response.json()["email"]
        picture = userinfo_response.json()["picture"]
        users_name = userinfo_response.json()["given_name"]

        print(unique_id, users_email, picture, users_name)
    else:
        return "User email not available or not verified by Google.", 400

    return redirect(url_for("home"))


@app.route("/logout")
def logout():
    return redirect(url_for("home"))


@app.route("/")
@app.route("/home")
def home():
    form = todoForm()
    todos = Todo.query.filter_by(date_posted=today).all()
    if request.method == "GET":
        return render_template('home.html', form=form, todos=todos)


@app.route('/todo/<int:todo_id>/update', methods=['GET', 'POST'])
def update(todo_id):
    form = UpdatetodoForm()
    todo_data = Todo.query.get_or_404(todo_id)
    if request.method == 'POST':
        if form.title.data:
            todo_data.title = form.title.data
        db.session.commit()
        return redirect(url_for('home'))

    if request.method == 'GET':
        return render_template('update.html', form=form, todo_data=todo_data)


@app.route('/todo/<int:todo_id>/delete', methods=['POST'])
def delete(todo_id):
    todo_data = Todo.query.get_or_404(todo_id)
    db.session.delete(todo_data)
    db.session.commit()
    flash('Your Todo is deleted Succesfully!', 'info')
    return redirect(url_for('home'))


@app.route('/<string:dateSelected>/getTable')
def getTable(dateSelected):
    todos = Todo.query.filter_by(date_posted=dateSelected).all()
    todoTable = render_template('todoTable.html', todos=todos)
    return todoTable


@app.route('/addTodo', methods=['POST'])
def addTodo():
    form = todoForm()
    todos = Todo.query.all()
    if request.method == 'POST' and request.form:
        title = request.form['title']
        todo = Todo(title=title, date_posted=today)
        db.session.add(todo)
        db.session.commit()
        print('done')
        flash('Your To-Do is added!', 'success')
        todoTable = render_template('todoTable.html', todos=todos, form=form)
        return todoTable
    return jsonify('No Data Recieved!')


if __name__ == '__main__':
    app.run(debug=True)
