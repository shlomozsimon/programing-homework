H = 1.00794   # weight of hydrogen
C = 12.0107   # weight of carbon
O = 15.9994   # weight of oxygen

#an infinite loop to keep asking for input until valid numbers are provided
while True:
    #make sure that the code doesnt crash if the user inputs a non-numeric value
    try:
        inputH = float(input("Enter the number of hydrogen: "))
        inputC = float(input("Enter the number of carbon: "))
        inputO = float(input("Enter the number of oxygen: "))
        #exit the loop if all inputs are valid numbers
        break
    #runs this code if the user inputs a non-numeric value
    except ValueError:
        print("Please enter a valid number.")

#calculate the molecular weight using the formula
molecular_weight = inputH * H + inputC * C + inputO * O

#print the result
print("The molecular weight is:", molecular_weight)