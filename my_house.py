from graphics import *

#constants:

#canvas dimensions
WINDOW_TITLE = "My House"
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000

#house dimensions
HOUSE_CENTER_X = WINDOW_WIDTH / 2 # this stores the center x value of the house which can then be used to set the points for top left and bottomm right corners of the house
HOUSE_BOTTOM = WINDOW_HEIGHT - 50 # this stores the offset from the bottom of the window to the bottom of the house
HOUSE_WIDTH = 500 # this stores the width of the house
HOUSE_HEIGHT = 250 # this stores the height of the house
HOUSE_LEFT = HOUSE_CENTER_X - HOUSE_WIDTH / 2
HOUSE_RIGHT = HOUSE_CENTER_X + HOUSE_WIDTH / 2
HOUSE_TOP = HOUSE_BOTTOM - HOUSE_HEIGHT

#door dimensions
DOOR_WIDTH = 100
DOOR_HEIGHT = 10
DOOR_LEFT = HOUSE_CENTER_X - DOOR_WIDTH / 2
DOOR_RIGHT = HOUSE_CENTER_X + DOOR_WIDTH / 2
DOOR_TOP = HOUSE_BOTTOM - DOOR_HEIGHT

#window dimensions (note: the pluses are used to offset the window from the top left corner of the house)
WINDOW_SIZE = 60
WINDOW_LEFT = HOUSE_LEFT + 30
WINDOW_RIGHT = WINDOW_LEFT + WINDOW_SIZE
WINDOW_TOP = HOUSE_TOP + 50
WINDOW_BOTTOM = WINDOW_TOP + WINDOW_SIZE

#roof dimensions
ROOF_HEIGHT = 200
ROOF_PEAK_X = HOUSE_CENTER_X
ROOF_PEAK_Y = HOUSE_TOP - ROOF_HEIGHT

#sun dimensions
SUN_RADIUS = 100
SUN_CENTER_X = WINDOW_WIDTH - 100
SUN_CENTER_Y = 100


def main():

    # create the graphics window
    win = GraphWin(WINDOW_TITLE, WINDOW_WIDTH, WINDOW_HEIGHT)

    #draws the house
    house = Rectangle(
        Point(HOUSE_LEFT, HOUSE_TOP),
        Point(HOUSE_RIGHT, HOUSE_BOTTOM)
    )
    house.setFill("lightblue")
    house.setOutline("black")
    house.draw(win)

    #deaws the door
    door = Rectangle(
        Point(DOOR_LEFT, DOOR_TOP),
        Point(DOOR_RIGHT, HOUSE_BOTTOM)
    )
    door.setFill("brown")
    door.setOutline("black")
    door.draw(win)

    #draws the window
    window = Rectangle(
        Point(WINDOW_LEFT, WINDOW_TOP),
        Point(WINDOW_RIGHT, WINDOW_BOTTOM)
    )
    window.setFill("yellow")
    window.setOutline("black")
    window.draw(win)

    #draws the roof (its actualy made up of two lines)
    roof_left = Line(
        Point(HOUSE_LEFT, HOUSE_TOP),
        Point(ROOF_PEAK_X, ROOF_PEAK_Y)
    )
    roof_left.setFill("red")
    roof_left.setWidth(5)
    roof_left.draw(win)

    roof_right = Line(
        Point(ROOF_PEAK_X, ROOF_PEAK_Y),
        Point(HOUSE_RIGHT, HOUSE_TOP)
    )
    roof_right.setFill("red")
    roof_right.setWidth(5)
    roof_right.draw(win)

    #draws the sun
    sun = Circle(
        Point(SUN_CENTER_X, SUN_CENTER_Y),
        SUN_RADIUS
    )
    sun.setFill("yellow")
    sun.setOutline("orange")
    sun.draw(win)

    #creates a label for the house
    label = Text(
        Point(HOUSE_CENTER_X, HOUSE_BOTTOM + 25),
        "My House"
    )
    label.setSize(20)
    label.setStyle("bold")
    label.setTextColor("green")
    label.draw(win)

    # get the user input of a mouse click to run the next line of code, which opens the door
    win.getMouse()

    # opens the door when the person clicks
    door.setFill("green")

    # Wait for another click before closing.
    win.getMouse()
    win.close()


# check to see if we have only one main module running,
if __name__ == "__main__":
    main()