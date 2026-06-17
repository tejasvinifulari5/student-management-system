from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Create database and table
def init_db():
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

    conn.commit()
    conn.close()

# Initialize database
init_db()


# Home Page - View Students
@app.route('/')
def home():

    conn = sqlite3.connect('database.db')

    students = conn.execute(
        "SELECT * FROM students"
    ).fetchall()

    conn.close()

    return render_template(
        'index.html',
        students=students
    )


# Add Student
@app.route('/add', methods=['GET', 'POST'])
def add_student():

    if request.method == 'POST':

        name = request.form['name']
        branch = request.form['branch']
        year = request.form['year']
        email = request.form['email']
        phone = request.form['phone']

        conn = sqlite3.connect('database.db')

        conn.execute(
            """
            INSERT INTO students
            (name, branch, year, email, phone)
            VALUES (?, ?, ?, ?, ?)
            """,
            (name, branch, year, email, phone)
        )

        conn.commit()
        conn.close()

        return redirect('/')

    return render_template('add_student.html')


# Delete Student
@app.route('/delete/<int:id>')
def delete_student(id):

    conn = sqlite3.connect('database.db')

    conn.execute(
        "DELETE FROM students WHERE id=?",
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect('/')


# Edit Student
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):

    conn = sqlite3.connect('database.db')

    if request.method == 'POST':

        name = request.form['name']
        branch = request.form['branch']
        year = request.form['year']
        email = request.form['email']
        phone = request.form['phone']

        conn.execute(
            """
            UPDATE students
            SET name=?,
                branch=?,
                year=?,
                email=?,
                phone=?
            WHERE id=?
            """,
            (name, branch, year, email, phone, id)
        )

        conn.commit()
        conn.close()

        return redirect('/')

    student = conn.execute(
        "SELECT * FROM students WHERE id=?",
        (id,)
    ).fetchone()

    conn.close()

    return render_template(
        'edit_student.html',
        student=student
    )


if __name__ == "__main__":
    app.run(debug=True)