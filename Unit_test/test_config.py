import Scheduler.Logic.parser as parser
import unittest


class TestConfig(unittest.TestCase):
    def setUp(self) -> None:
        self.conf_dict = parser.elevator_reader("default_1.json")
        self.passenger_queue = parser.passenger_getter("passenger_1.csv")

    def test_read(self):
        pass

    def test_write(self):
        pass
