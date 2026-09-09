import streamlit as st
import pandas as pd
import asyncio
import ast

from client.mcp_client import mcp_client


# ---------------- MCP FUNCTIONS ----------------

async def load_donors():
    async with mcp_client:
        result = await mcp_client.call_tool("view_donors", {})
        return ast.literal_eval(result.content[0].text)


async def search_donor_data(blood_group, location):
    async with mcp_client:
        result = await mcp_client.call_tool(
        "search_donor",
        {
            "blood_group": blood_group,
            "location": location
        }
    )
    return ast.literal_eval(result.content[0].text)


async def remove_donor_data(donor_id):
    async with mcp_client:
        await mcp_client.call_tool(
        "remove_donor",
        {"donor_id": donor_id}
    )


async def donor_details(donor_id):
    async with mcp_client:
        result = await mcp_client.call_tool(
        "donor_details",
        {"donor_id": donor_id}
    )

    data = ast.literal_eval(result.content[0].text)

    if isinstance(data, tuple):
        data = list(data)

    return data


async def edit_donor_data(
    donor_id,
    name,
    age,
    gender,
    blood_group,
    phone,
    email,
    location,
):
    async with mcp_client:
        await mcp_client.call_tool(
            "edit_donor",
            {
                "donor_id": donor_id,
                "name": name,
                "age": age,
                "gender": gender,
                "blood_group": blood_group,
                "phone": phone,
                "email": email,
                "location": location
            }
        )


# ---------------- STREAMLIT ----------------

def show_view_donors():

    if st.button("⬅ Back to Home"):
        st.session_state.page = "Home"
        st.rerun()

    st.title("👥 Registered Donors")

    st.subheader("🔍 Search Donors")

    col1, col2 = st.columns(2)

    with col1:
        blood_group = st.selectbox(
            "Blood Group",
            ["", "A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
        )

    with col2:
        location = st.text_input("Location")

    try:

        if st.button("Search"):
            donors = asyncio.run(
                search_donor_data(blood_group, location)
            )
        else:
            donors = asyncio.run(load_donors())

    except Exception as e:
        st.error(e)
        return

    st.subheader("📋 Donor List")

    if donors:

        columns = [
            "ID",
            "Name",
            "Age",
            "Gender",
            "Blood Group",
            "Phone",
            "Email",
            "Location",
            "Last Donation"
        ]

        st.dataframe(
            pd.DataFrame(donors, columns=columns),
            use_container_width=True
        )

    else:
        st.warning("No donors found.")

    st.divider()

    st.subheader("🗑 Delete Donor")

    delete_id = st.number_input(
        "Donor ID",
        min_value=1,
        step=1
    )

    if st.button("Delete Donor"):

        try:
            asyncio.run(remove_donor_data(delete_id))
            st.success("Donor deleted successfully.")
            st.rerun()

        except Exception as e:
            st.error(e)

    st.divider()

    st.subheader("✏ Edit Donor")

    edit_id = st.number_input(
        "Donor ID to Edit",
        min_value=1,
        step=1,
        key="edit"
    )

    if st.button("Load Donor"):

        donor = asyncio.run(
            donor_details(edit_id)
        )

        if donor:
            st.session_state["edit_donor"] = donor
        else:
            st.error("Donor not found.")

    if "edit_donor" in st.session_state:

        donor = st.session_state["edit_donor"]

        name = st.text_input("Name", donor[1])

        age = st.number_input(
            "Age",
            18,
            65,
            donor[2]
        )

        genders = ["Male", "Female", "Other"]

        gender = st.selectbox(
            "Gender",
            genders,
            index=genders.index(donor[3])
        )

        blood_groups = [
            "A+","A-","B+","B-",
            "AB+","AB-","O+","O-"
        ]

        blood_group = st.selectbox(
            "Blood Group",
            blood_groups,
            index=blood_groups.index(donor[4])
        )

        phone = st.text_input("Phone", donor[5])
        email = st.text_input("Email", donor[6])
        location = st.text_input("Location", donor[7])

        if st.button("Update Donor"):

            try:

                asyncio.run(
                    edit_donor_data(
                        donor[0],
                        name,
                        age,
                        gender,
                        blood_group,
                        phone,
                        email,
                        location
                    )
                )

                st.success("Donor updated successfully.")

                del st.session_state["edit_donor"]

                st.rerun()

            except Exception as e:
                st.error(e)