from FileLoader import FileLoader
import pandas as pd


def get_medals_sum(x, df, c, color):
    year = x['Year']
    return df.loc[df['Year'] == year].loc[df['Medal'] == color].count()


def howManyMedalsByCountry(df, country):
    df_filtered = df.loc[df['Team'] == country].loc[df['Medal'] != 'NaN']
    new_df = pd.DataFrame(columns=['Year', 'G', 'S', 'B'])
    new_df['Year'] = df_filtered['Year']
    new_df.drop_duplicates('Year', inplace=True)
    df_filtered.drop_duplicates(
        ['Year', 'Event', 'Sport', 'Medal'], inplace=True)
    df_gold = df_filtered.loc[df['Medal'] == 'Gold']
    df_filtered.sort_index(inplace=True)
    new_df.sort_index(inplace=True)
    new_df['G'] = new_df.apply(lambda x: get_medals_sum(
        x, df_filtered, 'G', 'Gold'), axis=1)
    new_df['S'] = new_df.apply(lambda x: get_medals_sum(
        x, df_filtered, 'S', 'Silver'), axis=1)
    new_df['B'] = new_df.apply(lambda x: get_medals_sum(
        x, df_filtered, 'B', 'Bronze'), axis=1)
    dic = new_df.set_index('Year').to_dict(orient='index')
    return dic
