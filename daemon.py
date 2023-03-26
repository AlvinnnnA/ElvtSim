from Scheduler.Logic import parser
from Scheduler.Thread.thread1 import Passenger
from Log.Common.bifrost import Reporter, Chime

DEFAULT_CONFIG = "/Data/config.json"
DEFAULT_USER_CSV = "/Data/users.csv"


class InterLayer:
    def __init__(self, config=DEFAULT_CONFIG, user_csv=DEFAULT_USER_CSV, use_random=False, random_args: list=False):
        self.config = config
        self.simlog = Reporter()
        if not use_random:
            self.user = user_csv
        else:
            if not random_args:
                self.simlog.error("Random passenger generation requires random_args")
            else:
                self.user = Passenger.random_passenger(random_args.append(self.simlog))


if __name__ == "__main__":
    config = "/Data/config.json"
    user_csv = "/Data/users.csv"

