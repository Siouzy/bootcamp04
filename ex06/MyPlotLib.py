import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn
import pandas as pd
import scipy as sp
from FileLoader import FileLoader


class MyPlotLib:

    def histogram(self, data, features):
        fig, axes = plt.subplots(ncols=len(features), nrows=1)
        for i, feat in enumerate(features):
            axe = plt.subplot(data[feat].hist(ax=axes[i]))
            axe.set_title(feat)
        plt.show()

    def density(self, data, features):
        for i, feat in enumerate(features):
            axe = plt.subplot(data[feat].plot.density())
            axe.legend()
        plt.show()

    def pair_plot(self, data, features):
        seaborn.set(style="ticks", color_codes=True)
        g = seaborn.pairplot(data, vars=features)
        plt.show()

    def box_plot(self, data, features):
        pd.plotting.boxplot(data, features)
        plt.show()


if (__name__ == __main__):
    mpl = MyPlotLib()
    fl = FileLoader()
    df = fl.load('athlete_events.csv')

    mpl.histogram(df, ['Height', 'Weight'])
    mpl.density(df, ['Height', 'Weight'])
    mpl.pair_plot(df, ['Height', 'Weight'])
    mpl.box_plot(df, ['Height', 'Weight'])
