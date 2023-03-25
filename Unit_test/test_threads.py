import threading
import unittest

from Scheduler.Thread import convert_time
from Scheduler.Thread.thread1 import Elevator, Passenger, GlobalClock


class TestElevatorThread(unittest.TestCase):
    def setUp(self):
        pass