from flask import render_template, request, redirect, url_for, flash, jsonify
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
@login_required
def create():
	return render_template('create.html')

@app.route('/addpost', methods=['POST'])
@login_required
def addpost():
		title = request.form['title']
		description = request.form['description']
		post = Articles(title=title, description=description, author_id=current_user.get_id())
		db.session.add(post)
		db.session.commit()
		return render_template('detail.html', article=post)

@app.route('/delete/<int:post_id>', methods=['GET'])
@login_required
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
	if db.session.query(User.id).filter_by(username=user.username).scalar() is not None:
		flash('Username already exists', 'error')
		return redirect(url_for('register'))
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
    return redirect(request.args.get('next') or url_for('index'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/api/posts', methods=['GET'])
def get_all_post():

    posts = Articles.query.all()

    output = []

    for post in posts:
        user_post = {}
        user_post['title'] = post.title
        user_post['description'] = post.description
        user_post['created_at'] = post.created_at
        user_post['author_id'] = post.author_id
        output.append(user_post)

    return jsonify({'posts' : output})



