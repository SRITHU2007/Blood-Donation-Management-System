from database import get_connection


def add_hospital(name, location, phone):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO hospitals
        (
            name,
            location,
            phone
        )
        VALUES (?, ?, ?)
    """, (
        name,
        location,
        phone
    ))

    conn.commit()
    conn.close()


def get_all_hospitals():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM hospitals
    """)

    hospitals = cursor.fetchall()

    conn.close()

    return hospitals


def search_hospitals(location):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM hospitals
        WHERE location LIKE ?
    """, (f"%{location}%",))

    hospitals = cursor.fetchall()

    conn.close()

    return hospitals


def get_hospital_by_id(hospital_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM hospitals
        WHERE hospital_id = ?
    """, (hospital_id,))

    hospital = cursor.fetchone()

    conn.close()

    return hospital


def update_hospital(hospital_id, name, location, phone):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE hospitals
        SET
            name = ?,
            location = ?,
            phone = ?
        WHERE hospital_id = ?
    """, (
        name,
        location,
        phone,
        hospital_id
    ))

    conn.commit()
    conn.close()


def delete_hospital(hospital_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM hospitals
        WHERE hospital_id = ?
    """, (hospital_id,))

    conn.commit()
    conn.close()