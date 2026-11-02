# importing the sys module to use sys.exit() for exiting the program in case of errors
import sys
import csv


# this is a function that takes in a str that prompts the user and a bool value which determines whether or not the answer can be negative and returns a float.
def get_user_input(input_prompt, can_be_negative):

    # this is a stop sign (programing humor)
    while True:
        # this is also a stop sign (more programing humor)
        try:
            # stores the user input in a variable
            user_input = float(input(input_prompt))

            # checks if the user input is a valid number and if it can be negative or not
            if not can_be_negative and user_input < 0:
                print("please enter a non negative number.")
                continue

            # even more stop sign
            return user_input
        
        except ValueError:
            print("please enter a valid number.")
            continue


# this is a function that takes in a string that prompts the user and returns a string.
def ask_user_str(input_prompt):

    while True:

        user_input = input(input_prompt)

        # checks if the user has left the input blank
        if user_input.strip() == "":
            print("please enter a valid string.")
            continue

        return user_input
    
# this is a function that takes in a prompt and a list of valid choices and returns the user's choice. (important note: the user's choice is converted to lowercase before being returned and valid_choices must also be in lowercase)
def get_user_choice(input_prompt, valid_choices):

    while True:

        # stores the user input in a variable
        user_input = input(input_prompt)

        # checks if the user's input is one of the valid choices
        if user_input.lower() in valid_choices:
            return user_input.lower()

        # tells the user if their choice is invalid
        print("ERROR: Please enter one of the following choices: {}".format(", ".join(valid_choices)))

# this is a function that takes in a string that prompts the user and returns a file object
def get_file(file_prompt):

    file_name = input(file_prompt)

    # this is a try-except block that attempts to open the file and returns the file object if successful, or prints an error message and exits the program if not.
    try:
        # try to open the file for reading
        file = open(file_name, "r")
        return file

    # this is the except block that handles the case where the file could not be found or the user does not have permission to open the file.
    except FileNotFoundError:
        # tell the user if the file could not be found
        print("Error: file not found. Please try again.")
        sys.exit(1)

    # this is the except block that handles the case where the user does not have permission to open the file.
    except PermissionError:
        # tell the user if they cannot access the file
        print("Error: you do not have permission to open this file.")
        sys.exit(1)



# this is a function that takes in a file name and returns a list of dictionaries from a csv file
def get_csv_file(file_name):

    # try to open and read the csv file
    try:
        with open(file_name, "r", newline="") as file:

            # read the csv file as a list of dictionaries
            csv_reader = csv.DictReader(file)

            # return all the records
            return list(csv_reader)

    except FileNotFoundError:
        print("Error: file not found.")
        sys.exit(1)

    except PermissionError:
        print("Error: you do not have permission to open this file.")
        sys.exit(1)