#Importing the required packages
import streamlit as st
import pandas as pd

#Used to create some of the plots
#import plost as pls
#import matplotlib.pyplot as plt
#import plotly.express as px

#Maybe to use option menus
from streamlit_option_menu import option_menu


######## Setting the overall page configuration ########
st.set_page_config(
    layout='wide',
    page_title='AiTHLETES F1 Hub | Data Hub',
    page_icon="📊",
    initial_sidebar_state='collapsed'
)

######## Setting a new style for the page ########
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

#### Importing the datasets from our github repo that will be used to create the visualizations
new_era = pd.read_csv("https://raw.githubusercontent.com/ARCadete21/Capstone-Project/cadete/data2022_2023.csv") #for general use

#Data for drivers tab
drivers_data = pd.read_csv("https://raw.githubusercontent.com/ARCadete21/Capstone-Project/main/data/drivers.csv")
constructors_data = pd.read_csv("https://raw.githubusercontent.com/ARCadete21/Capstone-Project/main/data/constructors.csv")
# Merge datasets based on 'driverRef'
merged_drivers = pd.merge(new_era, drivers_data[['driverRef', 'forename', 'surname']], on='driverRef', how='left')
merged_drivers = pd.merge(merged_drivers, constructors_data[['constructorRef', 'name']], on='constructorRef', how='left')

# Create a new column 'driver_name' by concatenating 'Forename' and 'Surname'
merged_drivers['driver_name'] = merged_drivers['forename'] + ' ' + merged_drivers['surname']

# year int
merged_drivers['year'] = merged_drivers['year'].astype('Int32')

# Sample mapping of constructorRef values to image paths
# constructor_logos = {
#     'Mercedes': 'https://yt3.googleusercontent.com/GAn-iyc9QWZT_RsxaGRuX7deb8AP2dJRo9N8XOjYeciqQMC6AP00zNTXQXqiApHN3QtmsAYK=s900-c-k-c0x00ffffff-no-rj',
#     'Red Bull': 'https://liquipedia.net/commons/images/d/d8/Red_Bull_Racing_allmode.png',
#     'McLaren': 'https://logowik.com/content/uploads/images/mclaren-formula-1-team8249.logowik.com.webp',
#     'Aston Martin': 'https://logowik.com/content/uploads/images/aston-martin-cognizant-formula-one-team6133.jpg',
#     'AlphaTauri': 'https://upload.wikimedia.org/wikipedia/en/thumb/0/09/Scuderia_Alpha-Tauri.svg/1200px-Scuderia_Alpha-Tauri.svg.png',
#     'Haas F1 Team': 'https://branditechture.agency/brand-logos/wp-content/uploads/wpdm-cache/Haas-F1-Team-900x0.png',
#     'Alpine F1 team': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Alpine_F1_Team_Logo.svg/2233px-Alpine_F1_Team_Logo.svg.png',
#     'Williams': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Logo_Williams_F1.png/1280px-Logo_Williams_F1.png',
#     'Ferrari': 'https://w7.pngwing.com/pngs/733/606/png-transparent-scuderia-ferrari-laferrari-car-formula-1-ferrari-logo-signage-ferrari-thumbnail.png',
#     'Alfa Romeo': 'https://media.formula1.com/image/upload/content/dam/fom-website/manual/teams/Sauber/Alfa_Romeo_Racing_logo.jpg'
# }

driver_nations = {'American' : '🇺🇸', 'British': '🇬🇧', 'Thai': '🇹🇭',
                  'Australian': '🇦🇺', 'Japanese': '🇯🇵', 'Canadian': '🇨🇦',
                  'Spanish': '🇪🇸', 'Dutch': '🇳🇱', 'German': '🇩🇪',
                  'Monegasque': '🇲🇨', 'French': '🇫🇷' , 'Finnish': '🇫🇮',
                  'Chinese': '🇨🇳', 'Mexican': '🇲🇽', 'Danish': '🇩🇰'
}



#Constructor Selection selectbox
st.sidebar.subheader("What are you looking for?")
select_opts = ['Driver Information', 
               'Constructor Statistics', 
               'Grand Prix Information',
               'Historical Data']
# Driver statistics, Constructor Statistics, Grand Prix information
option_chosen = st.sidebar.selectbox('Select your option', [None] + select_opts)

if option_chosen == 'Driver Information':
    selected_driver = st.selectbox("Select a driver:", [None] + merged_drivers['driver_name'].sort_values().unique().tolist(), 
                                   index=0, key="driver_selectbox")
    #Sidebar specifics
    st.sidebar.selectbox('Select Year', merged_drivers['year'].unique())
    st.sidebar.write(f"Driver selected: {selected_driver}")
    # Add your driver statistics content here
    if selected_driver is None:
        #Inserir general graficos
        st.text('narah yet')


    else:
        #Row A
        #Initializing the columns
        col1, col2, col3 = st.columns(3)

        # Column 1
        # Assuming selected_driver is the variable containing the selected driver's name
        selected_driver_nationality = merged_drivers.loc[merged_drivers['driver_name'] == selected_driver, 'nationality_x'].iloc[0]
        selected_driver_emoji = driver_nations.get(selected_driver_nationality, '')
        col1.metric("Driver Nationality", f"{selected_driver_nationality} \n {selected_driver_emoji}")

        selected_driver_age = merged_drivers.loc[merged_drivers['driver_name'] == selected_driver, 'age'].iloc[0]
        col1.metric(f"{selected_driver}'s Age", selected_driver_age)

        #Column 2
        selected_driver_team = merged_drivers.loc[merged_drivers['driver_name'] == selected_driver, 'name'].iloc[0]
        col2.metric(f"{selected_driver} drives for", selected_driver_team)

        








elif option_chosen == 'Constructor Statistics':
    selected_constructor = st.selectbox("Select a Constructor:", merged_drivers['name'].sort_values().unique().tolist(), 
                                   index=0, key="constructor_selectbox")

    st.sidebar.write("Constructor statistics content goes here")#Sidebar specifics
    st.sidebar.selectbox('Select Year', merged_drivers['year'].unique())
    st.sidebar.write(f"Driver selected: {selected_constructor}")# Add your constructor statistics content here

elif option_chosen == 'Grand Prix Information':
    st.sidebar.write("Grand Prix information content goes here")
    # Add your Grand Prix information content here

elif option_chosen is None:
    st.sidebar.write("Select an option to display relevant content")
    # Add default content here






####To Finish Off the Sidebar with Trademark
st.sidebar.markdown('''
---
Website developed for the \n Capstone Project Course
                    
                    © AiTHLETES  
''') 