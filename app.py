from flask import Flask, jsonify, request, url_for, redirect

app = Flask(__name__)

app.config['DEBUG'] = True

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
    return '''<form method="POST" action="/theform"> 
                <input type="text" name="name">
                <input type="text" name="location">
                <input type="submit" value="Submit">
              </form>
                '''


# Incoming Request Method
@app.route('/theform', methods=['POST'])
def process():
    name = request.form['name']
    location = request.form['location']

    #return f'<h1>Hello {name}. You are from {location}. You have submitted the form successfully!</h1>'
    return redirect(url_for('home', name=name, location=location))


# Request JSON Data
@app.route('/processjson', methods=['POST'])
def processjson():
    data = request.get_json()

    name = data['name']
    location = data['location']
    randomlist = data['randomlist']

    return jsonify({'result': 'Success!', 'name': name, 'location': location, 'randomkeyinlist': randomlist[1]})


if __name__ == '__main__':
    app.run()
