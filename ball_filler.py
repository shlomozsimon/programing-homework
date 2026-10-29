import utilities
import math

def main():
    # get user input for the number of balls, diameter, and core volume
    amount_of_balls = int(utilities.get_user_input(
        "How many bowling balls will be manufactured? ", False))

    # get user input for the diameter of each ball and the core volume
    diameter = utilities.get_user_input(
        "What is the diameter of each ball in inches? ", False)

    # get user input for the core volume of each ball
    core_volume = utilities.get_user_input(
        "What is the core volume in inches cubed? ", False)

    # calculates the volume of a sphere using the formula (4/3) * pi * r^3
    radius = diameter / 2
    volume = (4 / 3) * math.pi * (radius ** 3)

    # calculates the volume of the shell by subtracting the core volume from the total volume
    filler_volume = volume - core_volume

    # calculates the total filler volume needed for all the balls
    final_calculation = filler_volume * amount_of_balls

    # prints the final calculation to the user
    print("You will need", final_calculation, "inches cubed of filler")


# check to see if we have only one main module running, if so run the main function
if __name__ == "__main__":
    main()
