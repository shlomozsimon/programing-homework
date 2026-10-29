from graphics import *

WINDOW_TITLE = "Graphics Demostration"

# define constants that will determine sizes and locations
WINDOW_WIDTH  = 400
WINDOW_HEIGHT = 500

RECT1_LEFT   = 200 + 50
RECT1_TOP    = 40 + 250
RECT1_WIDTH  = 50
RECT1_HEIGHT = 30

# right side of rect2 will always be 2 pixels to the left of rect1
RECT2_RIGHT = RECT1_LEFT - 2

# top of rect2 will always be the same as top of rect1
RECT2_TOP = RECT1_TOP

# width of rect2 will alway be 20 less than width of rect1
RECT2_WIDTH = RECT1_WIDTH - 20

# height of rect2 will always be the same as the height of rect1
RECT2_HEIGHT = RECT1_HEIGHT

# create a graphics window in which to draw my elements
win = GraphWin(WINDOW_TITLE, WINDOW_WIDTH, WINDOW_HEIGHT)

# create the points that define the two rectangles
rect1_upper_left  = Point(RECT1_LEFT, RECT1_TOP)
rect1_lower_right = Point(RECT1_LEFT + RECT1_WIDTH, RECT1_TOP + RECT1_HEIGHT)

rect2_upper_right = Point(RECT2_RIGHT, RECT2_TOP)
rect2_lower_left  = Point(RECT2_RIGHT - RECT2_WIDTH, RECT2_TOP + RECT2_HEIGHT)
    
# create two side-by-side rectangles
rect1 = Rectangle(rect1_upper_left, rect1_lower_right)
rect2 = Rectangle(rect2_upper_right, rect2_lower_left)

# establish their coloring
rect1.setFill("red")
rect1.setOutline("blue")

rect2.setFill("yellow")
rect2.setOutline("green")

# draw the rectangles
rect1.draw(win)
rect2.draw(win)

# wait for the user to click in the window before closing the window and ending the program
point_of_click = win.getMouse()
win.close()