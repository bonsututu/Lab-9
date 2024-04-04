from flask import Flask, render_template, g
import sqlite3

app = Flask(__name__)
DATABASE = 'poems.db'

# Connect to the database
def connect_to_database():
    return sqlite3.connect(DATABASE)

# Query the database
def query_db(query, args=(), one=False):
    cur = g.db.execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

# Initialize database connection before request
@app.before_request
def before_request():
    g.db = connect_to_database()

# Close database connection after request
@app.teardown_request
def teardown_request(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# Route to display poems
@app.route('/')
def display_poems():
    poems = query_db('SELECT * FROM poems')
    return render_template('index.html', poems=poems)

if __name__ == '__main__':
    app.run(debug=True)
