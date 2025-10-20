# P3LAB_CooperLakeshia
# This program converts a money amount into the most efficient combination
# of dollars, quarters, dimes, nickels, and pennies.

# Get user input
amount = float(input("Enter the amount of money as a float: $"))

# Convert amount to cents
cents = int(round(amount * 100))

# Handle no change case
if cents == 0:
    print("No change")
else:
    # Dollars
    dollars = cents // 100
    cents = cents % 100

    # Quarters
    quarters = cents // 25
    cents = cents % 25

    # Dimes
    dimes = cents // 10
    cents = cents % 10

    # Nickels
    nickels = cents // 5
    cents = cents % 5

    # Pennies
    pennies = cents

    # Output results
    if dollars > 0:
        print(f"{dollars} Dollar" if dollars == 1 else f"{dollars} Dollars")

    if quarters > 0:
        print(f"{quarters} Quarter" if quarters == 1 else f"{quarters} Quarters")

    if dimes > 0:
        print(f"{dimes} Dime" if dimes == 1 else f"{dimes} Dimes")

    if nickels > 0:
        print(f"{nickels} Nickel" if nickels == 1 else f"{nickels} Nickels")

    if pennies > 0:
        print(f"{pennies} Penny" if pennies == 1 else f"{pennies} Pennies")