import turtle


class Button:
    """
    Button class is used to present button in game.
    """

    def __init__(self, file_name, center_x, center_y, width, height):
        """
        FUNCTION - __init__()
        This function is the constructor。

        PARAMETERS:
        File_name -- a string.
        center_x -- an int. The x coordinate of button center.
        center_y -- an int. The y coordinate of button center.
        width - an int. The width of button
        height - an int. The height of button

        RETURNS:
        None
        """
        self.file_name = file_name
        self.center_x = center_x
        self.center_y = center_y
        self.width = width
        self.height = height
        self.button_pen = turtle.Turtle()

    def draw(self, screen: turtle.Screen):
        """
        FUNCTION -draw()
        This function is to draw the button

        PARAMETERS:
        screen -- a Screen instance.

        RETURNS:
        None
        """
        screen.register_shape(self.file_name)
        self.button_pen.shape(self.file_name)
        self.button_pen.penup()
        self.button_pen.setpos(self.center_x, self.center_y)
        self.button_pen.pendown()
        screen.update()

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
        if (self.center_x - 0.5 * self.width) <= x <= (
                self.center_x + 0.5 * self.width) and (
                self.center_y - 0.5 * self.height) <= y <= (
                self.center_y + 0.5 * self.height):
            return True
        else:
            return False
