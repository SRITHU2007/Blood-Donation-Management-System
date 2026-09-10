import sqlite3

DATABASE_NAME = "blood.db"


def get_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # ---------------- Donors ----------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS donors (
        donor_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        gender TEXT,
        blood_group TEXT,
        phone TEXT,
        email TEXT,
        location TEXT,
        last_donation_date TEXT
    )
    """)

    # ---------------- Blood Inventory ----------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS blood_inventory (
        blood_group TEXT PRIMARY KEY,
        units_available INTEGER DEFAULT 0
    )
    """)

    # Insert default blood groups
    blood_groups = [
        "A+","A-",
        "B+","B-",
        "AB+","AB-",
        "O+","O-"
    ]

    for group in blood_groups:
        cursor.execute("""
        INSERT OR IGNORE INTO blood_inventory
        (blood_group, units_available)
        VALUES (?, ?)
        """, (group, 0))

    # ---------------- Hospitals ----------------
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


if __name__ == "__main__":
    create_tables()
    print("Database created successfully.")