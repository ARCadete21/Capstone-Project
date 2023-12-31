import streamlit as st

st.set_page_config(
    page_title='Title of the page',
    page_icon=":slight_smile:"
)

st.title("Main Page")
st.text("adding some text")
st.sidebar.success("Select one of the below pages")