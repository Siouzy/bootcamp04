from FileLoader import FileLoader


def youngestFellah(df, year):
    mask_m = (df.Year == year) & (df.Sex == 'M')
    mask_f = (df.Year == year) & (df.Sex == 'F')
    ym = df[mask_m]['Age'].min()
    yw = df[mask_f]['Age'].min()

    return {'youngest woman': ym, 'youngest man': ym}


if (__name__ == '__main__'):
    fl = FileLoader()
    df = fl.load('athlete_events.csv')
    print(youngestFellah(df, 2004))
