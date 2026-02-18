
import sqlite3
conn = sqlite3.connect("clinic.db")

conn.execute('''
CREATE TABLE IF NOT EXISTS appointments(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_name TEXT,
    email TEXT,
    date TEXT,
    token_number INTEGER,
    status TEXT
)
''')

conn.commit()
conn.close()
print("Database Ready")
