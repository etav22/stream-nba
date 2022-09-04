from distutils.command.clean import clean
import streamlit as st
import pandas as pd
import numpy as np
from util.nba_data import get_season_data, clean_data
import plotly.figure_factory as ff

def streamlit_app():
    
    # Titleheader
    st.title('NBA Stats')

    # Create list to get the different season from 2013-2022
    nba_seasons = ['20' + str(i) + '-' + str(i+1) for i in range(13, 22)][::-1]
    selection = st.selectbox('NBA Season:', nba_seasons)

    # Output some data
    df = get_season_data(selection)
    df = clean_data(df)
    st.table(df.head(10))

    # Setting metrics:
    col1, col2, col3 = st.columns(3)
    col1.metric(label='Max Points Scored:', value=df['PTS'].max())
    col2.metric(label='Player', value=df[df['PTS'] == df['PTS'].max()]['PLAYER_NAME'].iloc[0])


    # Plot a simple graph
    fig = ff.create_distplot([df['PTS']], group_labels=['PTS'], bin_size=100)
    st.plotly_chart(fig, use_container_width=True)

if __name__ == '__main__':
    streamlit_app()