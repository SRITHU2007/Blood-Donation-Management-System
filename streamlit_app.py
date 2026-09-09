import streamlit as st
from database import get_connection

st.set_page_config(
    page_title="Blood Donation Management System",
    page_icon="🩸",
    layout="wide"
)

# ---------------- Session ----------------

if "page" not in st.session_state:
    st.session_state.page = "Home"

# ---------------- HOME ----------------

# ---------------- HOME ----------------

if st.session_state.page == "Home":

    st.title("🩸 Blood Donation Management System")
    st.markdown("### Welcome!")
    st.write("Choose an option below.")

    # -------- Row 1 --------
    col1, col2 = st.columns(2)

    with col1:
        if st.button("➕ Add Donor", use_container_width=True):
            st.session_state.page = "Add Donor"
            st.rerun()

    with col2:
        if st.button("👥 View Donors", use_container_width=True):
            st.session_state.page = "View Donors"
            st.rerun()

    st.write("")

    # -------- Row 2 --------
    col3, col4 = st.columns(2)

    with col3:
        if st.button("🩸 Blood Inventory", use_container_width=True):
            st.session_state.page = "Blood Inventory"
            st.rerun()

    with col4:
        if st.button("🚨 Emergency Request", use_container_width=True):
            st.session_state.page = "Emergency Request"
            st.rerun()

    st.write("")

    # -------- Row 3 --------
    col5, col6 = st.columns(2)

    with col5:
        if st.button("🏥 Hospital Management", use_container_width=True):
            st.session_state.page = "Hospital Management"
            st.rerun()

    with col6:
        if st.button("🗺️ Nearby Hospitals", use_container_width=True):
            st.session_state.page = "Nearby Hospitals"
            st.rerun()

# ---------------- ADD DONOR ----------------

elif st.session_state.page == "Add Donor":

    if st.button("⬅ Back to Home"):
        st.session_state.page = "Home"
        st.rerun()

    st.header("➕ Register New Donor")

    name = st.text_input("Name")

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=65
    )

    gender = st.selectbox(
        "Gender",
        ["Male", "Female", "Other"]
    )

    blood_group = st.selectbox(
        "Blood Group",
        [
            "A+",
            "A-",
            "B+",
            "B-",
            "AB+",
            "AB-",
            "O+",
            "O-"
        ]
    )

    phone = st.text_input("Phone Number")

    email = st.text_input("Email")

    location = st.text_input("Location")

    last_donation = st.date_input(
        "Last Donation Date"
    )

    if st.button("Register Donor"):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO donors
        (name, age, gender, blood_group,
        phone, email, location,
        last_donation_date)

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

        st.success("✅ Donor Registered Successfully!")

# ---------------- VIEW DONORS ----------------

elif st.session_state.page == "View Donors":

    if st.button("⬅ Back to Home"):
        st.session_state.page = "Home"
        st.rerun()

    st.header("👥 Registered Donors")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
    donor_id,
    name,
    age,
    gender,
    blood_group,
    phone,
    email,
    location,
    last_donation_date
    FROM donors
    ORDER BY donor_id DESC
    """)

    donors = cursor.fetchall()

    conn.close()

    if donors:

        st.dataframe(
            donors,
            use_container_width=True
        )

    else:

        st.info("No donors registered yet.")

# ---------------- BLOOD INVENTORY ----------------

elif st.session_state.page == "Blood Inventory":

    if st.button("⬅ Back to Home"):
        st.session_state.page = "Home"
        st.rerun()

    st.header("🩸 Blood Inventory")

    blood_group = st.selectbox(
        "Blood Group",
        [
            "A+",
            "A-",
            "B+",
            "B-",
            "AB+",
            "AB-",
            "O+",
            "O-"
        ]
    )

    units = st.number_input(
        "Available Units",
        min_value=0,
        step=1
    )

    if st.button("Update Inventory"):

        conn = get_connection()
        cursor = conn.cursor()

        # Check whether the blood group already exists
        cursor.execute(
            "SELECT inventory_id FROM blood_inventory WHERE blood_group=?",
            (blood_group,)
        )

        existing = cursor.fetchone()

        if existing:

            cursor.execute("""
                UPDATE blood_inventory
                SET units_available=?
                WHERE blood_group=?
            """, (units, blood_group))

        else:

            cursor.execute("""
                INSERT INTO blood_inventory
                (blood_group, units_available)
                VALUES (?, ?)
            """, (blood_group, units))

        conn.commit()
        conn.close()

        st.success("✅ Inventory Updated Successfully!")

    st.subheader("Current Blood Inventory")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
        blood_group,
        units_available
        FROM blood_inventory
        ORDER BY blood_group
    """)

    inventory = cursor.fetchall()

    conn.close()

    if inventory:

        st.dataframe(
            inventory,
            use_container_width=True
        )

    else:

        st.info("No blood inventory available.")      
