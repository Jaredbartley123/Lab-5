while True:
    try:
        income = input("Please enter your total income: ")

        income = int(income)

        if income <= 85528:
            tax = income * .18 - 556.02

        elif income > 85528:
            tax = (income - 85528) * .32 + 14839

        if tax < 0:
            tax = 0

        tax = round(tax,0)
        print(tax)

    except(ValueError):
        print("Please enter a valid Base 10 integer")
        continue

    var = input("Would you like to exit? (Y/N)")

    if var == "Y" or var == "y":
        break
