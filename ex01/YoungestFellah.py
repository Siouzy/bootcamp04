from FileLoader import FileLoader

def youngestFellah(df, year):
    yw = df.loc[df['Year'] == year].loc[df['Sex'] == 'F']['Age'].apply(lambda x: float(x)).min()
    ym = df.loc[df['Year'] == year].loc[df['Sex'] == 'M']['Age'].apply(lambda x: float(x)).min()

    return {'youngest woman' : ym, 'youngest man' : ym}

fl = FileLoader()
df = fl.load('athlete_events.csv')
print(youngestFellah(df, 2004))