# ---------------- EMERGENCY REQUEST ----------------

elif st.session_state.page == "Emergency Request":

    if st.button("⬅ Back to Home"):
        st.session_state.page = "Home"
        st.rerun()

    st.header("🚨 Emergency Blood Request")

    patient_name = st.text_input("Patient Name")

    required_group = st.selectbox(
        "Required Blood Group",
        [
            "A+",
            "A-",
            "B+",
            "B-",
            "AB+",
            "AB-",
            "O+",
            "O-"
        ]
    )

    required_units = st.number_input(
        "Required Units",
        min_value=1,
        step=1
    )

    if st.button("Check Availability"):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT units_available
            FROM blood_inventory
            WHERE blood_group=?
        """, (required_group,))

        result = cursor.fetchone()

        if result:

            available = result[0]

            st.subheader("Result")

            if available >= required_units:

                st.success(
                    f"✅ Blood Available!\n\n"
                    f"Patient: {patient_name}\n\n"
                    f"Blood Group: {required_group}\n\n"
                    f"Available Units: {available}"
                )

            else:

                st.warning(
                    f"⚠️ Only {available} unit(s) available."
                )

                st.subheader("Matching Donors")

                cursor.execute("""
                    SELECT
                    name,
                    phone,
                    location
                    FROM donors
                    WHERE blood_group=?
                """, (required_group,))

                donors = cursor.fetchall()

                if donors:

                    st.dataframe(
                        donors,
                        use_container_width=True
                    )

                else:

                    st.error(
                        "No matching donors found."
                    )

        else:

            st.error(
                "Blood group not available in inventory."
            )

        conn.close()
        
# ---------------- NEARBY HOSPITALS ----------------

elif st.session_state.page == "Nearby Hospitals":

    if st.button("⬅ Back to Home"):
        st.session_state.page = "Home"
        st.rerun()

    st.header("🏥 Nearby Hospitals")

    st.write("Hospitals with current blood requirements")

    import pandas as pd

    hospitals = pd.DataFrame({
        "Hospital": [
            "Apollo Hospital",
            "Yashoda Hospital",
            "Care Hospital",
            "KIMS Hospital",
            "AIG Hospital"
        ],
        "Blood Group": [
            "B+",
            "O+",
            "A-",
            "AB+",
            "O-"
        ],
        "Units Needed": [
            3,
            5,
            2,
            1,
            4
        ],
        "Latitude": [
            17.4375,
            17.4416,
            17.4250,
            17.4430,
            17.4485
        ],
        "Longitude": [
            78.4483,
            78.3910,
            78.4510,
            78.3772,
            78.3648
        ]
    })

    st.subheader("Hospital Requirements")

    st.dataframe(
        hospitals[
            [
                "Hospital",
                "Blood Group",
                "Units Needed"
            ]
        ],
        use_container_width=True
    )

    st.subheader("Hospital Locations")

    st.map(
        hospitals.rename(
            columns={
                "Latitude": "lat",
                "Longitude": "lon"
            }
        )
    )