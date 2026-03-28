## Monte Carlo portfolio simulation
import pandas as pd
# import numpy as np
import random
import plotly.express as pe

def monteCarlo(file : str, numSims : int, risk : float):

    finalRisk = risk / 100
    argFile = pd.read_csv(file)
    df = pd.DataFrame(argFile)
    quickDF = pd.DataFrame(columns=("Company", "Value"))

    print("Initial Investments")
    print(df)
    print("Temp: ", quickDF)

    valueSum = df['Value'].sum()
    compSum = df['Company'].count()

    #   This is the start of the simulation 
    print("Starting Monte Carlo Simulation")
    print("Total Number of Simulations: ", numSims)
    print("Total Number of Companyies: ", compSum)  # find the final number of companies
    print("Total Value: $", valueSum)

    start = 0
    while start < numSims:

        start += 1
        print("Sim Number: ", start)

        for x, y in df.itertuples(index=False):

            change = y * finalRisk
            finalValue = random.uniform(a=(y + change), b=(y - change))
            quickDF.loc[len(quickDF)] = [x, finalValue]

            # print("Company: ", x) # Debugging
            # print("Original Number:", y)  # Debugging
            # print("Final Value: ", finalValue)    #Debugging

    print("Checking Values: \n", quickDF)

    fig = pe.histogram(y=("Company"), x="Value")
    fig.show()

            






    

            
    



monteCarlo(file=r"test.csv",numSims=20, risk=20)