from database import get_connection


def add_donor(name, age, gender, blood_group, phone, email, location, last_donation):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO donors
        (
            name,
            age,
            gender,
            blood_group,
            phone,
            email,
            location,
            last_donation_date
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        name,
        age,
        gender,
        blood_group,
        phone,
        email,
        location,
        str(last_donation)
    ))

    conn.commit()
    conn.close()


def get_all_donors():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM donors")
    donors = cursor.fetchall()

    conn.close()

    return donors


def get_matching_donors(blood_group):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT name, phone, location
        FROM donors
        WHERE blood_group = ?
    """, (blood_group,))

    donors = cursor.fetchall()

    conn.close()

    return donors

def search_donors(blood_group="", location=""):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
        SELECT *
        FROM donors
        WHERE 1=1
    """

    params = []

    if blood_group:
        query += " AND blood_group = ?"
        params.append(blood_group)

    if location:
        query += " AND location LIKE ?"
        params.append(f"%{location}%")

    cursor.execute(query, params)

    donors = cursor.fetchall()

    conn.close()

    return donors
def update_donor(donor_id, name, age, gender, blood_group, phone, email, location):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE donors
        SET
            name=?,
            age=?,
            gender=?,
            blood_group=?,
            phone=?,
            email=?,
            location=?
        WHERE donor_id=?
    """, (
        name,
        age,
        gender,
        blood_group,
        phone,
        email,
        location,
        donor_id
    ))

    conn.commit()
    conn.close()
    
def delete_donor(donor_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM donors WHERE donor_id=?",
        (donor_id,)
    )

    conn.commit()
    conn.close()

def get_donor_by_id(donor_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM donors WHERE donor_id = ?",
        (donor_id,)
    )

    donor = cursor.fetchone()

    conn.close()

    return donor