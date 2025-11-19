import sqlite3

def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        gender TEXT,
        height REAL,
        current_weight REAL,
        target_weight REAL,
        activity_level TEXT,
        fitness_goal TEXT,
        equipment TEXT,
        workout_plan TEXT,
        predicted_weeks REAL
    )
    """)
    conn.commit()
    conn.close()

def save_user_data(data):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO users (
            name, age, gender, height, current_weight, target_weight,
            activity_level, fitness_goal, equipment, workout_plan, predicted_weeks
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data["name"], data["age"], data["gender"], data["height"],
        data["current_weight"], data["target_weight"], data["activity_level"],
        data["fitness_goal"], data["equipment"], data["workout_plan"],
        data["predicted_weeks"]
    ))
    conn.commit()
    conn.close()
