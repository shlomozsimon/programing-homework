#an infinit while loop
while True:
    #here we ask for user input
    userInput = input("Enter the amount of bitcoin: ")
    #try is used to salfy run this code without crashing incase the user would input a string causing a ValueError
    try:
        #converting the sstring input to a float
        bitcoinAmount = float(userInput)
        #making sure the user input is not negative
        if bitcoinAmount < 0:
            print("Please enter a non-negative amount.")
            #continue will restart the loop if the user inputs a negative number
            continue
        #exits the loop if the input is valid
        break
    #if user inputs an invalid input such as a string, this will catch the error and print a message and will allow the code to keep running
    except ValueError:
        print("Please enter a valid number.")
#calculating the final amount in USD by multiplying the bitcoin amount by the current price of bitcoin in USD
finalAmount = bitcoinAmount * 79936.30 # pulled the current bitcoin price from coinbase.com at 1:43pm on 9/6/2026
#printing the final amount in USD
print("The amount in USD is: $" + str(finalAmount))

