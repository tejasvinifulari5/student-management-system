import sqlite3

conn = sqlite3.connect('database.db')

conn.execute('''
CREATE TABLE IF NOT EXISTS students(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
branch TEXT,
year TEXT,
email TEXT,
phone TEXT
)
''')

conn.close()

print("Database created")

from flask import Flask, render_template
from flask import request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

@app.route('/add', methods=['GET','POST'])
def add_student():

    if request.method == 'POST':

        name = request.form['name']
        branch = request.form['branch']
        year = request.form['year']
        email = request.form['email']
        phone = request.form['phone']

        conn = sqlite3.connect('database.db')

        conn.execute(
            "INSERT INTO students(name,branch,year,email,phone) VALUES(?,?,?,?,?)",
            (name,branch,year,email,phone)
        )

        conn.commit()
        conn.close()

        return redirect('/')

    return render_template('add_student.html')
    