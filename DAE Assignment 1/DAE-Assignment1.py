"""
Assignment 1
Part 2: Python Programming

In this assignment, you will analyze two datasets; PlayerStatistics.csv and Games.csv.
These datasets contain player statistics for NBA (National Basket Association) games played from 1947-2025.
The datasets provide an avenue to research basketball history, players’ performance, games data and the teams’ performance.

Student Name: Silvana Paredes
Date: 03/10/2025
"""

import pandas as pd
import matplotlib.pyplot as plt

#--------------------------------------------------------------------------
#1.Loading the Dataset
#a.Read the files
df_games = pd.read_csv("Games.csv", sep=",", low_memory=False)
df_players = pd.read_csv("PlayerStatistics.csv", sep=",", low_memory=False)

#b.Display the first 10 rows of each dataset
print(f'\nGames file:\n{df_games.head(10)}')
print(f'\nPlayers file:\n{df_players.head(10)}')

#--------------------------------------------------------------------------
#2.Data Manipulation 
#a.Check for missing values
print('\nCheck for missing values:')
print(f'\nGames file:\n{df_games.isnull().sum()}')
print(f'\nPlayers file:\n{df_players.isnull().sum()}')

#b.Create a new column in PlayerStatistics.csv called Full Name to combine both firstName and lastName field
df_players['fullName'] = df_players['firstName'] + ' ' + df_players['lastName']
print(f"\nFull name column:\n{df_players['fullName'].head(10)}")

#c.Identify the types of games the players played using the gameType field in PlayerStatistics.csv
game_types = df_players['gameType'].unique()
print(f'\nTypes of games:\n{game_types}')

#Replace 'Preseason' to 'Pre-season'
df_players['gameType'] = df_players['gameType'].replace('Preseason', 'Pre-season')
#Display the column after applying the changes
df_preseason = df_players.loc[df_players['gameType'] == 'Pre-season', 'gameType']
print(f'\nUpdated gameType column:\n{df_preseason}')

#--------------------------------------------------------------------------
#3.Data Summary
#Using Games.csv
#a.Identify and list categorical columns in Games.csv.
df_cat = df_games.select_dtypes(include=['object','category']).columns
print(f'\nCategorical columns:\n{df_cat}')

#b.List the distinct/unique hometeamCity and count them in Games.csv.
#List
df_hometeamCity = df_games['hometeamCity'].unique()
print(f'\nUnique Hometeam Cities:\n{df_hometeamCity}')

#Count
num_hometeamCity = df_games['hometeamCity'].nunique()
print('\nNumber of Hometeam Cities:', num_hometeamCity)

#c.Generate descriptive statistics for numerical features in Games.csv.
print('\nDescriptive statistics for numerical features in Games:\n',df_games.describe(include='number'))

#Using PlayerStatistics.csv
#d.Identify the clubs the players play for, how many clubs do we have? 
#List
df_clubs = df_players['playerteamName'].unique()
print(f'\nClubs:\n{df_clubs}')

#Count
num_clubs = df_players['playerteamName'].nunique()
print('\nNumber of clubs:', num_clubs)

#--------------------------------------------------------------------------
#4.Players Analysis
#a.Using a bar chart, Display the top 10 players from 1947-2025 based on points.
#Get the top 10 players based on total points
df_top10 = df_players.groupby('fullName')['points'].sum().sort_values(ascending=False).head(10)
print(f'\nTop 10 Players from 1947-2025:\n{df_top10}')

#Bar chart
plt.figure(figsize=(12,6))
df_top10.plot(kind='bar')
plt.xlabel('Players', fontweight='bold')
plt.ylabel('Points', fontweight='bold')
plt.title('Top 10 Players from 1947-2025', fontweight='bold')
plt.xticks(rotation=30, ha='right')  # rotate the player names
plt.subplots_adjust(bottom=0.25)     # increase space at the bottom 
plt.show()

