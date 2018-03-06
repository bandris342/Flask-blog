from flask import render_template, request, redirect, url_for
from app.models import Articles, db
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




