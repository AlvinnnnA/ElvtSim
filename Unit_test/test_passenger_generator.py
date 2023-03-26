import os
from random import randint
import Scheduler.Logic.user_fit as usergen
import Scheduler.Logic.parser as parser
import Scheduler.Thread.thread1 as thread
import unittest
from pandas import DataFrame
from daemon import main
from datetime import datetime as dt


class TestUsergen(unittest.TestCase):
    def setUp(self):
        self.users = thread.Passenger.random_passenger(10000, 12, '19:59:00', '20:00:00')
        usergen.fit_users_to_curve(self.users, ['09:00:00', '12:00:00', '18:00:00'], '08:00:00', '22:00:00')
        user_list = []
        for user in self.users:
            user_list.append(user.to_list())
        self.df = DataFrame(user_list,
                            columns=['uid', 'src_floor', 'dest_floor', 'occurrence_time', 'occurrence_time_seconds'])
        #usergen.plot_user_occurrence(self.users)
        self.df.to_csv('user.csv', index=False)
        main(config='config.json',user_csv='user.csv',log_configs={
             "mode": "log",
             "path": f"{dt.strftime(dt.now(), '%m-%d-%H-%M')}.log",
             "level": "DEBUG"})
        self.passenger_list = parser.passenger_getter(os.path.join(os.path.abspath(os.path.curdir),
                                                                   '../Scheduler/Logic/user.csv'))

    def test_csv_data(self):
        for i in range(0, 5):
            with self.subTest(i=i):
                random_instance = randint(0, len(self.users) - 1)
                self.assertEqual(self.users[random_instance].dest_floor, self.df.iloc[random_instance, 2],
                                 f"Failed constructing csv file. {random_instance} chosen, \
                                 object read{self.users[random_instance].to_list()}, \
                                 csv read{self.df.iloc[random_instance, :]}")

    def test_csv_read(self):
        self.assertEqual(len(self.passenger_list), len(self.users),
                         f"Failed reading csv file. csv length read{len(self.passenger_list)}, \
                            object length read{len(self.users)}")
        self.assertEqual(self.passenger_list[0].call_time,
                         self.users[0].call_time,
                         f"Failed reading csv file. Start one chosen, \
                                            csv read{self.passenger_list[0].to_list()}, \
                                            object read{self.users[0].to_list()}")
        self.assertEqual(self.passenger_list[-1].call_time,
                         self.users[-1].call_time,
                         f"Failed reading csv file. Last chosen, \
                                            csv read{self.passenger_list[-1].to_list()}, \
                                            object read{self.users[-1].to_list()}")
        for i in range(0, 5):
            with self.subTest(i=i):
                random_instance = randint(0, len(self.users) - 1)
                self.assertEqual(self.passenger_list[random_instance].call_time,
                                 self.users[random_instance].call_time,
                                 f"Failed reading csv file. {random_instance} chosen, \
                                    csv read{self.passenger_list[random_instance].to_list()}, \
                                    object read{self.users[random_instance].to_list()}")

    def tearDown(self) -> None:
        # os.remove('user.csv')
        pass
