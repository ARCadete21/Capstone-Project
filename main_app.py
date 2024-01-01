import streamlit as st
from streamlit_option_menu import option_menu

# Page imports
from pages_emojiless.Homepage import show_homepage
from pages_emojiless.Data_Hub import show_data_hub
from pages_emojiless.F1_Pilot import show_f1_pilot
from pages_emojiless.F1_Blog import show_f1_blog

# Define page names
pages = ["Homepage", "Data Hub", "F1 Pilot", "F1 Blog"]

# Check if the session_state variable exists; if not, initialize it
if 'selected_page' not in st.session_state:
    st.session_state.selected_page = 0

# Create the options menu for page navigation
selected_page = option_menu("F1 Data Hub", pages, default_index=st.session_state.selected_page, orientation="horizontal")

# Update the selected page in session_state
st.session_state.selected_page = pages.index(selected_page)

# Custom CSS to hide the sidebar
hide_sidebar_style = """
    <style>
        .css-1l02zg8 {
            display: none;
        }
    </style>
"""
st.markdown(hide_sidebar_style, unsafe_allow_html=True)

# Display content based on the selected page
if st.session_state.selected_page == 0:
    show_homepage()
elif st.session_state.selected_page == 1:
    show_data_hub()
elif st.session_state.selected_page == 2:
    show_f1_pilot()
elif st.session_state.selected_page == 3:
    show_f1_blog()
