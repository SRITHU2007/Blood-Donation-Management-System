from database import get_connection
from database import get_connection

conn = get_connection()
cursor = conn.cursor()

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
cursor.execute("""
CREATE TABLE IF NOT EXISTS blood_inventory (
    inventory_id INTEGER PRIMARY KEY AUTOINCREMENT,
    blood_group TEXT NOT NULL,
    units_available INTEGER NOT NULL,
    last_updated TEXT
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS emergency_requests (
    request_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_name TEXT NOT NULL,
    blood_group TEXT NOT NULL,
    units_required INTEGER,
    hospital_name TEXT,
    location TEXT,
    status TEXT
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS notifications (
    notification_id INTEGER PRIMARY KEY AUTOINCREMENT,
    donor_id INTEGER,
    message TEXT,
    sent_time TEXT,
    status TEXT,
    FOREIGN KEY (donor_id) REFERENCES donors(donor_id)
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS hospitals (
    hospital_id INTEGER PRIMARY KEY AUTOINCREMENT,
    hospital_name TEXT NOT NULL,
    location TEXT NOT NULL,
    latitude REAL,
    longitude REAL,
    blood_group TEXT NOT NULL,
    units_needed INTEGER NOT NULL
)
""")
conn.commit()
conn.close()

print("Donors table created successfully!")