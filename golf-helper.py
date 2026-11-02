from utilities import get_user_input


def get_golf_information():
    # ask the user if the ball is on the green
    is_on_green = input("Did you hit it on the green (y/n)? ")

    # ask the user how far the ball is from the hole
    distance = get_user_input("How far is the ball from the hole? ", False)

    return is_on_green, distance


def recommend_club(on_green, distance):
    # recommend the putter if the ball is on the green
    if on_green == "y":
        return "Putter"

    # recommend the driver if the distance is 200 or more
    elif distance >= 200:
        return "Driver"

    # recommend the 5-Iron if the distance is between 140 and 200
    elif distance >= 140:
        return "5-Iron"

    # recommend the 9-Iron if the distance is between 100 and 140
    elif distance >= 100:
        return "9-Iron"

    # recommend the pitching wedge for any other distance
    else:
        return "Pitching Wedge"

def main():
    print("Welcome to the Golf Club Helper!")
    print("Tell me your situation, and I'll recommend a club")
    print()

    # get the user's golfing information
    on_green, distance = get_golf_information()

    # get the recommended club
    club = recommend_club(on_green, distance)

    # display the recommended club
    print()
    print("I recommend using your", club)

if __name__ == "__main__":
    main()
