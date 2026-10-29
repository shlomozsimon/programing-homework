from graphics import *


def main():

    # create the graphics window
    win = GraphWin("Rectangle", 600, 500)

    # get the two opposite corners from the user
    point1 = win.getMouse()
    point2 = win.getMouse()

    # calculate the width and height of the rectangle
    width = abs(point2.getX() - point1.getX())
    height = abs(point2.getY() - point1.getY())

    # create and draw the rectangle
    rectangle = Rectangle(point1, point2)
    rectangle.setFill("lightblue")
    rectangle.setOutline("black")
    rectangle.draw(win)

    # calculate the perimeter and area
    perimeter = 2 * (width + height)
    area = width * height

    # print the results
    print("Width:", width)
    print("Height:", height)
    print("Perimeter:", perimeter)
    print("Area:", area)

    # wait for another click before closing
    win.getMouse()
    win.close()


if __name__ == "__main__":
    main()