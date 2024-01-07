import fastf1 as ff1
from fastf1 import plotting
from fastf1 import utils
import fastf1.legacy
import fastf1 as ff1
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib import cm
import matplotlib.font_manager as fm
import numpy as np
import pandas as pd
import matplotlib as mpl

colormap = mpl.cm.plasma


def draw_f1_circuit(circuit, year=2023):
    session = fastf1.get_session(year, circuit, 'R')
    session.load()
    circuit_info = session.get_circuit_info()
    lap = session.laps.pick_fastest()
    pos = lap.get_pos_data()
    fig, ax = plt.subplots(figsize=(10, 5))

    track = pos.loc[:, ('X', 'Y')].to_numpy()

    track_angle = circuit_info.rotation / 180 * np.pi

    offset_vector = [500, 0]

    def rotate(xy, *, angle):
        rot_mat = np.array([[np.cos(angle), np.sin(angle)],
                            [-np.sin(angle), np.cos(angle)]])
        return np.matmul(xy, rot_mat)

    rotated_track = rotate(track, angle=track_angle)
    plt.plot(rotated_track[:, 0], rotated_track[:, 1], color='tab:orange')

    # Iterate over all corners.
    for _, corner in circuit_info.corners.iterrows():
        # Create a string from corner number and letter
        txt = f"{corner['Number']}{corner['Letter']}"

        # Convert the angle from degrees to radian.
        offset_angle = corner['Angle'] / 180 * np.pi

        # Rotate the offset vector so that it points sideways from the track.
        offset_x, offset_y = rotate(offset_vector, angle=offset_angle)

        # Add the offset to the position of the corner
        text_x = corner['X'] + offset_x
        text_y = corner['Y'] + offset_y

        # Rotate the text position equivalently to the rest of the track map
        text_x, text_y = rotate([text_x, text_y], angle=track_angle)

        # Rotate the center of the corner equivalently to the rest of the track map
        track_x, track_y = rotate([corner['X'], corner['Y']], angle=track_angle)

        # Draw a circle next to the track.
        plt.scatter(text_x, text_y, color='yellow', s=140)

        # Draw a line from the track to this circle.
        plt.plot([track_x, text_x], [track_y, text_y], color='yellow')

        # Finally, print the corner number inside the circle.
        plt.text(text_x, text_y, txt,
                 va='center_baseline', ha='center', size='small', color='black')

        # Add title with session name
        plt.title(session.event['EventName'])

        # hide axis
        ax.axis('off')


