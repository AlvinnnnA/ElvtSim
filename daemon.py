import json
import threading
from datetime import datetime as dt
from pprint import pprint

from Log.bifrost import Reporter
from Scheduler.Logic import parser
from Scheduler.Thread.thread1 import Passenger, Elevator, GlobalClock
from common_objects import DefaultPrint

DEFAULT_CONFIG = "Data/config.json"
DEFAULT_USER_CSV = "Data/users.csv"


class InterLayer:
    def __init__(self, config=DEFAULT_CONFIG):
        self.config = config
        self.simlog = DefaultPrint()
        if isinstance(config, str):
            self.simlog.info(f"Daemon: Config file detected {config}")

    def entry_point(self, user_csv=DEFAULT_USER_CSV, use_random=False, random_args: list = False,
                    log_configs: dict = False):
        self.simlog.info("Daemon: Initializing entry point - Users")
        if not use_random:
            self.simlog.info("Daemon: Using predefined user")
            self.user = user_csv
        else:
            self.simlog.info("Daemon: Using random passenger generator")
            if not random_args:
                self.simlog.critical("Daemon: Random passenger generation requires random_args")
            else:
                random_args.append(self.simlog)
                self.user = Passenger.random_passenger(*random_args)
        self.simlog.info("Daemon: Initializing entry point - Config")
        if isinstance(parser.combine_all_and_output(self.config, self.user), list):
            self.simlog.info("Daemon: Scene mode detected, generating elevator configs")
            return self.process_scene(parser.combine_all_and_output(self.config, self.user), self.user, log_configs)
        self.simlog.info("Daemon: Initializing entry point - Log")
        if isinstance(self.simlog,Reporter):
            pass
        else:
            if not isinstance(log_configs, dict):
                self.simlog = Reporter()
            else:
                print("Daemon: Log configs detected, initializing reporter")
                self.simlog = Reporter(log_configs)
        self.simlog.info("Daemon: entry point initialized. Ready to start")
        return True

    def process_scene(self, scene_list, user_queue, log_configs):
        scene_instances = []
        print(f"Daemon: {len(scene_list)} scenes detected, generating configs as file")
        #pprint(scene_list)
        for scene in scene_list:
            self.config = scene
            name = f"Data/scene_{dt.strftime(dt.now(), '%m-%d-%H-%M')}_{scene['base']['config_strategy']}.json"
            with open(name, "w") as f:
                json.dump(scene, f, indent=4)
            scene_instances.append(InterLayer(config=name))
            log_configs[
                "path"] = f"Data/scene_{dt.strftime(dt.now(), '%m-%d-%H-%M')}_{scene['base']['config_strategy']}.log"
            scene_instances[-1].simlog = Reporter(log_configs,name=scene['base']['config_strategy'])
            scene_instances[-1].entry_point(user_queue, log_configs=log_configs)
            #scene_instances.append(scene_interlayer_object)
        return scene_instances
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


def classify_elevator(final, elevator_lut=None):  # 分类电梯，并将独立乘客分配到独立电梯，共同乘客分配到共同电梯
    groups = {}
    elevator_list = list(final['elevators'].keys())

    for elevator in final['results']['elevators']:
        if len(elevator['group']) == 1:
            groups.setdefault('group1', []).append(elevator)  # 为独立运行电梯分组
        else:
            groups.setdefault('group2', []).append(elevator)  # 为共同运行电梯分组
    # pprint(groups)
    noindividual = False
    nocommon = False
    try:
        for group in groups['group1']:  # 为电梯分配乘客
            elevators = group['group']
            queue = group['queue']
            for elevator in elevators:
                for passenger in queue:
                    elevator_lut[elevator].total_list.append(passenger)
                    elevator_lut[elevator].elevator_timestamp.append(passenger.call_time)

        # for elevator in groups['group1']:
        #     print(elevator)

        for i, elevator in enumerate(elevator_list):  # 为独立运行电梯中，每个乘客分配电梯
            for group in groups['group1']:
                if elevator in group['group']:
                    for passenger in group['queue']:
                        passenger.into_elevator = elevator_lut[elevator]
    except KeyError:
        noindividual = True
        pass
    queue_list = False
    try:
        allocate_common_passenger(groups, elevator_lut)  # 分配共同乘客
        queue_list = [item for sublist in [x['queue'] for x in groups['group2']] for item in sublist]
    except KeyError:
        nocommon = True
        pass

    if noindividual and nocommon:
        raise RuntimeError("Daemon: No passenger detected")

    # queue_list = False
    pprint(queue_list)
    return queue_list


