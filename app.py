from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello stranger</h1>'


@app.route('/home', methods=['GET'], defaults={'name': 'Default'})
@app.route('/home/<string:name>', methods=['GET'])
def home(name):
    return f'<h1>Hello {name},you are on the home page!'


@app.route('/json')
def json():
    return jsonify({'key': 'value', 'key2': [1, 2, 3, 4]})


if __name__ == '__main__':
    app.run(debug=True)
