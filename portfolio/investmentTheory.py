import yfinance as yf
import pandas as pd


def CAPM(risk_free_rate:float, beta:float, expected_market_return:float, expected_investment_return:float, FIND:str):
    """
    Capital Asset Pricing Model (CAPM) calculator.

    Parameters:
    -----------
    risk_free_rate : float
        Risk-free rate as a percentage (e.g., 6 for 6%).
    beta : float
        Beta of the asset.
    expected_market_return : float
        Expected market return as a percentage (e.g., 16 for 16%).
    expected_investment_return : float
        Expected return of the investment as a percentage (e.g., 20 for 20%).
    find : str
        Variable to calculate. Options:
        - "risk free"
        - "beta"
        - "expected investment return"
        - "expected market return"

    Returns:
    --------
    float
        The calculated value of the requested variable. Returns percentage for rates.
    """


    rf = (risk_free_rate / 100)
    b = beta
    rm = (expected_market_return / 100)
    er = (expected_investment_return / 100)

    match FIND:

        case "risk free":
            rf = (er - (b * rm))/(1-b)
            rf = rf * 100
            print(f"risk free rate = {round(rf, 2)} %")

        case "beta":
            b = (er - rf)/(rm - rf)
            print(f"beta = {round(b, 2)}")
        
        case "expected investment return":
            ra = rf + b * (rm - rf)
            ra = ra * 100
            print(f"expected investment return = {round(ra, 2)} %")

        case "expected market return":
            rm = ((er - rf) / b) + rf
            rm = rm * 100
            print(f"expected market return = {round(rm, 2)} %")

        case _ : 
            print("Unkown Command for payment")



# def porftolioER(file:str, file_type:str):   #TODO: Fix the system and make sure the calculations are correct. 

#     """ This is to test the porftlio ER
    
#     Structure your file like this, Column A = Ammount put into stock, Column B = Expected Returns"""
#     match file_type:


#         case "xlsx":

#             data = pd.read_excel(file, header=None)
#             print(data.shape)
#             print(data)

#             invested = data[0]
#             er = data[1]
#             print(sum(invested*er))

#         case "csv":
#             data = pd.read_csv(file, header=None)
#             print(data.shape)
#         case _:
#             print("Invalid file type")
#     return    

