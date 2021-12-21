from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello Im running Flask over Vercel'


@app.route('/test')
def test():
    return 'Testing another route'
