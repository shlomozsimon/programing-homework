# imports the get_user_input function from utilities
from utilities import get_user_input


def display_instructions():
    """Displays the instructions for the unique list program.

    Returns:
        None
    """

    print("This program tests if the sequence of positive numbers you input are unique")
    print("Enter -1 to quit")


def get_numbers():
    """Collects positive integers from the user until -1 is entered.

    Returns:
        list: A list containing the positive integers entered by the user.
    """

    # creates an empty list to store the numbers
    numbers = []

    # stores the first input prompt
    input_prompt = "Enter the first number: "

    # continues asking for numbers until the user enters -1
    while True:

        # gets a number from the user
        number = int(get_user_input(input_prompt, True))

        # checks if the user wants to quit
        if number == -1:
            break

        # checks if the number is positive
        elif number <= 0:
            print("please enter a positive number.")
            continue

        # adds the number to the list as an integer
        numbers.append(number)

        # changes the prompt for subsequent numbers
        input_prompt = "Next: "

    # returns the completed list
    return numbers


def check_unique(numbers):
    """Checks whether a list contains duplicate values using a set.

    Args:
        numbers (list): The list of numbers to check.

    Returns:
        bool: True if all numbers are unique, otherwise False.
    """

    # converts the list into a set to remove duplicate values
    unique_numbers = set(numbers)

    # returns whether the list and set have the same length
    return len(numbers) == len(unique_numbers)


def display_results(numbers, is_unique):
    """Displays the original sequence and whether it is unique.

    Args:
        numbers (list): The original sequence of numbers.
        is_unique (bool): Whether the sequence contains only unique values.

    Returns:
        None
    """

    # checks if the sequence is unique
    if is_unique:

        # displays the result if all numbers are unique
        print("The sequence {} is unique!".format(numbers))

    else:

        # displays the result if duplicate numbers were found
        print("The sequence {} is NOT unique!".format(numbers))


def main():
    """Runs the unique list program.

    Returns:
        None
    """

    # displays the program instructions
    display_instructions()

    # collects the numbers entered by the user
    numbers = get_numbers()

    # checks whether the numbers are unique
    is_unique = check_unique(numbers)

    # displays the results
    display_results(numbers, is_unique)


# starts the program
if __name__ == "__main__":
    main()