#b.Visualize the top 5 players in 2025 based on steals using a chart of your choice.
#Top 5
df_players['gameDate'] = pd.to_datetime(df_players['gameDate'], errors='coerce')  #convert to a datetime format
df_players['year'] = df_players['gameDate'].dt.year                               #create a new column named year
df_2025 = df_players.loc[df_players['year'] == 2025]                              #filter by year
df_top5 = df_2025.groupby('fullName')['steals'].sum().sort_values(ascending=False).head(5)
print(f'\nTop 5 Players in 2025 Based on Steals:\n{df_top5}')

#Horizontal bar chart
plt.figure(figsize=(12,6))
df_top5.plot(kind='barh')
plt.xlabel('Steals', fontweight='bold')
plt.ylabel('Players', fontweight='bold')
plt.title('Top 5 Players in 2025 Based on Steals', fontweight='bold')
plt.subplots_adjust(left=0.25)       # increase space on the left
plt.gca().invert_yaxis()             # show the highest score at the top 
plt.show()

#c.Using a line chart, display the total number of points scored in each year from 2015 -2025
#Calculate the total number of points per year
df_years = df_players.loc[                                #filter by range of years
             (df_players['year'] >= 2015) &
             (df_players['year'] <= 2025)
             ]
df_points_year = df_years.groupby('year')['points'].sum()                     
print(f'\nTotal Number of Points Scored in Each Year From 2015 -2025:\n{df_points_year}')

#Line chart
plt.figure(figsize=(12,6))
df_points_year.plot(kind='line')
plt.xlabel('Year', fontweight='bold')
plt.ylabel('Points', fontweight='bold')
plt.title('Total Number of Points Scored in Each Year From 2015 -2025', fontweight='bold')
plt.show()

#d.Canadian, Shai Gilgeous-Alexander was the MVP for 2025, display his total points for 2025
df_mvp = df_players.loc[
               (df_players['personId'] == 1628983) &              #filter by player
               (df_players['year'] == 2025)                       #filter by year
                   ]
total_mvp = df_mvp['points'].sum()
print('\nTotal points for Shai Gilgeous-Alexander in 2025:', total_mvp)


#--------------------------------------------------------------------------
#5.Games Analysis
#a.Display in a dataframe, the top 3 games with the highest attendance,
#include the hometeamName and awayteamName.
df_top3 = df_games.sort_values(by='attendance', ascending=False).head(3)
df_top3 = df_top3[['hometeamName', 'awayteamName', 'attendance']]
print(f'\nTop 3 Games with the Highest Attendance:\n{df_top3}')

#b.Using a pie chart display the winning percentage of the top 5 teams in 2025
#(the rest should be considered as “Others” – meaning the pie chart should have 6 pies)
df_games['gameDate'] = pd.to_datetime(df_games['gameDate'], errors='coerce')    #convert to a datetime format
df_games['year'] = df_games['gameDate'].dt.year                                 #create a new column named year

#Filter by year 2025
df_2025 = df_games[df_games['year'] == 2025]                                               

#Create a dictionary for the team names which played in 2025
df_teams = df_2025[['hometeamId','hometeamName']].drop_duplicates().sort_values('hometeamId')
print(f'\nTeam names:\n{df_teams}')

#Count the number of wins and get the top 5
df_top5teams_all = df_2025['winner'].value_counts()
df_top5teams = df_top5teams_all.head(5).reset_index()                                                                                             
df_top5teams.columns = ['hometeamId', 'wins']                               #rename columns

others_wins = df_top5teams_all.iloc[5:].sum()                               #calculate 'Others' group
df_top5teams = df_top5teams.merge(df_teams, on='hometeamId', how='left')    #merge the winner IDs with the corresponding team names

#Add Others group to the final dataframe
df_others = pd.DataFrame({                                                  #create 'Others' line in a dataframe
    'hometeamId': [None],                                             
    'wins': [float(others_wins)],  
    'hometeamName': ['Others']
})

df_top5teams = pd.concat([df_top5teams, df_others], ignore_index=True)      #add Others group to the final dataframe
print(f'\nTop 5 Teams in 2025:\n{df_top5teams}')


#Create the pie
plt.figure(figsize=(12,6))
plt.pie(df_top5teams['wins'], labels=df_top5teams['hometeamName'], autopct='%1.1f%%')
plt.title('Top 5 Teams in 2025')
plt.show()
















