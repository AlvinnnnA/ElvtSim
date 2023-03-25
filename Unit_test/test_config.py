import Scheduler.Logic.parser as parser
import unittest


class TestConfig(unittest.TestCase):
    def setUp(self) -> None:
        self.conf_dict = parser.elevator_reader("default_1.json")
        self.passenger_queue = parser.passenger_getter("passenger_1.csv")

    def test_add(self):
        self.assertEqual(1 + 1, 2)

    def test_read(self):
        self.assertDictEqual(self.conf_dict,
                             {'event_enabled': True, 'verbose': True, 'state': 'static', 'speed': 're-start',
                              'initial_floor': 4,
                              'initial_dest': 1, 'min_floor': 1, 'max_floor': 4, "max_weight": 15,
                              'initial_time': "06:00:00",
                              'floor_list': [1, 2, 3, 4]}, "Success Reading Config File")

    def test_write(self):
        pass
