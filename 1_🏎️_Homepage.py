import streamlit as st

#Setting the overall page configuration
st.set_page_config(
    layout='wide',
    page_title='AiTHLETES F1 Hub Homepage',
    page_icon="🏎️",
    initial_sidebar_state='collapsed',
    #menu_items = {'item': 'link'} could be interesting to explore (top right corner)
)

#Sidebar settings
st.sidebar.header('AiTHLETES F1 Hub')
#st.sidebar.success("Select one of the above pages to navigate through our Website")


#Page content
st.title("Welcome to your new Formula One Hub!")
st.text("adding some text")







####To Finish Off the Sidebar with Trademark
st.sidebar.markdown('''
---
Website developed for the \n Capstone Project Course
                    
                    © AiTHLETES  
''') 