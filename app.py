from flask import Flask, jsonify, request, url_for, redirect, session, render_template, g
import sqlite3

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'Thisisasecret!'


def connect_db():
    sql = sqlite3.connect('data.db')  # database root
    sql.row_factory = sqlite3.Row
    return sql


def get_db():
    if not hasattr(g, 'sqlite3'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


@app.route('/')
def index():
    session.pop('name', None)
    return '<h1>Hello stranger</h1>'


# Route Variables and Methods
@app.route('/home', methods=['GET'], defaults={'name': 'Default'})
@app.route('/home/<string:name>', methods=['GET'])
def home(name):
    session['name'] = name
    db = get_db()
    cur = db.execute('select id, name, location from users')
    results = cur.fetchall()

    return render_template('home.html', name=name, display=False, mylist=['one', 'two', 'three', 'four'],
                           listofdictionaries=[{'name': 'Zach'}, {'name': 'Zoe'}], results=results)


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

    db = get_db()
    db.execute('insert into users (name, location) values(?, ?)', [name, location])
    db.commit()

    # return f'<h1>Hello {name}. You are from {location}. You have submitted the form successfully!</h1>'
    return redirect(url_for('home', name=name, location=location))


# Request JSON Data
@app.route('/processjson', methods=['POST'])
def processjson():
    data = request.get_json()

    name = data['name']
    location = data['location']
    randomlist = data['randomlist']

    return jsonify({'result': 'Success!', 'name': name, 'location': location, 'randomkeyinlist': randomlist[1]})


@app.route('/viewresults')
def viewresults():
    db = get_db()
    cur = db.execute('select * from users')
    results = cur.fetchall()
    print(results[0]['location'])
    return f"<h1>The id is {results[0]['id']}, the name is {results[0]['name']}, the location is {results[0]['location']}</h1>"


if __name__ == '__main__':
    app.run()
