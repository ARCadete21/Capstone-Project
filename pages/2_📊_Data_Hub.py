#Importing the required packages
import streamlit as st
import pandas as pd

#Used to create some of the plots
import plotly.express as px

#import plost as pls
#import matplotlib.pyplot as plt


#Maybe to use option menus
from streamlit_option_menu import option_menu

#Useful Dictionaries
driver_nations = {'American' : '🇺🇸', 'British': '🇬🇧', 'Thai': '🇹🇭',
                  'Australian': '🇦🇺', 'Japanese': '🇯🇵', 'Canadian': '🇨🇦',
                  'Spanish': '🇪🇸', 'Dutch': '🇳🇱', 'German': '🇩🇪',
                  'Monegasque': '🇲🇨', 'French': '🇫🇷' , 'Finnish': '🇫🇮',
                  'Chinese': '🇨🇳', 'Mexican': '🇲🇽', 'Danish': '🇩🇰'}
driver_photos_2022 = {
    'Daniel Ricciardo': 'https://media.formula1.com/content/dam/fom-website/drivers/2022Drivers/ricciardo.jpg.img.',
    'Lando Norris': 'https://media.formula1.com/content/dam/fom-website/drivers/2022Drivers/norris.jpg.img.',
    'Lewis Hamilton': 'https://media.formula1.com/content/dam/fom-website/drivers/2022Drivers/hamilton.jpg.img.',
    'George Russell': 'https://media.formula1.com/content/dam/fom-website/drivers/2022Drivers/russell.jpg.img.',
    'Alexander Albon': 'https://media.formula1.com/content/dam/fom-website/drivers/2022Drivers/albon.jpg.img.',
    'Carlos Sainz': 'https://media.formula1.com/content/dam/fom-website/drivers/2022Drivers/sainz.jpg.img.',
    'Charles Leclerc': 'https://media.formula1.com/content/dam/fom-website/drivers/2022Drivers/leclerc.jpg.img.',
    'Esteban Ocon': 'https://media.formula1.com/content/dam/fom-website/drivers/2022Drivers/ocon.jpg.img.',
    'Fernando Alonso': 'https://media.formula1.com/content/dam/fom-website/drivers/2022Drivers/alonso.jpg.img.',
    'Lance Stroll': 'https://media.formula1.com/content/dam/fom-website/drivers/2022Drivers/stroll.jpg.img.',
    'Valtteri Bottas': 'https://media.formula1.com/content/dam/fom-website/drivers/2022Drivers/bottas.jpg.img.',
    'Guanyu Zhou': 'https://media.formula1.com/content/dam/fom-website/drivers/2022Drivers/zhou.jpg.img.',
    'Sergio Pérez': 'https://media.formula1.com/content/dam/fom-website/drivers/2022Drivers/perez.jpg.img.',
    'Max Verstappen': 'https://media.formula1.com/content/dam/fom-website/drivers/2022Drivers/verstappen.jpg.img.',
    'Nico Hülkenberg': 'https://media.formula1.com/content/dam/fom-website/drivers/2023Drivers/hulkenberg.jpg.img.1920.medium.jpg/1676983071882.jpg',
    'Pierre Gasly': 'https://media.formula1.com/content/dam/fom-website/drivers/2022Drivers/gasly.jpg.img.',
    'Yuki Tsunoda': 'https://media.formula1.com/content/dam/fom-website/drivers/2022Drivers/tsunoda.jpg.img.',
    'Nicholas Latifi': 'https://media.formula1.com/content/dam/fom-website/drivers/2022Drivers/latifi.jpg.img.',
    'Kevin Magnussen': 'https://media.formula1.com/content/dam/fom-website/drivers/2022Drivers/magnussen.jpg.img.',
    'Mick Schumacher': 'https://media.formula1.com/content/dam/fom-website/drivers/2022Drivers/schumacher.jpg.img.',
    'Nyck de Vries': 'https://media.formula1.com/content/dam/fom-website/drivers/2023Drivers/devries.jpg.img.',
    'Sebastian Vettel': 'https://media.formula1.com/content/dam/fom-website/drivers/2022Drivers/vettel.jpg.img.'
}

