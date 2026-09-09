import streamlit as st
import asyncio
import ast

from client.mcp_client import mcp_client


async def process_emergency_request(required_group, required_units):
    async with mcp_client:
        result = await mcp_client.call_tool(
            "process_request",
            {
                "blood_group": required_group,
                "required_units": required_units
            }
        )

        return ast.literal_eval(result.content[0].text)


async def get_matching_donors_mcp(required_group):
    async with mcp_client:
        result = await mcp_client.call_tool(
            "get_matching_donors",
            {
                "blood_group": required_group
            }
        )

        return ast.literal_eval(result.content[0].text)


def show_emergency_request():

    # Back Button
    if st.button("⬅ Back to Home"):
        st.session_state.page = "Home"
        st.rerun()

    st.title("🚨 Emergency Blood Request")

    patient_name = st.text_input("Patient Name")

    required_group = st.selectbox(
        "Required Blood Group",
        ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
    )

    required_units = st.number_input(
        "Required Units",
        min_value=1,
        step=1
    )

    if st.button("Check Availability"):

        try:
            available, units = asyncio.run(
                process_emergency_request(
                    required_group,
                    required_units
                )
            )

            if available:

                st.success(
                    f"✅ Blood Available!\n\n{units} units of {required_group} are available."
                )

            else:

                st.error(
                    f"❌ Only {units} units of {required_group} are available."
                )

                st.subheader("Matching Donors")

                donors = asyncio.run(
                    get_matching_donors_mcp(required_group)
                )

                if donors:
                    st.table(donors)

                    if st.button("🏥 View Nearby Hospitals"):
                        st.session_state.page = "Nearby Hospitals"
                        st.rerun()

                else:
                    st.warning("No matching donors found.")

        except Exception as e:
            st.error(f"Error: {e}")