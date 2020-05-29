from FileLoader import FileLoader

def proportionBySport(df, year, sport, gender):
    total_df = df.loc[df['Sex'] == gender].loc[df['Year'] == year]
    total_df = total_df.drop_duplicates('Name')
    for_sport = len(total_df.loc[df['Sport'] == sport])
    return for_sport / len(total_df)


fl = FileLoader()
df = fl.load('athlete_events.csv')
print(proportionBySport(df, 2004, 'Tennis', 'F'))