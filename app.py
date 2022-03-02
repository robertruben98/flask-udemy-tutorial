from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello stranger</h1>'

@app.route('/<name>')
def index_name(name):
    return f'<h1>Hello {name}!</h1>'

if __name__ == '__main__':
    app.run()