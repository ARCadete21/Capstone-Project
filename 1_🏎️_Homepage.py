import streamlit as st
from streamlit_option_menu import option_menu as optm

######## Setting a new style for the page ########
st.set_page_config(
    layout='wide',
    page_title='AiTHLETES F1 Hub | Homepage',
    page_icon="🏎️",
    initial_sidebar_state='collapsed',
    #menu_items = {'item': 'link'} could be interesting to explore (top right corner)
)



#Page content
st.title("Welcome to your new Formula One Hub!")
st.text("")
st.image("https://cdn.racingnews365.com/2023/_1125x633_crop_center-center_85_none/SI202307230399.jpg?v=1690140014",
         width=750)
st.text("adding some text")


####To Finish Off the Sidebar with Trademark
st.sidebar.markdown('''
---
Website developed for the \n Capstone Project Course
                    
                    © AiTHLETES  
''')