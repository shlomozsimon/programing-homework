# runs the code so that it doesn't crash if the user inputs a non-integer value
try:
    #stores the user input as an integer
    n = int(input("Enter a non-negative integer: "))

    #makes sure that the user input is a non-negative integer
    if n < 0:
        print("Invalid input. Please enter a non-negative integer.")
    else:
        #stores the sum of natural numbers in a variable
        sum_of_natural_numbers = 0

        #loops through the range of numbers from 0 to n where n is the user input and adds them to the sum_of_natural_numbers variable
        for i in range(n + 1):
            sum_of_natural_numbers += i

        #prints the sum of natural numbers
        print("The sum of the first", n, "natural numbers is", sum_of_natural_numbers)

# catches the ValueError if the user inputs a non-integer value
except ValueError:
    print("Invalid input. Please enter a valid integer.")
