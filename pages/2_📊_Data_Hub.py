#Importing the required packages
import streamlit as st
import pandas as pd

#Used to create some of the plots
import plost as pls
#import matplotlib.pyplot as plt
import plotly.express as px

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
new_era = pd.read_csv("https://raw.githubusercontent.com/ARCadete21/Capstone-Project/cadete/data2022_2023.csv")


#### Subsetting the samples for different utilities 
# Creating a new DataFrame containing only Driver Names
driver_names = new_era[['driverRef']].drop_duplicates().copy()


# Capitalize the first letter of all other names
driver_names['driverRef'] = driver_names['driverRef'].str.capitalize()


# Mapping of specific names to be replaced
name_mapping = {'Max_verstappen': 'Verstappen',
                'Kevin_magnussen': 'Magnussen',
                'Mick_schumacher': 'Schumacher',
                'De_vries': 'De Vries'}

# Replace values in the 'driver_names' column using the mapping
driver_names['driverRef'] = driver_names['driverRef'].replace(name_mapping)

# to reset the index of the new DataFrame
driver_names.reset_index(drop=True, inplace=True)
driver_names.sort_values(by='driverRef', inplace=True)

######################
# Creating a new DataFrame containing only Team Names
team_names = new_era[['constructorRef']].drop_duplicates().copy()

# Capitalize the first letter of all other names
team_names['constructorRef'] = team_names['constructorRef'].str.capitalize()

# Mapping of specific names to be replaced
team_mapping = {'Aston_martin': 'Aston Martin',
                'Red_bull': 'Red Bull',
                'Alphatauri': 'Alpha Tauri',
                'Alfa': 'Alfa Romeo'}

# Replace values in the 'driver_names' column using the mapping
team_names['constructorRef'] = team_names['constructorRef'].replace(team_mapping)

# to reset the index of the new DataFrame
team_names.reset_index(drop=True, inplace=True)
team_names.sort_values(by='constructorRef', inplace=True)

######################










######## Main content of the page ########
#Page introduction
st.title("Data Hub")
st.text("In this page you will be able to find all things data related about the ongoing F1 Season!")
st.text("To the left you will find the sliders to filter for your favorite drivers and your favorite teams")
st.text("(or for anything you'd like really 😊)")

######## Row A #######
#Column 1
st.markdown('### Interesting facts')
col1, col2, col3 = st.columns(3)
#Subsetting a dataset containing only 1 row per driver
new_era_unique = new_era.drop_duplicates(subset='driverRef')
#Calculate the average age of the drivers
average_age = new_era_unique['age'].mean()
#Creating the first info box
col1.metric("Average Age on The Grid", average_age)


# #Column 2
# #Create a DataFrame with counts
# count_df = new_era_unique['nationality_y'].value_counts().reset_index()
# count_df.columns = ['nationality_y', 'count']

# #Plotting the bar chart using Plotly
# fig = px.bar(count_df, 
#              x='nationality_y', 
#              y='count',
#              title='Different Nationalities on the Grid')

# #Adjust the figure size and labels
# fig.update_layout(width=300, height=300,
#                   xaxis_title='Nationality',
#                   yaxis_title='Count')

# #Display the bar chart in the Streamlit app
# col2.plotly_chart(fig)


# #Column 3
# col3.metric("Humidity", "86%", "4%")


# ######## Sidebar definitions ########
# st.sidebar.header('F1 Data Hub')

# #Driver selection selectbox
# st.sidebar.subheader("Driver Selection")
# # driver_selbox = st.sidebar.selectbox('Filter By Driver', (driver_names.driverRef))
# # Create a sidebar selectbox to choose a driver
# selected_driver = st.sidebar.selectbox("Select a Driver", new_era_unique['driverRef'])

# # Filter the DataFrame based on the selected driver
# filtered_data = new_era_unique[new_era_unique['driverRef'] == selected_driver]

# # Display the selected driver's nationality using st.metric
# st.metric(label=f"Nationality of {selected_driver}", value=filtered_data['nationality_y'].iloc[0])


#Constructor Selection selectbox
st.sidebar.subheader("Constructor Selection")
team_selbox = st.sidebar.selectbox('Filter By Constructor', (team_names.constructorRef))




import streamlit as st
import pandas as pd
import plotly.express as px


# Create a sidebar selectbox to choose a driver
selected_driver = st.sidebar.selectbox("Select a Driver", [None] + list(new_era_unique['driverRef']))

# Check if the selected driver is None or a specific driver
if selected_driver is None:
    # Display the bar chart of counts per nationality
    fig = px.bar(new_era_unique.groupby('nationality_x').size().reset_index(name='count'), 
                 x='nationality_x', 
                 y='count',
                 title='Count of Drivers per Nationality')

    # Update axis labels
    fig.update_layout(
        xaxis_title='Nationality',
        yaxis_title='Count'
    )

    # Display the bar chart in the Streamlit app
    col2.plotly_chart(fig)
else:
    # Filter the DataFrame based on the selected driver
    filtered_data = new_era_unique[new_era_unique['driverRef'] == selected_driver]

    # Display the selected driver's nationality using st.metric
    col2.metric(label=f"Nationality of {selected_driver}", value=filtered_data['nationality_x'].iloc[0])









####To Finish Off the Sidebar with Trademark
st.sidebar.markdown('''
---
Website developed for the \n Capstone Project Course
                    
                    © AiTHLETES  
''') 