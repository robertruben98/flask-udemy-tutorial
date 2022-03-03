from flask import Flask, jsonify, request, url_for, redirect, session, render_template

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'Thisisasecret!'

@app.route('/')
def index():
    session.pop('name', None)
    return '<h1>Hello stranger</h1>'


# Route Variables and Methods
@app.route('/home', methods=['GET'], defaults={'name': 'Default'})
@app.route('/home/<string:name>', methods=['GET'])
def home(name):
    session['name'] = name
    return render_template('home.html', name=name, display=False)


@app.route('/json')
def json():
    if 'name' in session:
        name = session['name']
    else:
        name = 'NotinSession!'
    return jsonify({'key': 'value', 'key2': [1, 2, 3, 4], 'name': name})


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
    return render_template('form.html')


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
