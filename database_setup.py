import sqlite3

# Connect to the database (or create it)
conn = sqlite3.connect('messages.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a table to store messages
cursor.execute('''
CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    message TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database setup completed.")
