from pprint import pprint
import json
from Log.Common import bifrost
from Scheduler.Logic import parser
from Scheduler.Thread.thread1 import Passenger
from Log.Common.bifrost import Reporter
from common_objects import DefaultPrint
from datetime import datetime as dt

DEFAULT_CONFIG = "Data/config.json"
DEFAULT_USER_CSV = "Data/users.csv"


class InterLayer:
    def __init__(self, config=DEFAULT_CONFIG):
        self.config = config
        self.simlog = DefaultPrint()

    def entry_point(self, user_csv=DEFAULT_USER_CSV, use_random=False, random_args: list = False,
                    log_configs=False):
        self.simlog.info("Daemon: Initializing entry point - Users")
        if not use_random:
            self.simlog.info("Daemon: Using user csv")
            self.user = user_csv
        else:
            self.simlog.info("Daemon: Using random passenger generator")
            if not random_args:
                self.simlog.critical("Daemon: Random passenger generation requires random_args")
            else:
                random_args.append(self.simlog)
                self.user = Passenger.random_passenger(*random_args)
        self.simlog.info("Daemon: Initializing entry point - Config")
        if parser.elevator_reader(self.config)["mode"] == "scene":
            self.simlog.info("Daemon: Scene mode detected, generating elevator configs")
            return self.process_scene(parser.combine_all_and_output(self.config, self.user), self.user, log_configs)
        self.simlog.info("Daemon: Initializing entry point - Log")
        if not isinstance(log_configs, dict):
            self.simlog = Reporter()
        else:
            self.simlog = Reporter(log_configs)
        self.simlog.info("Daemon: entry point initialized. Ready to start")
        return True

    def process_scene(self, scene_list, user_queue, log_configs):
        scene_json = []
        print(f"Daemon: {len(scene_list)} scenes detected, generating configs as file")
        for scene in scene_list:
            self.config = scene
            name = f"Data/scene_{dt.strftime(dt.now(), '%m-%d-%H-%M')}_{scene_list.index(scene)}.json"
            with open(name, "w") as f:
                json.dump(scene, f, indent=4)
            scene_json.append(name)
        return scene_main(scene_json, user_queue, log_configs)
        # self.kickstart()

    def kickstart(self):
        result = parser.combine_all_and_output(self.config, self.user)
        if isinstance(result, dict):
            return result
        else:
            raise TypeError("Daemon: Unexpected return type from combine_all_and_output")
        # Give elevators the finished grand dict


def scene_main(scene_list, user_queue, log_configs):
    scene_instances = []
    for scene_cfg_path in scene_list:
        scene_instances.append(InterLayer(scene_cfg_path))
    return {"user_queue": user_queue, "log": log_configs, "scene": scene_instances}


def main(config=DEFAULT_CONFIG, user_csv=DEFAULT_USER_CSV, use_random=False, random_args: list = False,
         log_configs=False):
    daemon = InterLayer(config)
    ready_results = daemon.entry_point(user_csv, use_random=use_random, random_args=random_args,
                                       log_configs=log_configs)
    if ready_results is True:
        return daemon.kickstart()
        pass
    else:
        for scene_instance in ready_results["scene"]:
            scene_instance.entry_point(ready_results["user_queue"], log_configs=ready_results["log"])
            # return scene_instance.kickstart()
    # TODO fix this


if __name__ == "__main__":
    config = "Data/config.json"
    user_csv = "Data/user.csv"
    pprint(main(use_random=True, random_args=[100, 9, "08:00:00", "20:00:00"]))
