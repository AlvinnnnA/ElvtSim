from Scheduler.Thread.thread import Elevator
import json
from itertools import combinations

'''
elevator_one_choice = [3, 5]
elevator_two_choice = [2, 4, 6]
elevator_one_arrangement = {'min_floor': 1, 'max_floor': 6, 'elevator_choice': elevator_one_choice}  # 一号电梯的配置信息
elevator_two_arrangement = {'min_floor': 1, 'max_floor': 6, 'elevator_choice': elevator_two_choice}  # 二号电梯的配置信息
elevator_parse_dict ={'elevator_one': elevator_one_arrangement, 'elevator_two': elevator_two_arrangement}
elevator_json = json.dumps(elevator_parse_dict, indent=4, ensure_ascii=False)  # 将配置信息文件转化为json （试验用）


def elevator_parser(elevator_json):  # 传入一个电梯配置文件的json
    elevator_parse_dict = json.loads(elevator_json)  # 生成字典文件
    elevator_one_choice = elevator_parse_dict['elevator_one']['elevator_choice']
    elevator_two_choice = elevator_parse_dict['elevator_two']['elevator_choice']
    elevator_choice_dictionary = {'elevator_one': elevator_one_choice, 'elevator_two': elevator_two_choice}  # 电梯选择字典
    elevator_one = Elevator(elevator_parse_dict['elevator_one']['min_floor'], elevator_parse_dict['elevator_one']['max_floor'])  #一号电梯楼层
    elevator_two = Elevator(elevator_parse_dict['elevator_two']['min_floor'], elevator_parse_dict['elevator_two']['max_floor'])
    return elevator_one, elevator_two, elevator_choice_dictionary
'''

def elevator_parser(elevator_json):  # 传入一个电梯配置文件的json
    # TODO json config parsing
    elevator_parse_dict = json.loads(elevator_json)  # 生成字典文件
    #for elevator in elevator_parse_dict[]:


def allocate_floors(floors, elevator_count):
    # TODO reduce the allocation to only sensible ones
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

def passenger_parser():
    pass


if __name__=="__main__":
    print(len(allocate_floors(range(1,7), 2)))