from database import get_connection


def get_inventory():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT blood_group, units_available
        FROM blood_inventory
        ORDER BY blood_group
    """)

    inventory = cursor.fetchall()

    conn.close()

    return inventory


def update_inventory(blood_group, units):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE blood_inventory
        SET units_available = ?
        WHERE blood_group = ?
    """, (units, blood_group))

    conn.commit()
    conn.close()


def check_availability(blood_group):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT units_available
        FROM blood_inventory
        WHERE blood_group = ?
    """, (blood_group,))

    result = cursor.fetchone()

    conn.close()

    if result:
        return result[0]

    return 0