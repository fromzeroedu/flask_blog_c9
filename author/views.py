from flask_blog import app
from flask import render_template, redirect
from author.form import RegisterForm

@app.route('/login')
def login():
    return "Hello, User!"

@app.route('/register', methods=('GET', 'POST'))
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('author/register.html', form=form)

@app.route('/success')
def success():
    return "Author registered!"
