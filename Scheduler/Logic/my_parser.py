from Scheduler.Thread.thread import Elevator
import json

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


def passenger_parser():
    pass

