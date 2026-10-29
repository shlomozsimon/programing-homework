# Ask the user for the amount they want to invest
while True:
    userInput = input("Enter the amount you want to invest: ")

    try:
        # Convert the user's input into a float
        principal = float(userInput)

        # Make sure the investment isn't negative
        if principal < 0:
            print("Please enter a non-negative amount.")
            continue

        # Exit the loop if the input is valid
        break

    except ValueError:
        print("Please enter a valid number.")


# Ask the user for the annual interest rate
while True:
    userInput = input("Enter the annual interest rate (as a percentage): ")

    try:
        annual_interest_rate = float(userInput)

        if annual_interest_rate < 0:
            print("Please enter a non-negative interest rate.")
            continue

        # Convert percentage to decimal
        annual_interest_rate = annual_interest_rate / 100

        break

    except ValueError:
        print("Please enter a valid number.")


# Ask the user for the number of years
while True:
    userInput = input("Enter the number of years: ")

    try:
        years = int(userInput)

        if years < 0:
            print("Please enter a non-negative number of years.")
            continue

        break

    except ValueError:
        print("Please enter a whole number.")


# Start with the original investment
totalEarnings = principal

# Calculate compound interest for each year
for i in range(years):
    totalEarnings = totalEarnings * (1 + annual_interest_rate)


# Display the final amount
print("After", years, "years, your investment will be worth $", totalEarnings)