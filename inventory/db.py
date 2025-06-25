# Handles DB operations
import sqlite3

def get_connection():
    conn = sqlite3.connect('inventory.db')
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS inventory (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        quantity INTEGER,
                        threshold INTEGER)''')
    conn.commit()
    conn.close()