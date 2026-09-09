import streamlit as st
import pandas as pd
import asyncio
import ast

from client.mcp_client import mcp_client


async def load_inventory():
    async with mcp_client:
        result = await mcp_client.call_tool(
            "view_inventory",
            {}
        )
        return ast.literal_eval(result.content[0].text)


async def update_units(blood_group, units):
    async with mcp_client:
        await mcp_client.call_tool(
            "update_blood_inventory",
            {
                "blood_group": blood_group,
                "units": units
            }
        )


def show_blood_inventory():

    # Back Button
    if st.button("⬅ Back to Home"):
        st.session_state.page = "Home"
        st.rerun()

    st.title("🩸 Blood Inventory")

    try:
        inventory = asyncio.run(load_inventory())
    except Exception as e:
        st.error(f"Error: {e}")
        return

    if inventory:

        data = []

        for blood_group, units in inventory:

            if units >= 10:
                status = "🟢 Good"
            elif units >= 5:
                status = "🟡 Low"
            else:
                status = "🔴 Critical"

            data.append([
                blood_group,
                units,
                status
            ])

        df = pd.DataFrame(
            data,
            columns=[
                "Blood Group",
                "Units Available",
                "Status"
            ]
        )

        st.dataframe(
            df,
            use_container_width=True
        )

    else:
        st.warning("No inventory available.")

    st.divider()

    st.subheader("✏ Update Inventory")

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
        "Units Available",
        min_value=0,
        step=1
    )

    if st.button("Update Inventory"):

        try:
            asyncio.run(update_units(blood_group, units))
            st.success("✅ Inventory updated successfully!")
            st.rerun()

        except Exception as e:
            st.error(f"Error: {e}")