import streamlit as st


st.set_page_config(
    layout='wide',
    page_title='AiTHLETES F1 Hub | F1 Blog',
    page_icon="📢",
    initial_sidebar_state='collapsed'
)


######## Setting a new style for the page ########
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)




####To Finish Off the Sidebar with Trademark
st.sidebar.markdown('''
---
Website developed for the \n Capstone Project Course
                    
                    © AiTHLETES  
''') 



