import streamlit as st

from database import create_tables

from screens.home import show_home
from screens.add_donor import show_add_donor
from screens.view_donors import show_view_donors
from screens.blood_inventory import show_blood_inventory
from screens.emergency_request import show_emergency_request
from screens.hospital_management import show_hospital_management
from screens.nearby_hospitals import show_nearby_hospitals
from screens.chatbot import show_chatbot


# Create Database Tables
create_tables()


# Streamlit Configuration
st.set_page_config(
    page_title="Blood Donation Management System",
    page_icon="🩸",
    layout="wide"
)
st.markdown("""
<style>

/* Background */
.stApp{
    background: linear-gradient(
        135deg,
        #FFE5E5,
        #FDECEC,
        #FFF7F7
    );
}

/* Main Content Glass Card */
.block-container{
    background: rgba(255,255,255,0.35);
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
    border-radius:20px;
    padding:2rem;
    border:1px solid rgba(255,255,255,0.4);
    box-shadow:0 8px 32px rgba(0,0,0,0.15);
}

/* Sidebar */
[data-testid="stSidebar"]{
    background: rgba(255,255,255,0.55);
    backdrop-filter: blur(15px);
}

/* Buttons */
.stButton>button{
    width:100%;
    height:55px;
    border:none;
    border-radius:15px;
    font-size:17px;
    font-weight:bold;
    background:linear-gradient(90deg,#E53935,#D32F2F);
    color:white;
    transition:0.3s;
}

.stButton>button:hover{
    transform:translateY(-2px);
    box-shadow:0 8px 20px rgba(229,57,53,.4);
}

/* Metrics */
[data-testid="metric-container"]{
    background:rgba(255,255,255,0.45);
    border-radius:18px;
    padding:20px;
    box-shadow:0 8px 25px rgba(0,0,0,.08);
    border:1px solid rgba(255,255,255,.3);
}

/* DataFrames */
[data-testid="stDataFrame"]{
    border-radius:15px;
}

/* Chat messages */
.stChatMessage{
    border-radius:15px;
    background:rgba(255,255,255,.35);
    margin-bottom:10px;
}

/* Input */
.stTextInput input{
    border-radius:12px;
}

</style>
""", unsafe_allow_html=True)


# Navigation State
if "page" not in st.session_state:
    st.session_state.page = "Home"


page = st.session_state.page


# Routing
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
    
elif page == "AI Chatbot":
    show_chatbot()

else:
    st.session_state.page = "Home"
    st.rerun()
    
st.divider()

st.markdown(
"""
<div style="text-align:center;color:gray;">
© 2026 LifeBlood AI • Developed using Streamlit, Gemini AI & MCP
</div>
""",
unsafe_allow_html=True
)