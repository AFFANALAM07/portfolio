from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flash messages

def connect_db():
    return sqlite3.connect('messages.db')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO messages (name, email, message)
    VALUES (?, ?, ?)
    ''', (name, email, message))
    conn.commit()
    conn.close()

    flash('Your message has been sent successfully!', 'success')
    return redirect(url_for('contact'))

@app.route('/view_messages')
def view_messages():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT name, email, message, timestamp FROM messages')
    messages = cursor.fetchall()
    conn.close()
    return render_template('view_messages.html', messages=messages)

if __name__ == '__main__':
    app.run(debug=True)
