import streamlit as st
import sys
import os

# Add parent directory to path to import components
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from components.navbar import render_navbar

st.set_page_config(page_title="Live Tracking", page_icon="📍")
render_navbar()

st.title("📍 Live Group Tracking")

st.info("This feature is currently under development.")

st.markdown("""
### Planned Features:
- Real-time location sharing with group members
- Live map view of all riders
- Emergency alerts and status updates
""")

# Placeholder map
st.map(latitude=[12.9716], longitude=[77.5946], zoom=12)
