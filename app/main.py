from distutils.command.clean import clean
import streamlit as st
import pandas as pd
import numpy as np
from util.nba_data import get_season_data, clean_data
import plotly.figure_factory as ff


st.set_page_config(page_title="Individual Stats", page_icon="🏀")

# Titleheader
st.title('NBA Stats')

# Create list to get the different season from 2013-2022
nba_seasons = ['20' + str(i) + '-' + str(i+1) for i in range(13, 22)][::-1]
selection = st.selectbox('NBA Season:', nba_seasons)

# Output some data
df = get_season_data(selection)
df['PPG'] = round(df['PTS'] / df['GP'], 2)
df = clean_data(df)
st.table(df.head(10))

# Getting the leader for a specific metric
metrics = df.select_dtypes(include=np.number).columns.tolist()
metric_selection = st.selectbox('Selected Metric', metrics)

col1, col2 = st.columns(2)
col1.metric(
    label=f'{metric_selection} Leader:', 
    value=df[metric_selection].max()
)
col2.metric(
    label='Player', 
    value=df[df[metric_selection] == df[metric_selection].max()]['PLAYER_NAME'].iloc[0]
)

# Plot a simple graph
fig = ff.create_distplot([df[metric_selection]], group_labels=[metric_selection], bin_size=df[metric_selection].mean()/10)
st.plotly_chart(fig, use_container_width=True)
