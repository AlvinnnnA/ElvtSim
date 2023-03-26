from pprint import pprint

from Scheduler.Logic import parser
from Scheduler.Thread.thread1 import Passenger
from Log.Common.bifrost import Reporter, Chime

DEFAULT_CONFIG = "/Data/config.json"
DEFAULT_USER_CSV = "/Data/users.csv"


class InterLayer:
    def __init__(self, config=DEFAULT_CONFIG, user_csv=DEFAULT_USER_CSV, use_random=False, random_args: list=False):
        self.config = config
        self.simlog = Reporter()
        self.simlog.info("Daemon: main class initialized")
        if not use_random:
            self.user = user_csv
        else:
            if not random_args:
                self.simlog.error("Daemon: Random passenger generation requires random_args")
            else:
                random_args.append(self.simlog)
                self.user = Passenger.random_passenger(*random_args)

    def kickstart(self):
        return parser.combine_all_and_output(self.config, self.user)
        # Give elevators the finished grand dict


if __name__ == "__main__":
    config = "Data/config.json"
    user_csv = "Data/user.csv"
    daemon = InterLayer(config, use_random=True, random_args=[100, 9, "08:00:00", "20:00:00"])
    pprint(daemon.kickstart())

