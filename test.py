from database import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute("""
INSERT INTO donors
(name, age, gender, blood_group, phone, email, location, last_donation_date)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", (
    "Rahul",
    25,
    "Male",
    "O+",
    "9876543210",
    "rahul@gmail.com",
    "Hyderabad",
    "2025-01-01"
))

conn.commit()

cursor.execute("SELECT * FROM donors")
print(cursor.fetchall())

conn.close()