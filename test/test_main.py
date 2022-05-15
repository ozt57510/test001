import unittest
import main


class TestMain(unittest.TestCase):

    def test_say(self):
        self.assertEqual(main.say(), "Hello world")
