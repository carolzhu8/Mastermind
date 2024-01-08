import turtle


class Peg:
    """
    Peg class is used to present peg in game.
    """
    def __init__(self, x, y):
        """
        FUNCTION - __init__()
        This function is the constructor。

        PARAMETERS:
        x -- an int. The x coordinate of peg.
        y -- an int. The y coordinate of peg.

        RETURNS:
        None
        """
        self.x = x
        self.y = y
        # 0 wrong color 1 right color wrong position 2 right color right position
        self.situation = 0
        self.color = ""
        self.radius = 10
        self.peg_pen = turtle.Turtle()
        self.peg_pen.hideturtle()

    def set_situation(self, situation):
        """
        FUNCTION - set_situation()
        This function is to set the situation of peg

        PARAMETERS:
        situation -- an int.

        RETURNS:
        None
        """
        self.situation = situation  # pass the situation in
        self.convert_situation_to_color(situation)  # call convert function

    def draw(self):
        """
        FUNCTION -draw()
        This function is to draw the peg

        PARAMETERS:
        None

        RETURNS:
        None
        """
        self.peg_pen.clear()
        self.peg_pen.penup()
        self.peg_pen.setpos(self.x, self.y - self.radius)
        self.peg_pen.pendown()
        self.peg_pen.pencolor("black")
        self.peg_pen.fillcolor(self.color)
        self.peg_pen.begin_fill()
        self.peg_pen.circle(self.radius)
        self.peg_pen.end_fill()
    def convert_situation_to_color(self, situation):
        """
        FUNCTION - convert_situation_to_color()
        This function is to convert situation to color.

        PARAMETERS:
        situation -- an int.

        RETURNS:
        A string of colro.
        """
        if situation == 0:
            self.color = ""
            return
        if situation == 1:
            self.color = "red"
            return
        if situation == 2:
            self.color = "black"
            return

