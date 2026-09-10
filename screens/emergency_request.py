import streamlit as st
import asyncio
import ast

from client.mcp_client import call_mcp


# ---------------- MCP FUNCTIONS ----------------

async def check_blood_availability(blood_group):
    result = await call_mcp(
        "blood_availability",
        {
            "blood_group": blood_group
        }
    )

    return ast.literal_eval(result.content[0].text)


async def get_matching_donors_mcp(blood_group):
    result = await call_mcp(
        "matching_donors",
        {
            "blood_group": blood_group
        }
    )

    return ast.literal_eval(result.content[0].text)


# ---------------- STREAMLIT ----------------

def show_emergency_request():

    if st.button("⬅ Back to Home"):
        st.session_state.page = "Home"
        st.rerun()

    st.title("🚨 Emergency Blood Request")

    patient_name = st.text_input("Patient Name")

    blood_group = st.selectbox(
        "Required Blood Group",
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

    required_units = st.number_input(
        "Required Units",
        min_value=1,
        step=1
    )

    if st.button("Check Availability"):

        try:

            available_units = asyncio.run(
                check_blood_availability(blood_group)
            )

            if available_units >= required_units:

                st.success(
                    f"✅ Blood Available!\n\n"
                    f"{available_units} units of {blood_group} are available."
                )

            else:

                st.error(
                    f"❌ Only {available_units} units of {blood_group} are available."
                )

                st.subheader("🩸 Matching Donors")

                donors = asyncio.run(
                    get_matching_donors_mcp(blood_group)
                )

                if donors:

                    st.table(donors)

                    if st.button("🏥 View Nearby Hospitals"):
                        st.session_state.page = "Nearby Hospitals"
                        st.rerun()

                else:
                    st.warning("No matching donors found.")

        except Exception as e:
            st.error(f"❌ {e}")