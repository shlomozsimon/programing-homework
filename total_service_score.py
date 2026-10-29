import utilities

def main():
    # get user input for the number of days of scores
    number_of_days = int(utilities.get_user_input("How many days of scores? ", False))
    toatal_score = 0

    # loop through the number of days and get the score for each day
    for day in range(1, number_of_days + 1):
        score = int(utilities.get_user_input(f"Enter the score for day {day}: ", True))
        #adds up the scores for each day to get the total score
        toatal_score += score

    # prints the total score to the user
    print(f"The total score for {number_of_days} days is: {toatal_score}")

# check to see if we have only one main module running, if so run the main function
if __name__ == "__main__":
    main()