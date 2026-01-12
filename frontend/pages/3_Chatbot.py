import streamlit as st
import sys
import os

# Add parent directory to path to import utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import make_authenticated_request
from components.navbar import render_navbar

st.set_page_config(page_title="AI Assistant", page_icon="🤖")
render_navbar()

st.title("🤖 AI Ride Assistant")

if 'token' not in st.session_state or not st.session_state.token:
    st.warning("Please login from the Home page to access this feature.")
else:
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask me about rides, routes, or safety..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            response = make_authenticated_request("POST", "/api/v1/chatbot/message", data={"message": prompt})
            if response and response.status_code == 200:
                reply = response.json().get("response")
                st.markdown(reply)
                st.session_state.messages.append({"role": "assistant", "content": reply})
            else:
                st.error("Failed to get response from AI.")
