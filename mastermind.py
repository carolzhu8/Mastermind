import random
import turtle
import random

from Message import Message
from button import Button
from circle import Circle
from leaderboard import Leaderboard
from peg import Peg


class Game:
    """
    Game is a class to process the game.
    """
    def __init__(self):
        """
        FUNCTION - __init__()
        This function is the constructor of Game.

        PARAMETERS:
        None

        RETURNS:
        None
        """
        # set up screen instance

        self.sc = turtle.Screen()
        self.sc.screensize(1000, 1000)
        self.sc.setup(1000, 1000)  # window size
        self.sc.setworldcoordinates(0, 0, 1000, 1000)  # change the coordinates
        self.sc.tracer(0)
        self.sc.onclick(self.click)

        # draw background
        self.background_pen = turtle.Turtle()  # create pen
        self.background_pen.hideturtle()
        self.draw_rectangle(50, 200, 600, 730)
        self.draw_rectangle(700, 200, 250, 730)
        self.draw_rectangle(50, 50, 900, 130)
        self.background_pen.penup()
        self.background_pen.setpos(760, 880)
        self.background_pen.pendown()
        self.background_pen.write("Leader", font=("Arial", 30, "bold"))
        self.background_pen.penup()
        self.background_pen.setpos(790, 820)
        self.background_pen.pendown()
        self.background_pen.write("Top 5", font=("Arial", 18, "bold"))

        # create a nested list to store all result circles
        self.result_circles = []
        for i in range(10):
            line = []
            for k in range(4):
                line.append(Circle(100 + 100 * k, 880 - i * 70, ""))
            self.result_circles.append(line)
        self.draw_result_circles()  # draw all result circles

        # create an index to indicate current line
        self.line_index = 0
        self.max_line_index = 9

        # create a list to store all pegs
        self.peg_list = []
        for i in range(10):
            line = []
            for k in range(4):
                line.append(Peg(500 + 30 * k, 880 - i * 70))
            self.peg_list.append(line)
        self.draw_all_pegs()

        # create color database and random colors
        self.color_database = ["red", "blue", "green", "yellow", "purple",
                               "black"]
        self.answer = self.create_answer()

        # create a list to store all selection circles
        self.selection_circles = []
        for i in range(6):
            self.selection_circles.append(
                Circle(100 + 80 * i, 120, self.color_database[i]))
        self.draw_selection_circles()

        # create all buttons.
        self.check_button = Button("checkbutton.gif", 600, 120, 60, 60)
        self.check_button.draw(self.sc)
        self.xbutton = Button("xbutton.gif", 680, 120, 60, 60)
        self.xbutton.draw(self.sc)
        self.quit_button = Button("quit.gif", 840, 120, 200, 112)
        self.quit_button.draw(self.sc)

        # all messages
        self.quit_message = Message("quitmsg.gif", 500, 500)
        self.win_message = Message("winner.gif", 500, 500)
        self.lose_message = Message("Lose.gif", 500, 500)
        self.file_error_message = Message("file_error.gif", 500, 500)

        # get the name from the user
        self.user_name = self.get_user_name().upper()
        self.sc.update()

        # create leaderboard
        self.leaderboard = Leaderboard("leaderboard.txt")
        if not self.leaderboard.if_file_exist:  # file not exist
            self.file_error_message.pop_up(self.sc)
        self.leaderboard_list = self.leaderboard.read_file()
        for i in range(len(self.leaderboard_list)):
            if i <= 4:
                record = ":".join(self.leaderboard_list[i])
                # write name
                self.background_pen.penup()
                self.background_pen.setpos(720, 700 - 50 * i)
                self.background_pen.pendown()
                self.background_pen.write(record, font=("Arial", 18, "bold"))

        self.sc.update()

    def draw_result_circles(self):
        """
        FUNCTION - draw_result_circles()
        This function is to draw the result circles.

        PARAMETERS:
        None

        RETURNS:
        None
        """
        for i in range(len(self.result_circles)):
            for k in range(len(self.result_circles[i])):
                current_circle = self.result_circles[i][k]
                current_circle.draw()
        self.sc.update()  # update screen

    def draw_all_pegs(self):
        """
        FUNCTION - draw_result_circles()
        This function is to draw all pegs.

        PARAMETERS:
        None

        RETURNS:
        None
        """
        for i in range(len(self.peg_list)):
            for k in range(len(self.peg_list[i])):
                current_peg = self.peg_list[i][k]
                current_peg.draw()
        self.sc.update()  # update screen

    def draw_selection_circles(self):
        """
        FUNCTION - draw_selection_circles()
        This function is to draw all selection circles

        PARAMETERS:
        None

        RETURNS:
        None
        """
        for circle in self.selection_circles:
            circle.if_fill = True
            circle.draw()
        self.sc.update()  # update screen

    def draw_rectangle(self, x, y, width, height):
        """
        FUNCTION - draw_rectangle()
        This function is to draw rectangles

        PARAMETERS:
        x -- int. the left bottom x coordinate
        y -- int. the left bottom y coordinate
        width -- int. the width of the rectangle
        height -- int. The height of the rectangle

        RETURNS:
        None
        """
        self.background_pen.penup()
        self.background_pen.setpos(x, y)
        self.background_pen.setheading(0)
        self.background_pen.pendown()
        self.background_pen.forward(width)
        self.background_pen.left(90)
        self.background_pen.forward(height)
        self.background_pen.left(90)
        self.background_pen.forward(width)
        self.background_pen.left(90)
        self.background_pen.forward(height)

    def create_answer(self):
        """
        FUNCTION - create_answer()
        This function is to create the color answer

        PARAMETERS:
        None

        RETURNS:
        A string list of colors.
        """
        colors = self.color_database.copy()
        answer = []
        for i in range(4):
            random_index = random.randint(0, len(colors) - 1)
            answer.append(colors[random_index])
            colors.pop(random_index)
        return answer

    def get_user_name(self):
        """
        FUNCTION - get_user_name()
        This function is to get the username.

        PARAMETERS:
        None

        RETURNS:
        A string.
        """
        name = self.sc.textinput("Name input", "Please enter your name:")
        if not name:  # click cancel
            self.sc.bye()

        while name.strip(" ") == "" or len(name) > 12:  # invalid name
            name = self.sc.textinput("Name input", "Please try again:")
        return name

    def click(self, x, y):
        """
        FUNCTION - click()
        This function is to calculate which part the user clicks.

        PARAMETERS:
        X - int. the x coordinate of user click.
        y - int. the y coordinate of user click.

        RETURNS:
        None
        """
        # cheating line
        print(self.answer)

        # check circles
        for circle in self.selection_circles:
            if circle.if_clicked(x, y) and circle.if_fill:
                self.click_selection_circle(circle)
                break

        # check xbutton
        if self.xbutton.if_clicked(x, y):
            self.click_xbutton()

        # check quit button
        if self.quit_button.if_clicked(x, y):
            self.click_quit_button()

        # check check_button
        if self.check_button.if_clicked(x, y):
            self.click_check_button()

        self.sc.update()

    def click_selection_circle(self, circle):
        """
        FUNCTION - click_selection_circle()
        This function is to calculate which part the user clicks.

        PARAMETERS:
        circle - a circle instance.

        RETURNS:
        None
        """
        for result_circle in self.result_circles[self.line_index]:
            if result_circle.color == "":  # if result circle has no color
                circle.if_fill = False
                circle.draw()
                result_circle.color = circle.color
                result_circle.if_fill = True
                result_circle.draw()
                return

    def generate_situation_list(self, selection, answer):
        """
        FUNCTION - generate_situation_list()
        This function is to generate the situation list for pegs.

        PARAMETERS:
        selection - a list of Circle instance.
        answer - a string list

        RETURNS:
        An int list. Each int refers to a situation in pegs
        """
        situation_list = []
        for i in range(len(selection)):
            color = selection[
                i].color  # loop from every color in result circle
            if color in answer:  # if color is same as answer
                if i == answer.index(color):  # if color is right position
                    situation_list.append(2)
                else:
                    situation_list.append(
                        1)  # if color is same but not right position
            else:
                situation_list.append(
                    0)  # if neither color or position is right

        situation_list.sort(
            reverse=True)  # sort situation list from bigger to smaller
        return situation_list

    def click_check_button(self):
        """
        FUNCTION - click_check_button()
        This function is to react when user click the check button.

        PARAMETERS:
        None

        RETURNS:
        None
        """
        # reset selection circles to fill them with original colors
        for circle in self.selection_circles:
            circle.if_fill = True  # fill them with colors
            circle.draw()

        # create a situation list
        situation_list = self.generate_situation_list(
            self.result_circles[self.line_index], self.answer)

        # arrange situations to pegs and draw them
        for i in range(len(self.peg_list[self.line_index])):
            peg = self.peg_list[self.line_index][
                i]  # at first the line_index is 0
            peg.set_situation(situation_list[i])
            peg.draw()  # draw with new situation color

        # check if game success
        if_success = True
        for situation in situation_list:
            if situation != 2:
                if_success = False
        if if_success:
            self.game_success()

        self.line_index += 1  # next line of result circles

        # if user run out of chances
        if self.line_index > self.max_line_index:
            self.game_fail()

    def click_xbutton(self):
        """
        FUNCTION - click_xbutton()
        This function is to react when user click the x button.

        PARAMETERS:
        None

        RETURNS:
        None
        """
        for circle in self.selection_circles:
            circle.if_fill = True
            circle.draw()
        # reset result circles
        for circle in self.result_circles[self.line_index]:
            circle.color = ""
            circle.if_fill = False
            circle.draw()

    def click_quit_button(self):
        """
        FUNCTION - click_quit_button()
        This function is to react when user click the quit button.

        PARAMETERS:
        None

        RETURNS:
        None
        """
        self.quit_message.pop_up(self.sc)
        self.sc.ontimer(self.sc.bye, 1500)

    def game_success(self):
        """
        FUNCTION - game_success()
        This function is to react when game success

        PARAMETERS:
        None

        RETURNS:
        None
        """
        self.win_message.pop_up(self.sc)
        self.sc.ontimer(self.sc.bye, 1500)
        current_record = [self.line_index + 1, self.user_name]
        self.leaderboard.add_record(current_record, self.leaderboard_list)
        self.leaderboard.write_file(self.leaderboard_list)

    def game_fail(self):
        """
        FUNCTION - game_fail()
        This function is to react when game fail

        PARAMETERS:
        None

        RETURNS:
        None
        """
        self.lose_message.pop_up(self.sc)
        self.sc.ontimer(self.sc.bye, 1500)


def main():
    game = Game()
    game.sc.mainloop()


if __name__ == '__main__':
    main()
