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


def elevator_parser(elevator_num, elevator_json):  # 传入一个电梯配置文件的json
    if elevator_num <= 1 or elevator_num > 10:
        print("配置信息有误，请重新输入")
    else:
        elevator_parse_dict = json.loads(elevator_json)  # 生成字典文件
        elevator_choice_dictionary = {}  # 电梯选择楼层的字典
        elevator_dictionary = {}  # 电梯剩余基本信息的字典
        for i in range(1, elevator_num+1):
            if i == 1:n = "one"
            elif i == 2: n = "two"
            elif i == 3:n = "three"
            elif i == 4:n = "four"
            elif i == 5: n = "five"
            elif i == 6:n = "six"
            elif i == 7: n = "seven"
            elif i == 8:n = "eight"
            elif i == 9: n = "nine"
            elif i == 10:n = "ten"
            globals()['elevator_' + n + '_choice'] = elevator_parse_dict['elevator_' + n]['elevator_choice']  # 解析出所有电梯选择的楼层
            elevator_choice_dictionary.update({'elevator_' + n: eval('elevator_' + n + '_choice')})  # 电梯选择楼层的字典
            globals()['elevator_' + n] = Elevator(elevator_parse_dict['elevator_' + n]['min_floor'], elevator_parse_dict['elevator_' + n]['max_floor'])
            elevator_dictionary.update({'elevator_' + n: eval('elevator_' + n)})
        return elevator_dictionary, elevator_choice_dictionary
'''

def elevator_parser(elevator_json) -> dict:  # 传入一个电梯配置文件的json
    # TODO json config parsing
    elevator_parse_dict = json.loads(elevator_json)  # 生成字典文件
    #for elevator in elevator_parse_dict[]:

    return elevator_parse_dict

def auto_operator(conf_dict: dict):
    # TODO choose appropriate config for the given elevator configuration
    pass


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