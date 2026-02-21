## Monte Carlo portfolio simulation
import pandas as pd
import numpy as np
import random

def monteCarlo(file : str, numSims : int, risk : float):

    finalRisk = risk / 100
    argFile = pd.read_csv(file)
    df = pd.DataFrame(argFile)

    print("Initial Investments")
    print(df)

    valueSum = df['Value'].sum()
    valueColm = df['Value']

    print("Total Value: $", valueSum)

    start = 0
    while start < numSims:
        start += 1
        print("Sim Number: ", start)
        for y in valueColm:
            print("Original Number:", y)
            change = y * finalRisk
            finalValue = random.uniform(a=(y + change), b=(y - change))
            print("Final Value: ", finalValue)
            




monteCarlo(file=r"test.csv",numSims=20, risk=20)