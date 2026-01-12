import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")

def make_authenticated_request(method, endpoint, data=None):
    headers = {}
    if 'token' in st.session_state and st.session_state.token:
        headers["Authorization"] = f"Bearer {st.session_state.token}"
    
    url = f"{API_BASE_URL}{endpoint}"
    
    try:
        if method == 'GET':
            response = requests.get(url, headers=headers)
        elif method == 'POST':
            response = requests.post(url, json=data, headers=headers)
        
        # Don't raise error immediately, let caller handle 401/403
        return response
    except requests.exceptions.RequestException as e:
        st.error(f"Error: {str(e)}")
        return None
