import streamlit as st
import asyncio
from client.mcp_client import mcp_client


def show_add_donor():

    if st.button("⬅ Back to Home"):
        st.session_state.page = "Home"
        st.rerun()

    st.title("➕ Add Donor")

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
        ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
    )

    phone = st.text_input("Phone Number")
    email = st.text_input("Email")
    location = st.text_input("Location")
    last_donation = st.date_input("Last Donation Date")

    if st.button("Register Donor"):

        async def register():
            await mcp_client.call_tool(
                "register_donor",
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
            asyncio.run(register())
            st.success("✅ Donor Registered Successfully!")

        except Exception as e:
            st.error(f"Error: {e}")