import sqlite3

DATABASE_NAME = "blood.db"


def get_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # Donors Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS donors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        gender TEXT,
        blood_group TEXT,
        phone TEXT,
        email TEXT,
        location TEXT,
        last_donation_date TEXT
    )
    """)

    # Blood Inventory Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS blood_inventory (
        blood_group TEXT PRIMARY KEY,
        units_available INTEGER
    )
    """)

    # Hospitals Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS hospitals (
        hospital_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        location TEXT,
        phone TEXT
    )
    """)

    conn.commit()
    conn.close()