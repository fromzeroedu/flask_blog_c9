from flask_blog import app
from flask import render_template, redirect, flash, url_for, session, abort
from blog.form import SetupForm
from flask_blog import db
from author.models import Author
from blog.models import Blog
from author.decorators import login_required
import bcrypt

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/admin')
@login_required
def admin():
    blogs = Blog.query.count()
    if blogs == 0:
        return redirect(url_for('setup'))
    if session.get('is_author'):
        return render_template('blog/admin.html')
    else:
        abort(403)
    return render_template('blog/admin.html')

@app.route('/setup', methods=('GET', 'POST'))
def setup():
    form = SetupForm()
    if form.validate_on_submit():
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(form.password.data, salt)
        author = Author(
            form.fullname.data,
            form.email.data,
            form.username.data,
            hashed_password,
            True
        )
        db.session.add(author)
        db.session.flush()
        if author.id:
            blog = Blog(form.name.data, author.id)
            db.session.add(blog)
            db.session.flush()
        else:
            db.session.rollback()
            error = "Error creating user"
        if author.id and blog.id:
            db.session.commit()
        else:
            db.session.rollback()
            error = "Error creating blog"
        flash('Blog created')
        return redirect('/admin')
    return render_template('blog/setup.html', form=form)
