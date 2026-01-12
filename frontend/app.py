import streamlit as st
from utils import make_authenticated_request

from components.navbar import render_navbar

# Page configuration
st.set_page_config(page_title="BLR Riders", layout="wide", page_icon="🏍️")

# Render Top Navbar
render_navbar()

# Session state initialization
if 'token' not in st.session_state:
    st.session_state.token = None
    st.session_state.user = None

def login():
    with st.form("login_form"):
        st.subheader("Login")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")
        
        if submit:
            response = make_authenticated_request(
                'POST', 
                '/api/v1/auth/login',
                data={"username": email, "password": password}
            )
            if response and response.status_code == 200:
                data = response.json()
                st.session_state.token = data.get('access_token')
                st.session_state.user = email
                st.success("Successfully logged in!")
                st.rerun()
            else:
                st.error("Login failed. Please check your credentials.")

def register():
    with st.form("register_form"):
        st.subheader("Register New User")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        submit = st.form_submit_button("Register")
        
        if submit:
            if password != confirm_password:
                st.error("Passwords do not match!")
                return
                
            response = make_authenticated_request(
                'POST', 
                '/api/v1/auth/register',
                data={"email": email, "password": password}
            )
            if response and response.status_code == 200:
                st.success("Successfully registered! Please login.")
            else:
                st.error("Registration failed.")

def logout():
    st.session_state.token = None
    st.session_state.user = None
    st.success("Successfully logged out!")
    st.rerun()

def main():
    st.title("🏍️ BLR Riders - Home")
    
    if st.session_state.token:
        st.success(f"Welcome back, {st.session_state.user}!")
        st.info("Use the sidebar functionality to explore Rides, Learning, and the Chatbot.")
        
        # Logout logic is now handled in the Navbar
        st.info("Explore features using the top navigation bar.")
            
    else:
        tab1, tab2 = st.tabs(["Login", "Register"])
        
        with tab1:
            login()
        
        with tab2:
            register()

if __name__ == "__main__":
    main()