from markupsafe import escape
from flask import Flask, url_for, request
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

#HTML Escaping
@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

#Variable Rules
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

# Converter types:
# string (default) accepts any text without a slash
# int accepts positive integers
# float accepts positive floating point values
# path like string but also accepts slashes
# uuid accepts UUID strings

#Unique URLs / Redirection Behavior
@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

#URL Building
# @app.route('/login')
# def login():
#     return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    # print(url_for('login'))
    # print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))

#HTTP methods
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'do_the_login()'
    else:
        return 'show_the_login_form()'
    
#OR
@app.get('/login')
def login_get():
    return 'show_the_login_form()'

@app.post('/login')
def login_post():
    return 'do_the_login()'