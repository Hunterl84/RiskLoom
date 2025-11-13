# Bond Calculations


def QuikBondCalc(quantity: int, market_value: float, coupon: float, YTM: float, years_to_maturity: int, payment: str):
    """ This is to calculate the return on a bond at the time of investing

        Quanitity, interager showing how many bonds are bought

        face_value, float that is in percent. For example 101 → $1,010

        Coupon, float 
    """

    # Annual / Basic Variables
    coupon_rate = (coupon / 100)
    cash_flow = coupon_rate * 1000
    discount_rate = (YTM / 100)
    mv = market_value * 10
    total_pv = 0
    current_time = 1

    # Semi Anuual Variables
    semi_payments = years_to_maturity * 2
    semi_cf = cash_flow / 2
    semi_discount = discount_rate / 2

    # Quarterly Variables
    quar_pay = years_to_maturity * 4
    quar_cf = cash_flow / 4
    quar_dis = discount_rate / 4

    # Monthly Variables
    mon_pay = years_to_maturity * 12
    mon_cf = cash_flow / 12
    mon_dis = discount_rate / 12

    match payment:

        case "annual":
            while  current_time <= years_to_maturity:
                pv = cash_flow / ((1 + discount_rate)**current_time)
                total_pv += pv
                current_time += 1
                # print(f"Current year: {(current_time-1)}")
                # print(f"Current value of {payment} payments: {total_pv}")
            pv = 1000 / ((1 + discount_rate) ** years_to_maturity)
            total_val = (pv * quantity) + (total_pv * quantity)
            profit = (total_val * quantity) - (mv * quantity)
            print(f"Total Payments: {current_time-1}")
            print(f"Total value of {payment} payments per Bond: ${total_pv}")
            print(f"Present value of one Bond: ${round(pv,2)}")
            print(f"Total value of {quantity} Bonds: ${round(total_val,2)}")
            print(f"Market value of one Bond: ${round(mv,2)}")
            print(f"Total Profit of {quantity} Bonds: ${round(profit,2)}")

            
        case "semi":
            while current_time <= semi_payments:
                payment_pv = semi_cf / ((1 + semi_discount)**current_time)
                total_pv += payment_pv
                current_time += 1
                # print(f"Current payment: {(current_time-1)}")
                # print(f"Current value of {payment} annual payments: {total_pv}")

            pv = 1000 / ((1 + semi_discount)**semi_payments)
            total_val = (pv * quantity) + (total_pv * quantity)
            profit = (total_val * quantity) - (mv * quantity)
            print(f"Total Payments: {current_time-1}")
            print(f"Total value of {payment} annual payments per Bond: ${total_pv}")
            print(f"Present value of one Bond: ${round(pv,2)}")
            print(f"Total value of {quantity} Bonds: ${round(total_val,2)}")
            print(f"Market value of one Bond: ${round(mv,2)}")
            print(f"Total Profit of {quantity} Bonds: ${round(profit,2)}")


        case "quarterly":
            while current_time <= quar_pay:
                pv = quar_cf / ((1 + quar_dis)**current_time)
                total_pv += pv
                current_time += 1
                # print(f"Current year: {(current_time-1)}")
                # print(f"Current value of {payment} payments: {total_pv}")
            pv = 1000 / ((1+ quar_dis) ** quar_pay)
            total_val = (pv * quantity) + (total_pv * quantity)
            profit = (total_val * quantity) - (mv * quantity)
            print(f"Total Payments: {current_time-1}")
            print(f"Total value of {payment} payments per Bond: ${total_pv}")
            print(f"Present value of one Bond: ${round(pv,2)}")
            print(f"Total value of {quantity} Bonds: ${round(total_val,2)}")
            print(f"Market value of one Bond: ${round(mv,2)}")
            print(f"Total Profit of {quantity} Bonds: ${round(profit,2)}")

        case "monthly":
            while current_time <= mon_pay:
                pv = mon_cf / ((1 + mon_dis)**current_time)
                total_pv += pv
                current_time += 1
                print(f"Current year: {(current_time-1)}")
                print(f"Current value of {payment} payments: {total_pv}")
            pv = 1000 / ((1 + mon_pay) ** mon_pay)
            total_val = (pv * quantity) + (total_pv * quantity)
            profit = (total_val * quantity) - (mv * quantity)
            print(f"Total Payments: {current_time-1}")
            print(f"Total value of {payment} payments per Bond: ${total_pv}")
            print(f"Present value of one Bond: ${round(pv,2)}")
            print(f"Total value of {quantity} Bonds: ${round(total_val,2)}")
            print(f"Market value of one Bond: ${round(mv,2)}")
            print(f"Total Profit of {quantity} Bonds: ${round(profit,2)}")



        case _ : 
            print("Unkown Command for payment")