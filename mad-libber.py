# imports the function that asks the user for a string
from utilities import ask_user_str


def main():
    # prints a message that introduces the program as a mad lib maker
    print("Welcome to the Mad Lib Maker!")

    # asks the user for words to fill in the mad lib
    name = ask_user_str("Enter a name: ")
    animal = ask_user_str("Enter an animal: ")
    place = ask_user_str("Enter a place: ")
    verb = ask_user_str("Enter a verb ending in -ing: ")

    # adding a blank line for better readability
    print()

    # stores the story with numbered placeholders for the user's answers
    story = "One day, {0} took a {1} to the {2}. \n At the {2}, the {1} started {3}. \n {0} laughed while the {1} kept {3} all day."

    # replaces the numbered placeholders with the user's answers and prints the story
    print(story.format(name, animal, place, verb))


# checks if this file is the main file being run and if so, runs the main function
if __name__ == "__main__":
    main()