from nba_api.stats.endpoints import leaguedashplayerstats
import pandas as pd


def get_season_data(season: str):
    """Retrieves the season data for the desired season. I believe this only goes back to 2013. 

    Args:
        szn (str): NBA season in the following format: YYYY-YY

    Returns:
        pd.DataFrame: Returns a dataframe containing information for each player. 
    """
    return leaguedashplayerstats.LeagueDashPlayerStats(season=season).get_data_frames()[0]


def clean_data(df: pd.DataFrame):
    return df.drop(['PLAYER_ID', 'NICKNAME', 'TEAM_ID', 'WNBA_FANTASY_PTS_RANK', 'CFID', 'CFPARAMS'], axis=1)