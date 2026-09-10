import streamlit as st
import pandas as pd
import asyncio
import ast

from client.mcp_client import call_mcp


# ---------------- MCP FUNCTIONS ----------------

async def add_hospital_async(name, location, phone):
    await call_mcp(
        "add_hospital_tool",
        {
            "name": name,
            "location": location,
            "phone": phone
        }
    )


async def get_all_hospitals_async():
    result = await call_mcp(
        "view_hospitals",
        {}
    )
    return ast.literal_eval(result.content[0].text)


async def search_hospitals_async(location):
    result = await call_mcp(
        "search_hospital",
        {
            "location": location
        }
    )
    return ast.literal_eval(result.content[0].text)


async def get_hospital_by_id_async(hospital_id):
    result = await call_mcp(
        "hospital_details",
        {
            "hospital_id": hospital_id
        }
    )
    return ast.literal_eval(result.content[0].text)


async def update_hospital_async(hospital_id, name, location, phone):
    await call_mcp(
        "edit_hospital",
        {
            "hospital_id": hospital_id,
            "name": name,
            "location": location,
            "phone": phone
        }
    )


async def delete_hospital_async(hospital_id):
    await call_mcp(
        "remove_hospital",
        {
            "hospital_id": hospital_id
        }
    )


# ---------------- STREAMLIT UI ----------------

def show_hospital_management():

    if st.button("⬅ Back to Home"):
        st.session_state.page = "Home"
        st.rerun()

    st.title("🏥 Hospital Management")

    # ---------------- Add Hospital ----------------

    st.subheader("➕ Add Hospital")

    name = st.text_input("Hospital Name")
    location = st.text_input("Location")
    phone = st.text_input("Phone Number")

    if st.button("Add Hospital"):

        if name and location and phone:

            try:
                asyncio.run(
                    add_hospital_async(
                        name,
                        location,
                        phone
                    )
                )

                st.success("✅ Hospital Added Successfully!")
                st.rerun()

            except Exception as e:
                st.error(f"❌ {e}")

        else:
            st.warning("Please fill all fields.")

    st.divider()

    # ---------------- Search ----------------

    st.subheader("🔍 Search Hospitals")

    search_location = st.text_input("Search by Location")

    try:

        if st.button("Search Hospitals"):
            hospitals = asyncio.run(
                search_hospitals_async(search_location)
            )
        else:
            hospitals = asyncio.run(
                get_all_hospitals_async()
            )

    except Exception as e:
        st.error(f"❌ {e}")
        hospitals = []

    if hospitals:

        df = pd.DataFrame(
            hospitals,
            columns=[
                "Hospital ID",
                "Hospital Name",
                "Location",
                "Phone"
            ]
        )

        st.dataframe(
            df,
            use_container_width=True
        )

    else:
        st.warning("No hospitals found.")

    st.divider()

    # ---------------- Delete ----------------

    st.subheader("🗑 Delete Hospital")

    delete_id = st.number_input(
        "Hospital ID",
        min_value=1,
        step=1,
        key="delete"
    )

    if st.button("Delete Hospital"):

        try:

            asyncio.run(
                delete_hospital_async(delete_id)
            )

            st.success("✅ Hospital Deleted Successfully!")
            st.rerun()

        except Exception as e:
            st.error(f"❌ {e}")

    st.divider()

    # ---------------- Edit ----------------

    st.subheader("✏ Edit Hospital")

    edit_id = st.number_input(
        "Hospital ID to Edit",
        min_value=1,
        step=1,
        key="edit"
    )

    if st.button("Load Hospital"):

        try:

            hospital = asyncio.run(
                get_hospital_by_id_async(edit_id)
            )

            if hospital:
                st.session_state["edit_hospital"] = hospital
            else:
                st.error("Hospital not found.")

        except Exception as e:
            st.error(f"❌ {e}")

    if "edit_hospital" in st.session_state:

        hospital = st.session_state["edit_hospital"]

        hospital_name = st.text_input(
            "Hospital Name",
            value=hospital[1]
        )

        hospital_location = st.text_input(
            "Location",
            value=hospital[2]
        )

        hospital_phone = st.text_input(
            "Phone Number",
            value=hospital[3]
        )

        if st.button("Update Hospital"):

            try:

                asyncio.run(
                    update_hospital_async(
                        hospital[0],
                        hospital_name,
                        hospital_location,
                        hospital_phone
                    )
                )

                st.success("✅ Hospital Updated Successfully!")

                del st.session_state["edit_hospital"]

                st.rerun()

            except Exception as e:
                st.error(f"❌ {e}")