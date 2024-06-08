from decimal import Decimal

Decimal(90.000000000007789988)

accounts = ["2022012341", "2022012342", "2022012343", "2022012344", "2022012345"]

capital=500

acc_= input( "Which account would you like to deposit into?")
if acc_ not in accounts:
    print("Acconut is invalid")
else:
    print("Account validated")

    amount = input("How much would you like to deposit?")
    if float(amount) <= 0:
        print("Invalid amount")
    else:
        total = capital + float(amount)
        print(total)