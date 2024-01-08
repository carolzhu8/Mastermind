import turtle


class Circle:
    """
    Circle class is used to present circle in game.
    """
    def __init__(self, x, y, color):
        """
        FUNCTION - __init__()
        This function is the constructor。

        PARAMETERS:
        x -- an int. The x coordinate of button center.
        y -- an int. The y coordinate of button center.
        color - a string.

        RETURNS:
        None
        """
        self.x = x
        self.y = y
        self.color = color
        self.if_fill = False
        self.radius = 30
        self.circle_pen = turtle.Turtle()
        self.circle_pen.hideturtle()

    def get_x(self):
        """
        FUNCTION - __init__()
        This function is get the x coordinate.

        PARAMETERS:
        None

        RETURNS:
        An int.
        """
        return self.x

    def draw(self):
        """
        FUNCTION -draw()
        This function is to draw the circle

        PARAMETERS:
        screen -- a Screen instance.

        RETURNS:
        None
        """
        self.circle_pen.clear()  # clear previous circle
        self.circle_pen.penup()
        self.circle_pen.setpos(self.x, self.y - self.radius)
        self.circle_pen.pendown()
        self.circle_pen.pencolor("black")
        if self.if_fill:
            self.circle_pen.fillcolor(self.color)
            self.circle_pen.begin_fill()
            self.circle_pen.circle(self.radius)
            self.circle_pen.end_fill()
        else:
            self.circle_pen.circle(self.radius)

    def if_clicked(self, x, y):
        """
        FUNCTION -if_clicked()
        This function is to identify if circle has been clicked.

        PARAMETERS:
        center_x -- an int. The x coordinate of click
        center_y -- an int. The y coordinate of click

        RETURNS:
        A boolean.
        """
        if ((self.x - self.radius) <= x <= (self.x + self.radius) and
                (self.y - self.radius) <= y <= (self.y + self.radius)):
            return True
        else:
            return False
