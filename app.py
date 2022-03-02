from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello stranger</h1>'


# Route Variables and Methods
@app.route('/home', methods=['GET'], defaults={'name': 'Default'})
@app.route('/home/<string:name>', methods=['GET'])
def home(name):
    return f'<h1>Hello {name},you are on the home page!'


@app.route('/json')
def json():
    return jsonify({'key': 'value', 'key2': [1, 2, 3, 4]})


# Request query String
# Example: http://127.0.0.1:5000/query?name=Sara&location=Florida
@app.route('/query')
def query():
    name = request.args.get('name')
    location = request.args.get('location')
    return f'<h1>Hi {name}. You are from {location}. You are on the query page</h1>'


# Request Form Data
@app.route('/theform')
def theform():
    return '''<form method="POST" action="/process"> 
                <input type="text" name="name">
                <input type="text" name="location">
                <input type="submit" value="Submit">
              </form>
                '''


@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    location = request.form['location']

    return f'<h1>Hello {name}. You are from {location}. You have submitted the form successfully!</h1>'


if __name__ == '__main__':
    app.run(debug=True)
