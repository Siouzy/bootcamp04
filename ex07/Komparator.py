import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn
import pandas as pd
import scipy as sp
from MyPlotLib import MyPlotLib
from FileLoader import FileLoader


class Komparator:

    def __init__(self, df):
        self.df = df

    def compare_box_plot(self, categorical_var, numerical_var):
        df = self.df
        mpl = MyPlotLib()
        categories = list(df[categorical_var].unique())
        df.drop(categories, axis=1, errors='ignore')
        for cat in categories:
            mask = df[categorical_var] == cat
            df[cat] = df[mask][numerical_var]
        mpl.box_plot(df, categories)

    def density(self, categorical_var, numerical_var):
        df = self.df
        mpl = MyPlotLib()
        categories = list(df[categorical_var].unique())
        df.drop(categories, axis=1, errors='ignore')
        for cat in categories:
            mask = df[categorical_var] == cat
            df[cat] = df[mask][numerical_var]
        mpl.density(df, categories)

    def compare_histograms(self, categorical_var, numerical_var):
        df = self.df
        mpl = MyPlotLib()
        categories = list(df[categorical_var].unique())
        df.drop(categories, axis=1, errors='ignore')
        for cat in categories:
            mask = df[categorical_var] == cat
            df[cat] = df[mask][numerical_var]
        mpl.histogram(df, categories)


if (__name__ == '__main__'):
    fl = FileLoader()
    df = fl.load('athlete_events.csv')
    k = Komparator(df)
    k.compare_box_plot('Year', 'Height')
    k.density('Year', 'Height')
    k.compare_histograms('Year', 'Height')
