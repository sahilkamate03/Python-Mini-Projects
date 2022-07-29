from flask import jsonify, redirect, render_template, request, url_for, flash, abort
from flask_login import current_user, login_user, logout_user, login_required
from oauthlib.oauth2 import WebApplicationClient

from datetime import date
import os
import requests
import json

from planner import app, db
from planner.form import todoForm, UpdatetodoForm
from planner.models import User, Todo

GOOGLE_CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET')
GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration"
)

client = WebApplicationClient(GOOGLE_CLIENT_ID)


def get_google_provider_cfg():
    return requests.get(GOOGLE_DISCOVERY_URL).json()


today = str(date.today()).split('-')
today = '_'.join(today)


@app.route("/login")
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
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
        unique_id = userinfo_response.json()["sub"]
        users_email = userinfo_response.json()["email"]
        picture = userinfo_response.json()["picture"]
        users_name = userinfo_response.json()["given_name"]

        if not(User.query.filter_by(unique_id=unique_id).first()):
            user = User(unique_id=unique_id, username=users_email.split(
                '@')[0], email=users_email)
            db.session.add(user)
            db.session.commit()

        user = User.query.filter_by(unique_id=unique_id).first()
        login_user(user, remember=False)

    else:
        return "User email not available or not verified by Google.", 400

    return redirect(url_for("home"))


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route("/")
@app.route("/home")
@login_required
def home():
    form = todoForm()
    user = User.query.filter_by(email=current_user.email).first()
    todos_remain = Todo.query.filter_by(
        user_id=user.id, date_posted=today, type='R').all()
    todos_complete = Todo.query.filter_by(
        user_id=user.id, date_posted=today, type='C').all()
    if request.method == "GET":
        return render_template('home.html', form=form, todos_complete=todos_complete, todos_remain=todos_remain, current_username=current_user.username)


@app.route('/todo/<int:todo_id>/update', methods=['GET', 'POST'])
@login_required
def update(todo_id):
    todo_data = Todo.query.get_or_404(todo_id)
    if todo_data.author != current_user:
        abort(403)
    form = UpdatetodoForm()
    if request.method == 'POST':
        if form.title.data:
            todo_data.title = form.title.data
        db.session.commit()
        return redirect(url_for('home'))

    if request.method == 'GET':
        return render_template('update.html', form=form, todo_data=todo_data)


@app.route('/todo/<int:todo_id>/delete', methods=['GET', 'POST'])
@login_required
def delete(todo_id):
    todo_data = Todo.query.get_or_404(todo_id)
    if todo_data.author != current_user:
        abort(403)
    if request.method == 'POST':
        db.session.delete(todo_data)
        db.session.commit()
        return redirect(url_for('home'))

    if request.method == 'GET':
        db.session.delete(todo_data)
        db.session.commit()
        return redirect(url_for('home'))


@app.route('/todo/<int:todo_id>/complete', methods=['POST'])
@login_required
def complete(todo_id):
    todo_data = Todo.query.get_or_404(todo_id)
    if todo_data.author != current_user:
        abort(403)

    if request.method == 'POST':
        todo_data.type = "C"
        db.session.commit()
        return redirect(url_for('home'))

    if request.method == 'GET':
        return redirect(url_for('home'))


@app.route('/todo/<int:todo_id>/undo', methods=['POST'])
@login_required
def undo(todo_id):
    todo_data = Todo.query.get_or_404(todo_id)
    if todo_data.author != current_user:
        abort(403)

    if request.method == 'POST':
        todo_data.type = "R"
        db.session.commit()
        return redirect(url_for('home'))

    if request.method == 'GET':
        return redirect(url_for('home'))


@app.route('/<string:dateSelected>/getTable')
@login_required
def getTable(dateSelected):
    user = User.query.filter_by(email=current_user.email).first()
    if not(dateSelected):
        dateSelected = today
    todos_remain = Todo.query.filter_by(
        user_id=user.id, date_posted=dateSelected, type='R').all()
    todos_complete = Todo.query.filter_by(
        user_id=user.id, date_posted=dateSelected, type='C').all()

    todoTable_remain = render_template(
        'todoTable_remain.html', todos_remain=todos_remain)
    todoTable_complete = render_template(
        'todoTable_complete.html', todos_complete=todos_complete)

    data = {'remain': todoTable_remain, 'complete': todoTable_complete}
    return jsonify(data)


@app.route('/addTodo', methods=['POST'])
@login_required
def addTodo():
    form = todoForm()
    todos = Todo.query.all()
    if request.method == 'POST' and request.form:
        title = request.form['title']
        todo = Todo(title=title, date_posted=today, author=current_user)
        db.session.add(todo)
        db.session.commit()

        user = User.query.filter_by(email=current_user.email).first()
        todos_remain = Todo.query.filter_by(
            user_id=user.id, date_posted=today, type='R').all()
        todos_complete = Todo.query.filter_by(
            user_id=user.id, date_posted=today, type='C').all()

        todoTable_remain = render_template(
            'todoTable_remain.html',  todos_remain=todos_remain)
        todoTable_complete = render_template(
            'todoTable_complete.html', todos_complete=todos_complete)

        data = {'remain': todoTable_remain, 'complete': todoTable_complete}
        return jsonify(data)

    return jsonify('No Data Recieved!')
