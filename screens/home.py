import streamlit as st
from services.dashboard_service import get_dashboard_stats

def show_home():

    total_donors, total_hospitals, total_units = get_dashboard_stats()

    st.markdown("""
    <style>

    .stApp{
        background: linear-gradient(135deg,#edf6ff,#dbeafe,#fdf2f8);
        background-attachment:fixed;
    }

    #MainMenu{visibility:hidden;}
    footer{visibility:hidden;}
    header{visibility:hidden;}

    .block-container{
        padding-top:2rem;
        padding-bottom:2rem;
    }

    .title{
        text-align:center;
        font-size:55px;
        font-weight:800;
        color:#C62828;
        margin-bottom:10px;
    }

    .subtitle{
        text-align:center;
        color:#555;
        font-size:20px;
        margin-bottom:40px;
    }

    .glass{
        background:rgba(255,255,255,0.45);
        backdrop-filter:blur(18px);
        border-radius:25px;
        padding:25px;
        box-shadow:0 8px 30px rgba(0,0,0,.15);
        border:1px solid rgba(255,255,255,.4);
    }

    .card{
        background:white;
        border-radius:20px;
        padding:25px;
        text-align:center;
        box-shadow:0 8px 20px rgba(0,0,0,.12);
        transition:.3s;
    }

    .card:hover{
        transform:translateY(-8px);
        box-shadow:0 18px 35px rgba(0,0,0,.2);
    }

    .number{
        font-size:42px;
        color:#E53935;
        font-weight:bold;
    }

    .label{
        color:#666;
        font-size:18px;
    }

    div.stButton>button{
        width:100%;
        height:65px;
        border:none;
        border-radius:18px;
        background:linear-gradient(90deg,#ff416c,#ff4b2b);
        color:white;
        font-size:18px;
        font-weight:bold;
        transition:0.3s;
    }

    div.stButton>button:hover{
        transform:scale(1.03);
        box-shadow:0 12px 25px rgba(255,75,43,.35);
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='title'>🩸 Blood Donation Management System</div>", unsafe_allow_html=True)

    st.markdown("<div class='subtitle'>Smart Blood Bank & Hospital Management Platform</div>", unsafe_allow_html=True)

    st.markdown("<div class='glass'>", unsafe_allow_html=True)

    st.subheader("📊 Dashboard")

    col1,col2,col3=st.columns(3)

    with col1:
        st.markdown(f"""
        <div class="card">
            <h2>👥</h2>
            <div class="number">{total_donors}</div>
            <div class="label">Total Donors</div>
        </div>
        """,unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="card">
            <h2>🏥</h2>
            <div class="number">{total_hospitals}</div>
            <div class="label">Hospitals</div>
        </div>
        """,unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="card">
            <h2>🩸</h2>
            <div class="number">{total_units}</div>
            <div class="label">Blood Units</div>
        </div>
        """,unsafe_allow_html=True)

    st.markdown("<br>",unsafe_allow_html=True)

    st.subheader("🚀 Quick Access")
    # ---------------- Row 1 ----------------

col1, col2 = st.columns(2)

with col1:
    if st.button("➕ Add Donor"):
        st.session_state.page = "Add Donor"
        st.rerun()

with col2:
    if st.button("👥 View Donors"):
        st.session_state.page = "View Donors"
        st.rerun()

st.write("")

# ---------------- Row 2 ----------------

col3, col4 = st.columns(2)

with col3:
    if st.button("🩸 Blood Inventory"):
        st.session_state.page = "Blood Inventory"
        st.rerun()

with col4:
    if st.button("🚨 Emergency Request"):
        st.session_state.page = "Emergency Request"
        st.rerun()

st.write("")

# ---------------- Row 3 ----------------

col5, col6 = st.columns(2)

with col5:
    if st.button("🏥 Hospital Management"):
        st.session_state.page = "Hospital Management"
        st.rerun()

with col6:
    if st.button("🗺️ Nearby Hospitals"):
        st.session_state.page = "Nearby Hospitals"
        st.rerun()

st.write("")

# ---------------- Row 4 ----------------

col7, col8 = st.columns(2)

with col7:
    if st.button("🤖 AI Chatbot"):
        st.session_state.page = "Chatbot"
        st.rerun()

with col8:
    st.markdown("""
    <div style="
        background:white;
        border-radius:20px;
        padding:25px;
        text-align:center;
        box-shadow:0 8px 20px rgba(0,0,0,.12);
        height:110px;
    ">
        <h3 style="color:#E53935;">❤️ Save Lives</h3>
        <p>Every donation can save up to three lives.</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<div style="
    background:rgba(255,255,255,0.45);
    backdrop-filter:blur(15px);
    border-radius:25px;
    padding:35px;
    text-align:center;
    box-shadow:0 8px 25px rgba(0,0,0,.15);
">

<h2 style="color:#E53935;">
❤️ Donate Blood, Save Lives
</h2>

<p style="font-size:18px;color:#444;">
Every blood donation has the power to save up to <b>three lives</b>.
Our Blood Donation Management System helps connect donors,
hospitals, and patients quickly during emergencies.
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div style="
text-align:center;
color:#666;
font-size:15px;
">

<hr>

Made with ❤️ using <b>Streamlit</b>, <b>SQLite</b>,
<b>Gemini AI</b>, and <b>MCP Servers</b>

<br><br>

© 2026 Blood Donation Management System

</div>
""", unsafe_allow_html=True)

# Close the glass container started in Part 1
st.markdown("</div>", unsafe_allow_html=True)