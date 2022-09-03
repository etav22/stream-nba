from nba_api.stats.endpoints import leaguedashplayerstats


def get_season_data(season: str):
    """Retrieves the season data for the desired season. I believe this only goes back to 2013. 

    Args:
        season (str): NBA season in the following format: YYYY-YY

    Returns:
        pd.DataFrame: Returns a dataframe containing information for each player. 
    """
    return leaguedashplayerstats.LeagueDashPlayerStats(season=season).get_available_data()[0]
