from utilities import get_user_input


def main():
    # Get the person's age and years of citizenship
    age = int(get_user_input("Enter your age: ", False))
    citizenship = int(get_user_input("Enter years of US citizenship: ", False))

    # Check eligibility for the Senate
    if age >= 30 and citizenship >= 9:
        print("You are eligible to be a US Senator.")
    else:
        print("You are not eligible to be a US Senator.")

    # Check eligibility for the House of Representatives
    if age >= 25 and citizenship >= 7:
        print("You are eligible to be a US Representative.")
    else:
        print("You are not eligible to be a US Representative.")


if __name__ == "__main__":
    main()