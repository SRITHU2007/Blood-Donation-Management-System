import streamlit as st
from services.dashboard_service import get_dashboard_stats


def show_home():

    # Get Dashboard Statistics
    total_donors, total_hospitals, total_units = get_dashboard_stats()

    # Title
    st.title("🩸 Blood Donation Management System")
    st.markdown("### Welcome!")

    # ---------------- Dashboard ----------------
    st.subheader("📊 Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="👥 Total Donors",
            value=total_donors
        )

    with col2:
        st.metric(
            label="🏥 Hospitals",
            value=total_hospitals
        )

    with col3:
        st.metric(
            label="🩸 Blood Units",
            value=total_units
        )

    st.divider()

    st.markdown("### Choose an Option")

    # ---------------- Row 1 ----------------
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

    # ---------------- Row 2 ----------------
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

       # ---------------- Row 3 ----------------
    col5, col6 = st.columns(2)

    with col5:
        if st.button("🏥 Hospital Management", use_container_width=True):
            st.session_state.page = "Hospital Management"
            st.rerun()

    with col6:
        if st.button("🗺️ Nearby Hospitals", use_container_width=True):
            st.session_state.page = "Nearby Hospitals"
            st.rerun()

    st.write("")

    # ---------------- Row 4 ----------------
    if st.button("🤖 AI Chatbot", use_container_width=True):
        st.session_state.page = "AI Chatbot"
        st.rerun()