import streamlit as st
import asyncio
from client.mcp_client import call_mcp


def show_add_donor():

    # Back Button
    if st.button("⬅ Back to Home"):
        st.session_state.page = "Home"
        st.rerun()

    st.title("➕ Add Donor")

    # Form Inputs
    name = st.text_input("Name")

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=65,
        value=18
    )

    gender = st.selectbox(
        "Gender",
        ["Male", "Female", "Other"]
    )

    blood_group = st.selectbox(
        "Blood Group",
        ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
    )

    phone = st.text_input("Phone Number")
    email = st.text_input("Email")
    location = st.text_input("Location")
    last_donation = st.date_input("Last Donation Date")

    # Register Button
    if st.button("Register Donor"):

        # Validation
        if not name.strip():
            st.warning("Please enter donor name.")
            return

        async def register():
            return await call_mcp(
                "register_donor_tool",
                {
                    "name": name,
                    "age": age,
                    "gender": gender,
                    "blood_group": blood_group,
                    "phone": phone,
                    "email": email,
                    "location": location,
                    "last_donation": str(last_donation)
                }
            )

        try:
            result = asyncio.run(register())

            st.success("✅ Donor Registered Successfully!")
            st.balloons()

            if result and hasattr(result, "content"):
                st.info(result.content[0].text)

        except Exception as e:
            st.error(f"❌ Error: {e}")