from flask import Flask
from flask import render_template
from flask import request
from flask import abort, redirect, url_for
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/static/')
def projects():
    return 'The static page'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/uploaded_file.txt')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
