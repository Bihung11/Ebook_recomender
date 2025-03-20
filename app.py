from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# Function to create database & table
def create_db():
    conn = sqlite3.connect('ebooks.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ebooks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            tags TEXT,
            cover TEXT,
            pdf TEXT
        )
    ''')
    conn.commit()
    conn.close()

create_db()  # Run on startup to ensure DB exists

# Function to fetch books based on tags
def get_books_by_tag(tag):
    conn = sqlite3.connect('ebooks.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ebooks WHERE tags LIKE ? LIMIT 5", ('%' + tag + '%',))
    books = cursor.fetchall()
    conn.close()
    return books

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    tag = request.args.get('tag', '').lower()
    books = get_books_by_tag(tag)
    return jsonify(books)

if __name__ == '__main__':
    app.run(debug=True)
