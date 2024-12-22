import csv
import numpy as np
import pandas as pd
from scipy import signal


if __name__ == "__main__":
    df_rio = pd.read_csv('anuales.csv')
    df_rio = df_rio.iloc[:114]
    df_sol = pd.read_csv('manchas_solares_anuales.csv', delimiter=';')
    df_sol = df_sol.iloc[210:]
    print(df_rio)
    print(df_sol)
    # signal.correlate(df_rio, df_sol)
    array_rio = df_rio[["Derrame"]].to_numpy()
    # print(array_rio)
    array_sol = df_sol[["manchas"]].to_numpy()
    print(len(array_rio))
    print(len(array_sol))
    print(signal.correlate(array_rio, array_sol))