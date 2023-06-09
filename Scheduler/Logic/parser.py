import csv
from pprint import pprint

from Scheduler.Logic import config_manager, user_fit
from Scheduler.Thread.thread1 import Passenger
import json
from itertools import combinations
import os


def elevator_reader(elevator_json) -> dict:  # 传入一个电梯配置文件的json
    # 读取json文件
    with open(elevator_json, 'r') as f:
        elevator_parse_dict = json.load(f)
    # for elevator in elevator_parse_dict[]
    if elevator_parse_dict["mode"] == "config":
        return elevator_parse_dict
    elif elevator_parse_dict["mode"] == "scene":
        return config_manager.generate_elevator_configs_from_scene(elevator_parse_dict)
    else:
        raise ValueError("'mode' in config file must be 'config' or 'scene'")


def passenger_getter(passenger_csv) -> list:
    passenger_list = []
    with open(passenger_csv) as f:
        reader = csv.DictReader(f)
        for row in reader:
            # row is a dictionary mapping column names to values
            passenger_list.append(
                Passenger(int(row['uid']), int(row['src_floor']), int(row['dest_floor']), row['occurrence_time']))
    return passenger_list


def auto_operator(config, passenger_queue, to_json=False):
    def is_passenger_served(elevator, passenger):
        return passenger.src_floor in elevator and passenger.dest_floor in elevator

    def find_overlap_groups(config):
        overlaps = {}
        elevator_keys = sorted(config.keys())
        for n in range(2, len(elevator_keys) + 1):
            for elevator_group in combinations(elevator_keys, n):
                overlap_floors = set.intersection(*[set(config[elevator]) for elevator in elevator_group])
                if overlap_floors:
                    overlap_key = "_".join(sorted(elevator_group))
                    overlaps[overlap_key] = list(overlap_floors)
        return overlaps

    overlaps = find_overlap_groups(config)

    result = {"elevators": [], "unserved": []}

    for passenger in passenger_queue:
        if not isinstance(passenger.src_floor, int):
            raise TypeError("src_floor must be an int")
        served = False

        for overlap_key, overlap_floors in overlaps.items():
            if is_passenger_served(overlap_floors, passenger):
                served = True
                overlap_key_list = overlap_key.split("_")

                for elevator_dict in result["elevators"]:
                    if elevator_dict["group"] == overlap_key_list:
                        if to_json:
                            elevator_dict["queue"].append(passenger.to_list())
                        else:
                            elevator_dict["queue"].append(passenger)
                        break
                else:
                    if to_json:
                        result["elevators"].append({
                            "group": overlap_key_list,
                            "overlap_floors": overlap_floors,
                            "queue": [passenger.to_list()]
                        })
                    else:
                        result["elevators"].append({
                            "group": overlap_key_list,
                            "overlap_floors": overlap_floors,
                            "queue": [passenger]
                        })
                break

        if not served:
            for elevator, floors in config.items():
                if is_passenger_served(floors, passenger):
                    served = True

                    for elevator_dict in result["elevators"]:
                        if elevator_dict["group"] == [elevator]:
                            if to_json:
                                elevator_dict["queue"].append(passenger.to_list())
                            else:
                                elevator_dict["queue"].append(passenger)
                            break
                    else:
                        if to_json:
                            result["elevators"].append({
                                "group": [elevator],
                                "overlap_floors": floors,
                                "queue": [passenger.to_list()]
                            })
                        else:
                            result["elevators"].append({
                                "group": [elevator],
                                "overlap_floors": floors,
                                "queue": [passenger]
                            })
                    break

        if not served:
            if to_json:
                result["unserved"].append(passenger.to_list())
            else:
                result["unserved"].append(passenger)

    return result


def generate_floors(floors, elevator_count):
    # generate all possible floor combinations for a single elevator
    elevator_floors = []
    for i in range(1, len(floors) + 1):
        for c in combinations(floors, i):
            elevator_floors.append(frozenset(c))

    # generate all possible combinations of elevator configurations
    elevator_configs = set()
    for c in combinations(elevator_floors, elevator_count):
        # check if all floors are accessible in this configuration
        all_floors = set(floors)
        for floors in c:
            all_floors -= floors
        if not all_floors:
            # add this configuration to the result
            config = tuple(sorted(c))
            elevator_configs.add(config)

    # convert the result to a list of dictionaries
    result = []
    for config in elevator_configs:
        result.append({i + 1: sorted(floors) for i, floors in enumerate(config)})

    return result


def combine_all_and_output(config, passenger):
    # combine all the functions and output the result
    def get_passenger_info(passenger):
        if isinstance(passenger, list):
            passenger_queue = passenger
        elif isinstance(passenger, str):
            passenger_queue = passenger_getter(passenger)
        else:
            try:
                passenger_queue = passenger_getter(passenger)
            except:
                raise ValueError("Passenger must be a list or a str to csv")
        return passenger_queue

    def get_thread_config(config):
        if isinstance(config, str):
            config_dict = elevator_reader(config)
            if isinstance(config_dict,list):
                print("INFO: Scene mode. Config is a list of dicts.")
                return config_dict
                # TODO handle this
                #raise NotImplementedError("Scene mode not implemented yet")
        elif isinstance(config, dict):
            config_dict = config
        else:
            try:
                config_dict = elevator_reader(config)
                auto_operator(config_dict, passenger_queue)
            except:
                raise ValueError("Config must be a dict or a path to json")
        return config_dict

    passenger_queue = get_passenger_info(passenger)
    config_dict = get_thread_config(config)
    if isinstance(config_dict,list):
        return config_dict
    floor_dict = {}
    #print(config_dict)
    for name, info in config_dict['elevators'].items():
        floor_dict[name] = info['floor_list']
    config_dict['results'] = auto_operator(floor_dict, passenger_queue)
    return config_dict


def get_thread_config_test(passenger_count):
    config = {
        'elevator1': [1, 2, 3, 4, 5],
        'elevator2': [1, 3, 5, 7, 9],
        'elevator3': [1, 6, 7, 8, 9],
        'elevator4': [1, 2, 4, 6, 8],
    }
    passenger_queue = Passenger.random_passenger(passenger_count, 9, "08:00:00", "20:00:00")
    user_fit.fit_users_to_curve(passenger_queue, ['09:00:00', '12:00:00', '18:00:00'], '08:00:00', '22:00:00')
    # user_fit.plot_user_occurrence(passenger_queue)
    final = {"config": config}
    final["result"] = auto_operator(config, passenger_queue)
    return final


if __name__ == '__main__':
    pass
