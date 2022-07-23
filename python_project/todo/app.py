from datetime import datetime
from flask import Flask, jsonify, redirect, render_template, request, url_for, flash
from flask_sqlalchemy import SQLAlchemy

from form import todoForm, UpdatetodoForm

app = Flask(__name__)
app.config['SECRET_KEY']= '0eba9754456ba29dc071ad4fb4d99d5bf87852ebcae1369bb'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'

db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    time_posted = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self) -> str:
        return f'Todo ({self.title}, {self.time_posted})'

@app.route("/")
@app.route("/home")
def home():
    form = todoForm()
    todos = Todo.query.all()
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
        return render_template('update.html',form = form, todo_data=todo_data)

@app.route('/todo/<int:todo_id>/delete',methods=['POST'])
def delete(todo_id):
    todo_data = Todo.query.get_or_404(todo_id)  
    db.session.delete(todo_data)
    db.session.commit()
    flash('Your Todo is deleted Succesfully!','info')
    return redirect(url_for('home'))

@app.route('/getTable')
def getTable():
    todos = Todo.query.all()
    todoTable= render_template('todoTable.html', todos=todos)
    return todoTable

@app.route('/addTodo', methods=['POST'])
def addTodo():
    form = todoForm()
    todos = Todo.query.all()    
    if request.method == 'POST' and request.form:
        title = request.form['title']
        todo = Todo(title=title, time_posted=datetime.utcnow())
        db.session.add(todo)
        db.session.commit() 
        print('done')
        flash('Your To-Do is added!','success')
        todoTable= render_template('todoTable.html', todos=todos,form=form)
        return todoTable
    return jsonify('No Data Recieved!')

if __name__ == '__main__':
    app.run(debug=True)