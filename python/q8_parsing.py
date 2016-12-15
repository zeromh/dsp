# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import pandas as pd

df = pd.read_csv('football.csv')
df.columns = [n.lower().replace(' ','_') for n in list(df)]

heading = 'The team with the smallest difference between "for" and \
"against" goals is:'
print heading, df.assign(goals_diff = abs(df.goals - df.goals_allowed)). \
    sort_values('goals_diff').team[0]
