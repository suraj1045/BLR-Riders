import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API configuration
API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")

# Page configuration
st.set_page_config(page_title="BLR Riders - API Tester", layout="wide")

# Session state to store authentication status
if 'token' not in st.session_state:
    st.session_state.token = None
    st.session_state.user = None

def make_authenticated_request(method, endpoint, data=None):
    headers = {}
    if st.session_state.token:
        headers["Authorization"] = f"Bearer {st.session_state.token}"
    
    url = f"{API_BASE_URL}{endpoint}"
    
    try:
        if method == 'GET':
            response = requests.get(url, headers=headers)
        elif method == 'POST':
            response = requests.post(url, json=data, headers=headers)
        
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error: {str(e)}")
        if hasattr(e, 'response') and e.response:
            st.error(f"Response: {e.response.text}")
        return None

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
            if response:
                st.session_state.token = response.get('access_token')
                st.session_state.user = email
                st.success("Successfully logged in!")
                st.rerun()

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
            if response:
                st.success("Successfully registered! Please login.")

def user_profile():
    st.subheader("User Profile")
    if st.button("Get My Profile"):
        response = make_authenticated_request('GET', '/api/v1/auth/me')
        if response:
            st.json(response)

def health_check():
    st.subheader("Health Check")
    if st.button("Check API Health"):
        try:
            response = requests.get(f"{API_BASE_URL}/api/healthcheck")
            if response.status_code == 200:
                st.success(f"API is healthy: {response.json()}")
            else:
                st.error(f"API returned status code: {response.status_code}")
        except Exception as e:
            st.error(f"Error connecting to API: {str(e)}")

def logout():
    st.session_state.token = None
    st.session_state.user = None
    st.success("Successfully logged out!")
    st.rerun()

# Main app
def main():
    st.title("🚴 BLR Riders - API Tester")
    
    # Sidebar for navigation
    st.sidebar.title("Navigation")
    
    if st.session_state.token:
        st.sidebar.success(f"Logged in as {st.session_state.user}")
        if st.sidebar.button("Logout"):
            logout()
        
        menu = ["User Profile", "Health Check"]
        choice = st.sidebar.selectbox("Menu", menu)
        
        if choice == "User Profile":
            user_profile()
        elif choice == "Health Check":
            health_check()
            
    else:
        menu = ["Login", "Register"]
        choice = st.sidebar.selectbox("Menu", menu)
        
        if choice == "Login":
            login()
        elif choice == "Register":
            register()
        
        # Always show health check in the main area when not logged in
        health_check()

if __name__ == "__main__":
    main()