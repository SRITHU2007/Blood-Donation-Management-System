import streamlit as st

from database import create_tables

create_tables()

from screens.home import show_home
from screens.add_donor import show_add_donor
from screens.view_donors import show_view_donors
from screens.blood_inventory import show_blood_inventory
from screens.emergency_request import show_emergency_request
from screens.hospital_management import show_hospital_management
from screens.nearby_hospitals import show_nearby_hospitals
from screens.chatbot import show_chatbot

import streamlit as st

st.set_page_config(
    page_title="Blood Donation Management System",
    page_icon="🩸",
    layout="wide"
)

if "page" not in st.session_state:
    st.session_state.page = "Home"

page = st.session_state.page

if page == "Home":
    show_home()

elif page == "Add Donor":
    show_add_donor()

elif page == "View Donors":
    show_view_donors()

elif page == "Blood Inventory":
    show_blood_inventory()

elif page == "Emergency Request":
    show_emergency_request()

elif page == "Hospital Management":
    show_hospital_management()

elif page == "Nearby Hospitals":
    show_nearby_hospitals()

elif page == "Chatbot":
    show_chatbot()