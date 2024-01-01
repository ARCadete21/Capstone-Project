# import streamlit as st
# from streamlit_option_menu import option_menu as optm

# #Setting the overall page configuration
# st.set_page_config(
#     layout='wide',
#     page_title='AiTHLETES F1 Hub | Homepage',
#     page_icon="🏎️",
#     initial_sidebar_state='collapsed',
#     #menu_items = {'item': 'link'} could be interesting to explore (top right corner)
# )

# #Sidebar settings
# st.sidebar.header('AiTHLETES F1 Hub')
# #st.sidebar.success("Select one of the above pages to navigate through our Website")

# #Attempting to create a menu for the website
# selected3 = optm(None, ["Home", "Upload",  "Tasks", 'Settings'], 
#     icons=['house', 'cloud-upload', "list-task", 'gear'], 
#     menu_icon="cast", default_index=0, orientation="horizontal",
#     styles={
#         "container": {"padding": "0!important", "background-color": "#fafafa"},
#         "icon": {"color": "orange", "font-size": "25px"}, 
#         "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
#         "nav-link-selected": {"background-color": "green"},
#     }
# )

# #Page content
# st.title("Welcome to your new Formula One Hub!")
# st.text("")
# st.image("https://cdn.racingnews365.com/2023/_1125x633_crop_center-center_85_none/SI202307230399.jpg?v=1690140014",
#          width=750)
# st.text("adding some text")


##trying some new code

import streamlit as st

def show_homepage():
    st.title("Welcome to F1 Data Hub - Homepage")
    # Add content specific to the Homepage





####To Finish Off the Sidebar with Trademark
st.sidebar.markdown('''
---
Website developed for the \n Capstone Project Course
                    
                    © AiTHLETES  
''') 