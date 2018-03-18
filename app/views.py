from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user , logout_user , current_user , login_required
from app.models import Articles, db, User
from app import app

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/list', methods=['GET'])
def list():
	articles = Articles.query.all()
	return render_template('list.html', articles = articles)

@app.route('/detail/<int:post_id>', methods=['GET'])
def detail(post_id):
	article = Articles.query.filter_by(id=post_id).first()
	return render_template('detail.html', article = article)

@app.route('/create', methods=['GET'])
def create():
	return render_template('create.html')

@app.route('/addpost', methods=['POST'])
def addpost():
		title = request.form['title']
		description = request.form['description']
		post = Articles(title=title, description=description)
		db.session.add(post)
		db.session.commit()
		return render_template('detail.html', article=post)

@app.route('/delete/<int:post_id>', methods=['GET'])
def delete(post_id):
	post = Articles.query.filter_by(id=post_id).first()
	db.session.delete(post)
	db.session.commit()
	return redirect(url_for('list'))


@app.route('/register', methods=['GET', 'POST'])
def register():
	if request.method == 'GET':
		return render_template('register.html')
	user = User(username=request.form['username'], password=request.form['password'])
	db.session.add(user)
	db.session.commit()
	flash('User successfully registered')
	return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    username = request.form['username']
    password = request.form['password']
    registered_user = User.query.filter_by(username=username,password=password).first()
    if registered_user is None:
        flash('Username or Password is invalid' , 'error')
        return redirect(url_for('login'))
    login_user(registered_user)
    flash('Logged in successfully')
    return redirect(request.args.get('next') or url_for('index'))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))