driver_photos_2023 = {
    'Daniel Ricciardo': 'https://media.formula1.com/content/dam/fom-website/drivers/2023Drivers/ricciardo.jpg.img.1920.medium.jpg/1689928543988.jpg',
    'Lando Norris': 'https://media.formula1.com/content/dam/fom-website/drivers/2023Drivers/norris.jpg.img.1920.medium.jpg/1677069505471.jpg',
    'Oscar Piastri': 'https://media.formula1.com/content/dam/fom-website/drivers/2023Drivers/piastri.jpg.img.1920.medium.jpg/1676983075734.jpg',
    'Lewis Hamilton': 'https://media.formula1.com/content/dam/fom-website/drivers/2023Drivers/hamilton.jpg.img.1920.medium.jpg/1677069594164.jpg',
    'George Russell': 'https://media.formula1.com/content/dam/fom-website/drivers/2023Drivers/russell.jpg.img.1920.medium.jpg/1677069334466.jpg',
    'Alexander Albon': 'https://media.formula1.com/content/dam/fom-website/drivers/2023Drivers/albon.jpg.img.1920.medium.jpg/1689253984120.jpg',
    'Carlos Sainz': 'https://media.formula1.com/content/dam/fom-website/drivers/2023Drivers/sainz.jpg.img.1920.medium.jpg/1677069189406.jpg',
    'Charles Leclerc': 'https://media.formula1.com/content/dam/fom-website/drivers/2023Drivers/leclerc.jpg.img.1920.medium.jpg/1677069223130.jpg',
    'Esteban Ocon': 'https://media.formula1.com/content/dam/fom-website/drivers/2023Drivers/ocon.jpg.img.1920.medium.jpg/1677069269007.jpg',
    'Fernando Alonso': 'https://media.formula1.com/content/dam/fom-website/drivers/2023Drivers/alonso.jpg.img.1920.medium.jpg/1701269362697.jpg',
    'Lance Stroll': 'https://media.formula1.com/content/dam/fom-website/drivers/2023Drivers/stroll.jpg.img.1920.medium.jpg/1677069453013.jpg',
    'Valtteri Bottas': 'https://media.formula1.com/content/dam/fom-website/drivers/2023Drivers/bottas.jpg.img.1920.medium.jpg/1677069810695.jpg',
    'Guanyu Zhou': 'https://media.formula1.com/content/dam/fom-website/drivers/2023Drivers/zhou.jpg.img.1920.medium.jpg/1701089369046.jpg',
    'Sergio Pérez': 'https://media.formula1.com/content/dam/fom-website/drivers/2023Drivers/perez.jpg.img.1920.medium.jpg/1677069773437.jpg',
    'Max Verstappen': 'https://media.formula1.com/content/dam/fom-website/drivers/2023Drivers/verstappen.jpg.img.1920.medium.jpg/1701270073824.jpg',
    'Nico Hülkenberg': 'https://media.formula1.com/content/dam/fom-website/drivers/2023Drivers/hulkenberg.jpg.img.1920.medium.jpg/1676983071882.jpg',
    'Pierre Gasly': 'https://media.formula1.com/content/dam/fom-website/drivers/2023Drivers/gasly.jpg.img.1920.medium.jpg/1701087615229.jpg',
    'Yuki Tsunoda': 'https://media.formula1.com/content/dam/fom-website/drivers/2023Drivers/tsunoda.jpg.img.1920.medium.jpg/1701268830375.jpg',
    'Kevin Magnussen': 'https://media.formula1.com/content/dam/fom-website/drivers/2023Drivers/magnussen.jpg.img.1920.medium.jpg/1677069387823.jpg',
    'Logan Sargeant': 'https://media.formula1.com/content/dam/fom-website/drivers/2023Drivers/sargeant.jpg.img.1920.medium.jpg/1701272060171.jpg',
    'Nyck de Vries': 'https://media.formula1.com/content/dam/fom-website/drivers/2023Drivers/devries.jpg.img.',
}

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

#### Importing the datasets from our github repo that will be used to create the visualizations ###
#Data that was used for the modelling
new_era = pd.read_csv("https://raw.githubusercontent.com/ARCadete21/Capstone-Project/cadete/data2022_2023.csv") #for general use

#Data for drivers info tab
drivers_data = pd.read_csv("https://raw.githubusercontent.com/ARCadete21/Capstone-Project/main/data/drivers.csv")
constructors_data = pd.read_csv("https://raw.githubusercontent.com/ARCadete21/Capstone-Project/main/data/constructors.csv")

circuits_data = pd.read_csv("https://raw.githubusercontent.com/ARCadete21/Capstone-Project/main/data/circuits.csv")
#altering a specific circuits_data column to avoid confusion
circuits_data.rename(columns = {'name': 'track_name'}, inplace=True)

race_data = pd.read_csv("https://raw.githubusercontent.com/ARCadete21/Capstone-Project/main/data/races.csv")
#altering a specific race_data column to avoid confusion
race_data.rename(columns = {'name': 'gp_name'}, inplace=True)


