import turtle


class Message:
    """
    Message class is used to present message in game.
    """
    def __init__(self, file_name, center_x, center_y):
        """
        FUNCTION - __init__()
        This function is the constructor。

        PARAMETERS:
        file_name -- a string.
        center_x -- an int. The x coordinate of button center.
        center_y -- an int. The y coordinate of button center.

        RETURNS:
        None
        """
        self.file_name = file_name
        self.center_x = center_x  # location of msg
        self.center_y = center_y
        self.msg_pen = turtle.Turtle()  # create pen for msg
        self.msg_pen.hideturtle()  # hide the msg so it dosent show when no need

    def pop_up(self, screen:turtle.Screen):
        """
        FUNCTION -pop_up()
        This function is pop up the message

        PARAMETERS:
        screen -- a Screen instance.

        RETURNS:
        None
        """
        screen.register_shape(self.file_name)  # save the file to screen
        self.msg_pen.shape(self.file_name)  # change turtle to file shape
        self.msg_pen.penup()
        self.msg_pen.setpos(self.center_x, self.center_y)
        self.msg_pen.showturtle()  # show msg
        self.msg_pen.pendown()
        screen.update()
        screen.ontimer(self.msg_pen.hideturtle, 1000)  # hide msg
        screen.ontimer(screen.update, 1010)