def compare_track_dominance(race_name, driver_surname1, driver_surname2, year=2023, session='Q'):
    session_event = ff1.get_session(year, race_name, session)
    session_event.load()

    driver01 = session_event.results[session_event.results['LastName'] == driver_surname1]['Abbreviation'].values[0]
    driver02 = session_event.results[session_event.results['LastName'] == driver_surname2]['Abbreviation'].values[0]

    drivers = [driver01, driver02]
    compare_drivers = session_event.laps[session_event.laps['Driver'].isin(drivers)]

    fastest_lap_driver01 = session_event.laps.pick_driver(driver01).pick_fastest()
    fastest_lap_driver02 = session_event.laps.pick_driver(driver02).pick_fastest()

    telemetry_driver01 = fastest_lap_driver01.get_telemetry().add_distance()
    telemetry_driver02 = fastest_lap_driver02.get_telemetry().add_distance()

    telemetry_driver01['Driver'] = driver01
    telemetry_driver02['Driver'] = driver02
    # telemetry_drivers = pd.DataFrame(telemetry_driver01).append(pd.DataFrame(telemetry_driver02))
    telemetry_drivers = pd.concat([telemetry_driver01, telemetry_driver02])

    # We want 25 mini-sectors (this can be adjusted up and down)
    num_minisectors = 7 * 3

    # Grab the maximum value of distance that is known in the telemetry
    total_distance = total_distance = max(telemetry_drivers['Distance'])

    # Generate equally sized mini-sectors
    minisector_length = total_distance / num_minisectors

    # Initiate minisector variable, with 0 (meters) as a starting point.
    minisectors = [0]

    # Add multiples of minisector_length to the minisectors
    for i in range(0, (num_minisectors - 1)):
        minisectors.append(minisector_length * (i + 1))

    telemetry_drivers['Minisector'] = telemetry_drivers['Distance'].apply(
        lambda dist: (
            int((dist // minisector_length) + 1)
        )
    )

    average_speed = telemetry_drivers.groupby(['Minisector', 'Driver'])['Speed'].mean().reset_index()

    # Select the driver with the highest average speed
    fastest_driver = average_speed.loc[average_speed.groupby(['Minisector'])['Speed'].idxmax()]

    # Get rid of the speed column and rename the driver column
    fastest_driver = fastest_driver[['Minisector', 'Driver']].rename(columns={'Driver': 'Fastest_driver'})

    # Join the fastest driver per minisector with the full telemetry
    telemetry_drivers = telemetry_drivers.merge(fastest_driver, on=['Minisector'])

    # Order the data by distance to make matploblib does not get confused
    telemetry_drivers = telemetry_drivers.sort_values(by=['Distance'])

    # Convert driver name to integer
    telemetry_drivers.loc[telemetry_drivers['Fastest_driver'] == driver01, 'Fastest_driver_int'] = 1
    telemetry_drivers.loc[telemetry_drivers['Fastest_driver'] == driver02, 'Fastest_driver_int'] = 2

    x = np.array(telemetry_drivers['X'].values)
    y = np.array(telemetry_drivers['Y'].values)

    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    fastest_driver_array = telemetry_drivers['Fastest_driver_int'].to_numpy().astype(float)

    cmap = plt.get_cmap('spring', 2)
    lc_comp = LineCollection(segments, norm=plt.Normalize(1, cmap.N + 1), cmap=cmap)
    lc_comp.set_array(fastest_driver_array)
    lc_comp.set_linewidth(5)

    plt.rcParams['figure.figsize'] = [12, 6]

    plt.gca().add_collection(lc_comp)
    plt.axis('equal')
    plt.tick_params(labelleft=False, left=False, labelbottom=False, bottom=False)

    cbar = plt.colorbar(mappable=lc_comp, label='Driver', boundaries=np.arange(1, 4))
    cbar.set_ticks(np.arange(1.5, 3.5))
    cbar.set_ticklabels([driver01, driver02])
    # Store the fastest lap time of each driver. Use only minutes and seconds.

    title_color = 'silver'  # '#6441a5'
    plt.title(
        f"{year} {race_name} | {session} {driver_surname1} ({fastest_lap_driver01['LapTime']}) vs {driver_surname2} ({fastest_lap_driver02['LapTime']})",
        color=title_color, fontsize=16)

    plt.show()


# Gather data from FastF1
def get_from_fastf1(year, gp, session):
    # To get any data, you need to specify a session. This can be done by using the get_session method.
    # Session can be one of 'FP1', 'FP2', 'FP3', 'Q', 'R'.
    # GP can be the name of the GP, e.g. 'Monaco' or 'Monza', or the name of the circuit, e.g. 'Baku City Circuit'.
    # It can also be the name of the country, e.g. 'Italy' or 'Azerbaijan', but some countries have multiple GPs.
    session = ff1.get_session(year, gp, session)
    session.load()


import pandas as pd
import plotly.express as px
from plotly.io import show

from fastf1.ergast import Ergast
def plot_driver_standings_by_year(year):
    """
    Plot the driver standings of a given year. The data is obtained from Ergast. Be careful of the Ergast API limit.

    Parameters
    ----------
    year : int
        The year of the season.

    Returns
    -------
    fig : plotly.graph_objects.Figure
        A figure object.
    """

    ergast = Ergast()
    races = ergast.get_race_schedule(year)  # Races in year 2022
    results = []

    # For each race in the season
    for rnd, race in races['raceName'].items():

        # Get results. Note that we use the round no. + 1, because the round no.
        # starts from one (1) instead of zero (0)
        temp = ergast.get_race_results(season=year, round=rnd + 1)
        temp = temp.content[0]

        # If there is a sprint, get the results as well
        sprint = ergast.get_sprint_results(season=year, round=rnd + 1)
        if sprint.content and sprint.description['round'][0] == rnd + 1:
            temp = pd.merge(temp, sprint.content[0], on='driverCode', how='left')
            # Add sprint points and race points to get the total
            temp['points'] = temp['points_x'] + temp['points_y']
            temp.drop(columns=['points_x', 'points_y'], inplace=True)

        # Add round no. and grand prix name
        temp['round'] = rnd + 1
        temp['race'] = race.removesuffix(' Grand Prix')
        temp = temp[['round', 'race', 'driverCode', 'points']]  # Keep useful cols.
        results.append(temp)

    # Append all races into a single dataframe
    results = pd.concat(results)
    races = results['race'].drop_duplicates()

    results = results.pivot(index='driverCode', columns='round', values='points')
    # Here we have a 22-by-22 matrix (22 races and 22 drivers, incl. DEV and HUL)

    # Rank the drivers by their total points
    results['total_points'] = results.sum(axis=1)
    results = results.sort_values(by='total_points', ascending=False)
    results.drop(columns='total_points', inplace=True)

    # Use race name, instead of round no., as column names
    results.columns = races

    fig = px.imshow(
        results,
        text_auto=True,
        aspect='auto',  # Automatically adjust the aspect ratio
        color_continuous_scale=[[0,    'rgb(198, 219, 239)'],  # Blue scale
                                [0.25, 'rgb(107, 174, 214)'],
                                [0.5,  'rgb(33,  113, 181)'],
                                [0.75, 'rgb(8,   81,  156)'],
                                [1,    'rgb(8,   48,  107)']],
        labels={'x': 'Race',
                'y': 'Driver',
                'color': 'Points'}       # Change hover texts
    )
    fig.update_xaxes(title_text='')      # Remove axis titles
    fig.update_yaxes(title_text='')
    fig.update_yaxes(tickmode='linear')  # Show all ticks, i.e. driver names
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGrey',
                     showline=False,
                     tickson='boundaries')              # Show horizontal grid only
    fig.update_xaxes(showgrid=False, showline=False)    # And remove vertical grid
    fig.update_layout(plot_bgcolor='rgba(0,0,0,0)')     # White background
    fig.update_layout(coloraxis_showscale=False)        # Remove legend
    fig.update_layout(xaxis=dict(side='top'))           # x-axis on top
    fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))  # Remove border margins
    show(fig)
