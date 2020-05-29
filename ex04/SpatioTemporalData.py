from FileLoader import FileLoader
import pandas as pd


class SpatioTemporalData:

    def __init__(self, df):
        self.df = df

    def when(self, location):
        df = self.df
        new_df = df.loc[df['City'] == location]['Year'].drop_duplicates()
        return list(new_df.to_dict().values())

    def where(self, date):
        df = self.df
        new_df = df.loc[df['Year'] == date].drop_duplicates('City')
        return list(new_df['City'].to_dict().values())