def allocate_common_passenger(groups, elevator_lut=None):  # 分配共同乘客
    for group in groups['group2']:
        for passenger in group['queue']:
            passenger.maybe_into_elevator = [elevator_lut[group['group'][0]], elevator_lut[group['group'][1]]]


def main(config=DEFAULT_CONFIG, user_csv=DEFAULT_USER_CSV, use_random=False, random_args: list = False,
         log_configs: dict = False):
    daemon = InterLayer(config)
    ready_results = daemon.entry_point(user_csv, use_random=use_random, random_args=random_args,
                                       log_configs=log_configs)
    if ready_results is True:
        final = daemon.kickstart()
        # elevator_list = list(final['elevators'].keys())
        elevator_lut = {}
        for key, value in final['elevators'].items():
            elevator_lut[key] = Elevator(value, logger=daemon.simlog)
            if value["max_floor"] < final['base']['floor_count']:
                raise Exception("Elevator {} max floor is less than floor count".format(key))
        share_list = classify_elevator(final, elevator_lut)

        global_clock = GlobalClock([value for key, value in elevator_lut.items()])
        global_condition = threading.Condition()

        list_put = False
        for elevator in elevator_lut.values():
            if not list_put:
                elevator.share_list = share_list
                list_put = True
            elevator.global_clock = global_clock
            elevator.global_condition = global_condition

        thread_group = []
        for key, elevator in elevator_lut.items():
            thread_group.append(threading.Thread(target=elevator.start_elevator, name=key))
        for thread in thread_group:
            thread.start()
        for thread in thread_group:
            thread.join()  # Wait for thread to finish
        daemon.simlog.info("Daemon: All threads finished")
        daemon.simlog.user_to_file()
    else:
        for scene_instance in ready_results:
            final = scene_instance.kickstart()
            print(f"Daemon: Scene {final['base']['config_strategy']} running")
            #pprint(final)
            elevator_lut = {}
            for key, value in final['elevators'].items():
                elevator_lut[key] = Elevator(value, logger=scene_instance.simlog)
                if value["max_floor"] < final['base']['floor_count']:
                    raise Exception("Elevator {} max floor is less than floor count".format(key))
            share_list = classify_elevator(final, elevator_lut)

            global_clock = GlobalClock([value for key, value in elevator_lut.items()])
            global_condition = threading.Condition()

            list_put = False
            for elevator in elevator_lut.values():
                if not list_put:
                    elevator.share_list = share_list
                    list_put = True
                elevator.global_clock = global_clock
                elevator.global_condition = global_condition

            thread_group = []
            for key, elevator in elevator_lut.items():
                thread_group.append(threading.Thread(target=elevator.start_elevator, name=key))
            for thread in thread_group:
                thread.start()
            for thread in thread_group:
                thread.join()  # Wait for thread to finish
            scene_instance.simlog.info("Daemon: All threads finished")
            scene_instance.simlog.user_to_file(info=final['base']['config_strategy'])


if __name__ == "__main__":
    config = "Data/config.json"
    user_csv = "Data/user.csv"
    # daemon = InterLayer(config='Data/scene_03-27-18-35_even_odd.json')
    # ready_results = daemon.entry_point(user_csv, log_configs={
    #     "mode": "log",
    #     "path": f"Data/{dt.strftime(dt.now(), '%m-%d-%H-%M')}.log",
    #     "level": "INFO"}, use_random=True, random_args=[20, 12, '07:59:00', '20:00:00'])
    # final= daemon.kickstart()
    # elevator_lut = {}
    # for key, value in final['elevators'].items():
    #     elevator_lut[key] = Elevator(value, logger=DefaultPrint())
    #     if value["max_floor"] < final['base']['floor_count']:
    #         raise Exception("Elevator {} max floor is less than floor count".format(key))
    # share_list = classify_elevator(final, elevator_lut)

    # main(config="Data/scene.json", user_csv=user_csv,
    #      log_configs={
    #          "mode": "log",
    #          "path": f"Data/{dt.strftime(dt.now(), '%m-%d-%H-%M')}.log",
    #          "level": "INFO"}, use_random=True, random_args=[10000, 12, '07:59:00', '20:00:00'])
