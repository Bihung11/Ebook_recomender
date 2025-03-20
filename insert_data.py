import sqlite3
import csv

# Connect to the database (creates it if not exists)
conn = sqlite3.connect('ebooks.db')
cursor = conn.cursor()

# Create the ebooks table if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS ebooks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        tags TEXT,
        cover TEXT,
        pdf TEXT
    )
''')

# Open and read the CSV file
with open('ebooks_data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    for row in reader:
        cursor.execute("INSERT INTO ebooks (title, tags, cover, pdf) VALUES (?, ?, ?, ?)", row)

# Commit changes and close connection
conn.commit()
conn.close()

print("Data inserted successfully.")
