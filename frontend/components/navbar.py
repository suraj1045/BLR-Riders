import streamlit as st

def render_navbar():
    """
    Renders a top navigation bar using Streamlit columns and buttons/links.
    """
    # Custom CSS to style the navbar (optional, but good for visual separation)
    st.markdown("""
        <style>
        .stButton button {
            width: 100%;
        }
        </style>
    """, unsafe_allow_html=True)

    with st.container():
        # Columns for navigation items
        # Adjust column widths as needed
        col1, col2, col3, col4, col5, col6 = st.columns([2, 1, 1, 1, 1, 1])

        with col1:
            st.write("### 🏍️ BLR Riders")
        
        with col2:
            st.page_link("app.py", label="Home", icon="🏠")
        
        with col3:
            st.page_link("pages/1_Rides.py", label="Rides", icon="🗺️")
        
        with col4:
            st.page_link("pages/2_Learning.py", label="Learning", icon="📚")
        
        with col5:
            st.page_link("pages/3_Chatbot.py", label="Chatbot", icon="🤖")

        with col6:
            if 'token' in st.session_state and st.session_state.token:
                if st.button("Logout", key="navbar_logout"):
                    st.session_state.token = None
                    st.session_state.user = None
                    st.rerun()
            else:
                st.write("") # Spacer if not logged in

    st.markdown("---")
