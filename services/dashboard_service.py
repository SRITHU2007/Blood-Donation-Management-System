from database import get_connection


def get_dashboard_stats():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM donors")
    total_donors = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM hospitals")
    total_hospitals = cursor.fetchone()[0]

    cursor.execute("SELECT SUM(units_available) FROM blood_inventory")
    total_units = cursor.fetchone()[0] or 0

    conn.close()

    return total_donors, total_hospitals, total_units