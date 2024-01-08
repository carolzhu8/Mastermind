import unittest

from circle import Circle
from mastermind import Game


class TestGame(unittest.TestCase):
    """
    This is a unit test for the game
    """
    def test_guest(self):
        """
        FUNCTION - test_guest()
        This function is to test the guessing process of the game. During test,
        the game will pop up and please enter a username to make test runnable.

        PARAMETERS:
        None

        RETURNS:
        None
        """
        game = Game()
        answer = ["blue", "green", "red", "purple"]
        samples = [
            [Circle(0, 0, "blue"), Circle(0, 0, "green"), Circle(0, 0, "red"),
             Circle(0, 0, "purple")],
            [Circle(0, 0, "green"), Circle(0, 0, "blue"), Circle(0, 0, "red"),
             Circle(0, 0, "purple")],
            [Circle(0, 0, "yellow"), Circle(0, 0, "black"),
             Circle(0, 0, "white"), Circle(0, 0, "purple")]]
        expected_result = [[2, 2, 2, 2], [2, 2, 1, 1], [2, 0, 0, 0]]
        for i in range(len(samples)):
            result = game.generate_situation_list(samples[i], answer)
            self.assertEqual(result, expected_result[i])
