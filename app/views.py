from flask import render_template, request
from app.models import Articles, db
from app import app


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/list')
def list():
	articles = Articles.query.all()
	return render_template('list.html', articles = articles)

@app.route('/detail/<int:post_id>')
def detail(post_id):
	article = Articles.query.filter_by(id=post_id).first()
	return render_template('detail.html', article = article)

@app.route('/create', methods=['GET'])
def create_post():
	return render_template('create.html')

@app.route('/addpost', methods=['GET', 'POST'])
def addpost():

		title = request.form['title']
		description = request.form['description']
		post = Articles(title=title, description=description)
		db.session.add(post)
		db.session.commit() #Adding the post to the database.
		return render_template('detail.html', article=post)



