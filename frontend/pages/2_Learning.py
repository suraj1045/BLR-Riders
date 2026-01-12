import streamlit as st
import sys
import os

# Add parent directory to path to import utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import make_authenticated_request
from components.navbar import render_navbar

st.set_page_config(page_title="Learning", page_icon="📚")
render_navbar()

st.title("📚 Rider Safety & Learning")

if 'token' not in st.session_state or not st.session_state.token:
    st.warning("Please login from the Home page to access this feature.")
else:
    tab1, tab2 = st.tabs(["Modules", "Create Module"])

    with tab1:
        st.subheader("Available Modules")
        if st.button("Refresh Modules"):
            response = make_authenticated_request("GET", "/api/v1/learning/")
            if response and response.status_code == 200:
                modules = response.json()
                if not modules:
                    st.info("No learning modules available.")
                else:
                    for mod in modules:
                        with st.expander(f"{mod['title']} ({mod['category']})"):
                            st.markdown(mod['content'])
            else:
                st.error("Failed to load modules.")
    
    with tab2:
        st.subheader("Add New Learning Module")
        with st.form("create_module_form"):
            title = st.text_input("Module Title")
            category = st.selectbox("Category", ["Safety", "Maintenance", "Etiquette", "Skills"])
            content = st.text_area("Content (Markdown supported)", height=200)
            
            submitted = st.form_submit_button("Publish Module")
            
            if submitted:
                payload = {
                    "title": title,
                    "category": category,
                    "content": content
                }
                
                response = make_authenticated_request("POST", "/api/v1/learning/", data=payload)
                if response and response.status_code == 200:
                    st.success("Module published successfully!")
                else:
                    st.error("Failed to publish module.")