# Merge datasets based on 'driverRef'
#Adding driver's personal info
merged_drivers = pd.merge(new_era, drivers_data[['driverRef', 'forename', 'surname', 'dob', 'number', 'code']], on='driverRef', how='left')
#Adding constructors info
merged_drivers = pd.merge(merged_drivers, constructors_data[['constructorRef', 'name']], on='constructorRef', how='left')
#Adding track info & races info
merged_drivers = pd.merge(merged_drivers, circuits_data[['circuitRef', 'track_name', 'location', 'country', 'circuitId']], on='circuitRef', how='left') #possible to add lat, lng, alt

####### tá good

# # Drop duplicates from the 'circuitId' column in race_data
# race_data_unique = race_data.drop_duplicates('circuitId')
# ###############################################################################
# # Perform the left merge without duplicating rows
# merged_drivers = pd.merge(merged_drivers, race_data_unique[['circuitId', 'date', 'gp_name']], on='circuitId', how='left')

#######################

#Renaming the imported date column to gp_date, to know what it regards
merged_drivers.rename(columns = {'date': 'gp_date'}, inplace=True)

###### Additional data transformation #########

# Create a new column 'driver_name' by concatenating 'Forename' and 'Surname'
merged_drivers['driver_name'] = merged_drivers['forename'] + ' ' + merged_drivers['surname']
merged_drivers.rename(columns= {'name': 'team_name'}, inplace=True)


#Formatting time variables
# Reformat the 'dob' column to dd-mm-yyyy
merged_drivers['dob'] = pd.to_datetime(merged_drivers['dob'])
merged_drivers['dob'] = merged_drivers['dob'].dt.strftime('%d-%m-%Y')

# #Converting gp_date from object to datetime datatype
merged_drivers['gp_date'] = pd.to_datetime(merged_drivers['gp_date'])
# merged_drivers['gp_date'] = merged_drivers['gp_date'].dt.strftime('%d-%m-%Y')


# Convert the 'year' column to the appropriate data type (e.g., int)
merged_drivers['year'] = merged_drivers['year'].astype(int)


# '''
# note to self:
# columns to be used when driver is none:  
# 'grid', 'positionOrder', 'driverRef', 'driver_name', 'milliseconds_x', 
# 'nationality_x','status', 'circuitRef', 'year'
# '''




#Main Sidebar selectbox
st.sidebar.subheader("What are you looking for?")

select_opts = ['Driver Information', 
               'Constructor Statistics', 
               'Grand Prix Information',
               'Historical Data']
# Driver statistics, Constructor Statistics, Grand Prix information, etc.
option_chosen = st.sidebar.selectbox('Select your option', [None] + select_opts)



