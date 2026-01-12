import streamlit as st
import sys
import os
from datetime import datetime

# Add parent directory to path to import utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import make_authenticated_request
from components.navbar import render_navbar

st.set_page_config(page_title="Rides", page_icon="🗺️")
render_navbar()

st.title("🗺️ Ride Hosting & Discovery")

if 'token' not in st.session_state or not st.session_state.token:
    st.warning("Please login from the Home page to access this feature.")
else:
    tab1, tab2 = st.tabs(["Find a Ride", "Host a Ride"])

    with tab1:
        st.subheader("Upcoming Rides")
        if st.button("Refresh Rides"):
            response = make_authenticated_request("GET", "/api/v1/rides/")
            if response and response.status_code == 200:
                rides = response.json()
                if not rides:
                    st.info("No upcoming rides found.")
                else:
                    for ride in rides:
                        with st.expander(f"{ride['title']} - {datetime.fromisoformat(ride['date']).strftime('%Y-%m-%d %H:%M')}"):
                            st.markdown(f"**Difficulty:** {ride['difficulty']}")
                            st.markdown(f"**Route:** {ride['route']}")
                            st.markdown(f"**Description:** {ride['description']}")
                            st.button("Join Ride", key=f"join_{ride['id']}") 
            else:
                st.error("Failed to load rides.")

    with tab2:
        st.subheader("Host a New Ride")
        with st.form("create_ride_form"):
            title = st.text_input("Ride Title")
            description = st.text_area("Description")
            date = st.date_input("Date")
            time = st.time_input("Time")
            route = st.text_input("Route/Destination")
            difficulty = st.selectbox("Difficulty", ["Beginner", "Intermediate", "Expert"])
            
            submitted = st.form_submit_button("Create Ride")
            
            if submitted:
                # Combine date and time
                ride_datetime = datetime.combine(date, time)
                
                payload = {
                    "title": title,
                    "description": description,
                    "date": ride_datetime.isoformat(),
                    "route": route,
                    "difficulty": difficulty
                }
                
                response = make_authenticated_request("POST", "/api/v1/rides/", data=payload)
                if response and response.status_code == 200:
                    st.success("Ride created successfully!")
                else:
                    st.error("Failed to create ride.")
