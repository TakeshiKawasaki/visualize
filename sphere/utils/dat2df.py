import pandas as pd
import os


def dat2df(file):

    # read as dataframe
    header = ["rx","ry","rz","dummy1","dummy2","dummy3","dummy4"] # this is necessary for visualisation
    df = pd.read_csv(file, sep=" ", names = header)
    
    return df

if __name__ == '__main__':
    df = dat2df('data/coord_temp0.1_phi0.1_cut3.0.dat')

