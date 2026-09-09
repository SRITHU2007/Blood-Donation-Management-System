import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# ----------------------------
# Load Gemini API
# ----------------------------
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("❌ Gemini API Key not found. Please create a .env file and add your API key.")
    st.stop()

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")


# ----------------------------
# Chatbot Screen
# ----------------------------
def show_chatbot():

    if st.button("⬅ Back to Home"):
        st.session_state.page = "Home"
        st.rerun()

    st.title("🤖 AI Blood Donation Chatbot")

    st.write(
        "Ask questions about blood donation, blood groups, eligibility, "
        "blood inventory, or emergency blood requests."
    )

    # Chat History
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display Chat History
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # User Input
    prompt = st.chat_input("Ask your question...")

    if prompt:

        # Show user message
        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        with st.chat_message("user"):
            st.markdown(prompt)

        # Generate Gemini Response
        try:
            response = model.generate_content(prompt)

            if hasattr(response, "text"):
                answer = response.text
            else:
                answer = "Sorry, I couldn't generate a response."

        except Exception as e:
            answer = f"❌ Error: {str(e)}"

        # Show assistant response
        with st.chat_message("assistant"):
            st.markdown(answer)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )