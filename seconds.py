from utilities import get_user_input

def get_number_of_values():
    """
    Asks the user how many numbers they want to enter.

    Returns:
        int: The validated number of values, between 5 and 20.
    """

    #the user hasnt entered a vaule yet so the number of values is set to 0
    number_of_values = 0;


    # checks if the number of values is within the allowed range
    while number_of_values < 5 or number_of_values > 20:

        print("Please enter a whole number between 5 and 20.")

        number_of_values = int(get_user_input(
            "How many values will be in your list: ", False
        ))

    # converts the number of values into an integer
    return number_of_values


def get_numbers(number_of_values):
    """
    Collects a specified number of floating-point values.

    Args:
        number_of_values (int): The number of values to collect.

    Returns:
        list: A list containing the numbers entered by the user.
    """

    # creates an empty list to store the numbers
    numbers = []

    # asks the user to enter each number
    for i in range(number_of_values):

        # gets a number from the user
        value = get_user_input("Enter value {}: ".format(i + 1), True)

        # adds the number to the list
        numbers.append(value)

    return numbers


def find_second_values(numbers):
    """
    Finds the second smallest and second largest values.

    Args:
        numbers (list): The list of floating-point numbers.

    Returns:
        tuple: The second smallest and second largest values.
    """

    # sorts the numbers from smallest to largest
    sorted_numbers = sorted(numbers)

    # gets the second smallest and second largest values
    second_smallest = sorted_numbers[1]
    second_largest = sorted_numbers[-2]

    return second_smallest, second_largest


def display_results(second_smallest, second_largest):
    """
    Displays the second smallest and second largest values.

    Args:
        second_smallest (float): The second smallest value.
        second_largest (float): The second largest value.

    Returns:
        None
    """

    # displays the results
    print("The second largest value in your list is: {}".format(second_largest))
    print("The second smallest value in your list is: {}".format(second_smallest))

def main():
    """
    Runs the seconds program.

    Gets a list of numbers from the user and displays
    the second smallest and second largest values.
    """

    number_of_values = get_number_of_values()
    numbers = get_numbers(number_of_values)

    second_smallest, second_largest = find_second_values(numbers)

    display_results(second_smallest, second_largest)


if __name__ == "__main__":
    main()