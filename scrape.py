import pandas as pd

"""
Read a csv file from url
"""

# access the url
pr_league = pd.read_csv('https://www.football-data.co.uk/mmz4281/2122/E0.csv')

#print(pr_league)

# to rename columns
pr_league.rename(columns={'FTHG':'hm_goals',
                          'FTAG':'aw_goals'}, inplace=True)