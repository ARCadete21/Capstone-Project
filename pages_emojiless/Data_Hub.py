# #Importing the required packages
# import streamlit as st
# import pandas as pd

# #Used to create some of the plots
# import plost as pls

# st.set_page_config(
#     layout='wide',
#     page_title='AiTHLETES F1 Hub | Data Hub',
#     page_icon="📊",
#     initial_sidebar_state='collapsed'
# )

# st.title("Data Hub")
# st.text("In this page you will be able to find all things data related about the ongoing F1 Season!")

# ####
# # with open('style.css') as f:
# #     st.markdown(f'<style>{f.read()}</style>')

# st.sidebar.subheader("testing some tests")

import streamlit as st
import pandas as pd

def show_data_hub():
    st.title("F1 Data Hub - Data Hub")
    # Add content specific to the Data Hub page


#Importing the datasets from our github repo
drivers_data = pd.read_csv('https://raw.githubusercontent.com/ARCadete21/Capstone-Project/main/data/drivers.csv')
drivers_data
