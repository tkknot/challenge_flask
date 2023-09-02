from markupsafe import escape
from flask import url_for, Flask, request, redirect

app = Flask(__name__)

# ------------------------------------------

# @app.route('/')
# def hello_world():
#     return "aaaa"

# @app.route('/<int:name>')
# def hello(name):
#     return f"{escape(name)}"

# ------------------------------------------
# @app.route('/')
# def index():
#     return 'index'

# @app.route('/login')
# def login():
#     return 'login'

# @app.route('/user/<string:username>')
# def profile(username):
#     return f'{username}\'s profile'

# with app.test_request_context():
#     # url_for(function_name, params)
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='Doe'))

# ------------------------------------------

# @app.get('/login')
# @app.post('/login')

# ------------------------------------------

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return "aaaaa"