if option_chosen == 'Driver Information':
    # Sidebar specifics
    selected_year = st.sidebar.selectbox('Select Year', merged_drivers['year'].unique())

    # Filter drivers based on the selected year
    drivers_for_selected_year = merged_drivers[merged_drivers['year'] == selected_year]['driver_name'].sort_values().unique()

    # Add a None option at the beginning of the list
    drivers_list = [None] + drivers_for_selected_year.tolist()

    # Select a driver
    selected_driver = st.selectbox("Select a driver:", drivers_list, index=0, key="driver_selectbox")
    

    # Add your driver statistics content here
    if selected_driver is None:
        # Driver Standings (using overall dataset to then use for specific cases)
        driver_standings = merged_drivers.groupby(['driver_name', 'team_name', 'year'])['points'].sum().reset_index()
        driver_standings = driver_standings.rename(columns={'points': 'Total Points'})
        driver_standings_sorted = driver_standings.sort_values(by='Total Points', ascending=False)

        selected_year_data = driver_standings_sorted[driver_standings_sorted['year'] == selected_year]

        # Dropping the index column, resetting the index starting from 1, and removing the 'year' column
        selected_year_data_reset_index = selected_year_data.drop(columns=['year']).reset_index(drop=True)
        selected_year_data_reset_index.index += 1  # Set the index to start from 1

        # Renaming the first two columns
        selected_year_data_reset_index = selected_year_data_reset_index.rename(columns={'driver_name': 'Driver Name', 'team_name': 'Team Name'})

        # Display the table and stretching across the page
        st.markdown("Current Driver Championship Standings")
        st.dataframe(selected_year_data_reset_index, width=1500, height=815)


        ###### Row A of data displaying #######
        # Initializing columns to display data
        col1, col2, col3 = st.columns(3)

        # Add a new column 'positions_gained' representing positions gained per race
        merged_drivers['positions_gained'] = merged_drivers['grid'] - merged_drivers['positionOrder']

        # Filter data for the selected year
        selected_year_data = merged_drivers[merged_drivers['year'] == selected_year]

        # Display the top 5 gainers in the selected year using st.metric
        top_gainers = selected_year_data.groupby('driver_name')['positions_gained'].mean().nlargest(5).round(1)
        col1.write(f"Top 5 Position Gainers in {selected_year}:")
        for driver, positions_gained in top_gainers.items():
            col1.metric(label=driver, value=positions_gained)

        # Display top 5 losers using st.metric
        top_losers = selected_year_data.groupby('driver_name')['positions_gained'].mean().nsmallest(5).round(1)
        col2.write(f"Top 5 Position Losers in {selected_year}:")
        for driver, positions_lost in top_losers.items():
            col2.metric(label=driver, value=positions_lost)


        # #Drivers with most DNFs (tbd - terminator like schwarzeneger)
        # dnfs = selected_year_data.groupby('driver_name')['status'].value_counts().nsmallest(5)
        # col2.write(f"Top 5 Position Losers in {selected_year}:")
        # for driver, positions_lost in top_losers.items():
        #     col3.metric(label=driver, value=positions_lost)
        col3.markdown("add most dnfs")


        ###### Row B ######
        #Drivers with most wins
        winner_counts = selected_year_data[selected_year_data['positionOrder'] == 1].groupby('driver_name').size()

        gp_winners = winner_counts.nlargest(5)

        # Create a horizontal bar chart using plotly express
        fig = px.bar(gp_winners, x=gp_winners.values, 
                     y=gp_winners.index, 
                     orientation='h', 
                     title=f"Top 5 Drivers with more Wins in {selected_year}")

        # Display the chart using st.plotly_chart
        col1.plotly_chart(fig)


        # Drivers with most top 3
        # Count the occurrences of each driver in the top 3 positions
        top3_counts = selected_year_data[selected_year_data['positionOrder'] <= 3].groupby('driver_name').size()

        top3_drivers = top3_counts.nlargest(5)

        # Create a horizontal bar chart using plotly express
        fig = px.bar(top3_drivers, x=top3_drivers.values, 
                     y=top3_drivers.index, 
                     orientation='h', 
                     title=f"Top 5 Drivers with more Podiums in {selected_year}")

        # Display the chart using st.plotly_chart
        col2.plotly_chart(fig)

              
        #Boxplot with miliseconds variation (to display consistency)


        #Line Chart comparing finishing position
        
        #RaceID ordenado? How to ordenate races com o que já temos/ posso criar a ordem myself


        #Demographic Curiosities
        #Histogram with nationalities
        #Age Variation

    else:
        #Row A
        #Initializing the columns
        col1, col2, col3 = st.columns(3)

        # Select the appropriate driver_photos dictionary based on the selected year
        driver_photos_dict = driver_photos_2022 if selected_year == 2022 else driver_photos_2023

        # Column 1
        driver_pic = driver_photos_dict.get(selected_driver)
        col1.image(driver_pic, use_column_width=True)

        
        # Column 2
        #Personal Information
        #Driver's Nationality
        selected_driver_nationality = merged_drivers.loc[merged_drivers['driver_name'] == selected_driver, 'nationality_x'].iloc[0]
        selected_driver_emoji = driver_nations.get(selected_driver_nationality, '')
        col2.metric("Driver Nationality", f"{selected_driver_nationality} \n {selected_driver_emoji}")

        #Driver's Age
        selected_driver_age = merged_drivers.loc[(merged_drivers['driver_name'] == selected_driver) & (merged_drivers['year'] == selected_year), 'age'].iloc[0]
        col2.metric(f"{selected_driver}'s Age", selected_driver_age)
        #DOB 
        date_birth = merged_drivers.loc[merged_drivers['driver_name'] == selected_driver, 'dob'].iloc[0]
        col2.metric(f"{selected_driver}'s Date of Birth", date_birth)

        # Professional Info :)
        # Driver's Team
        selected_driver_team = merged_drivers.loc[(merged_drivers['driver_name'] == selected_driver) & (merged_drivers['year'] == selected_year), 'team_name'].iloc[0]
        col2.metric(f"{selected_driver} drives for", selected_driver_team)
        
        #Driver's No and Ref
        selected_driver_no = merged_drivers.loc[(merged_drivers['driver_name'] == selected_driver) & (merged_drivers['year'] == selected_year), 'number'].iloc[0]
        selected_driver_ref = merged_drivers.loc[merged_drivers['driver_name'] == selected_driver, 'code'].iloc[0]
        # Convert the tuple to a string
        driver_references = f"{selected_driver_ref}   | {selected_driver_no}"

        # Display the metric
        col2.metric(label="Driver references on the track", value=driver_references)








elif option_chosen == 'Constructor Statistics':
    selected_constructor = st.selectbox("Select a Constructor:", merged_drivers['team_name'].sort_values().unique().tolist(), 
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