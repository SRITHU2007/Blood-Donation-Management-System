from database import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute("SELECT * FROM donors")

for donor in cursor.fetchall():
    print(donor)

conn.close()