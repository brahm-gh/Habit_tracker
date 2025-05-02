import sqlite3
from datetime import datetime
from habit import Habit
import json

DB_NAME = 'data/habits.db'

def initialize_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS habits (
                 name TEXT PRIMARY KEY,
                 periodicity TEXT,
                 created_at TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS checkoffs (
                 habit_name TEXT,
                 timestamp TEXT)''')
    
        # Check if predefined habits are missing
    c.execute("SELECT COUNT(*) FROM habits")
    if c.fetchone()[0] == 0:
        # Insert predefined habits
        c.execute("INSERT INTO habits VALUES (?, ?, ?)", ("Drink water", "daily", "2024-03-01T08:00:00"))
        c.execute("INSERT INTO habits VALUES (?, ?, ?)", ("Exercise", "daily", "2024-03-01T09:00:00"))
        c.execute("INSERT INTO habits VALUES (?, ?, ?)", ("Read a book", "daily", "2024-03-01T20:00:00"))
        c.execute("INSERT INTO habits VALUES (?, ?, ?)", ("Grocery shopping", "weekly", "2024-03-01T12:00:00"))
        c.execute("INSERT INTO habits VALUES (?, ?, ?)", ("Call parents", "weekly", "2024-03-01T18:00:00"))
        print("✅ Predefined habits inserted.")

    conn.commit()
    conn.close()

def insert_habit(habit):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('INSERT INTO habits VALUES (?, ?, ?)',
              (habit.name, habit.periodicity, habit.created_at.isoformat()))
    conn.commit()
    conn.close()

def insert_checkoff(habit_name, timestamp):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('INSERT INTO checkoffs VALUES (?, ?)',
              (habit_name, timestamp.isoformat()))
    conn.commit()
    conn.close()

def load_all_habits():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('SELECT name, periodicity, created_at FROM habits')
    rows = c.fetchall()
    conn.close()
    return [Habit(name, periodicity, datetime.fromisoformat(created_at)) for name, periodicity, created_at in rows]

def get_checkoffs_for_habit(name):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('SELECT timestamp FROM checkoffs WHERE habit_name = ?', (name,))
    rows = c.fetchall()
    conn.close()
    return [datetime.fromisoformat(row[0]) for row in rows]



