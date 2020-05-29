import pandas as pd


class FileLoader:
    def load(self, path):
        df = pd.read_csv(path)
        print('%d * %d' % df.shape)
        self.df = df
        return df

    def display(self, n):
        if n >= 0:
            print(self.df.iloc[:n])
        else:
            print(self.df.iloc[len(self.df) + n:])
