import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

from services.map_service import get_nearby_hospitals


def show_nearby_hospitals():

    # Back Button
    if st.button("⬅ Back to Home"):
        st.session_state.page = "Home"
        st.session_state.pop("hospitals", None)
        st.rerun()

    st.title("🗺️ Nearby Hospitals")

    city = st.text_input("Enter City")

    if st.button("Search Hospitals"):

        if not city.strip():
            st.warning("Please enter a city name.")
            return

        # Clear previous search
        st.session_state.pop("hospitals", None)

        with st.spinner("Searching hospitals..."):
            try:
                hospitals = get_nearby_hospitals(city)
                st.session_state["hospitals"] = hospitals
            except Exception as e:
                st.error(f"Error: {e}")
                return

    if "hospitals" not in st.session_state:
        return

    hospitals = st.session_state["hospitals"]

    if len(hospitals) == 0:
        st.warning("No hospitals found.")
        return

    first = hospitals[0]

    m = folium.Map(
        location=[float(first["lat"]), float(first["lon"])],
        zoom_start=12
    )

    table = []

    for hospital in hospitals[:30]:

        lat = float(hospital["lat"])
        lon = float(hospital["lon"])

        folium.Marker(
            [lat, lon],
            popup=hospital["display_name"],
            tooltip=hospital["display_name"]
        ).add_to(m)

        table.append({
            "Hospital": hospital["display_name"],
            "Latitude": lat,
            "Longitude": lon
        })

    st.subheader("📍 Hospital Locations")

    st_folium(
        m,
        width=900,
        height=500,
        key="hospital_map"
    )

    st.subheader(f"🏥 Hospitals Found ({len(hospitals)})")

    st.dataframe(
        pd.DataFrame(table),
        use_container_width=True
    )