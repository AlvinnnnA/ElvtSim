from Scheduler.Thread.thread import Passenger
import parser
import json


# TODO This needs total rework to first build generate elevator objects then initiating dispatcher
# Choice_dictionary = {1:{"available_floors":[1,2,3],"elevator_object":Elevator()}}
def choice_allocation(total_passenger_list: dict, choice_dictionary: dict):  # 可选择性的多梯分配，传入电梯数量以及解析字典
    allocation_dict = {}
    if len(choice_dictionary) != len(choice_dictionary):
        pass #Dealing with unset floors
    for elevator_num in range(len(choice_dictionary)):
        allocation_dict[str(elevator_num)] = []
        for passenger in total_passenger_list:  # 遍历在总乘客列表中的每一个乘客，根据电梯的特点进行分配
            if passenger.src_floor in choice_dictionary[str(elevator_num)] and passenger.dest_floor in choice_dictionary[str(elevator_num)]:
                allocation_dict[str(elevator_num)].append(passenger)
        for passenger in allocation_dict[str(elevator_num)]:
            passenger.into_elevator = choice_dictionary[str(elevator_num)]['elevator_object']
            passenger.into_elevator.elevator_timestamp.append(passenger.call_time)
            passenger.into_elevator.total_list.append(passenger)

'''
elevator_one_choice = [3, 5]
elevator_two_choice = [2, 4, 6]
elevator_one_arrangement = {'min_floor': 1, 'max_floor': 6, 'elevator_choice': elevator_one_choice}  # 一号电梯的配置信息
elevator_two_arrangement = {'min_floor': 1, 'max_floor': 6, 'elevator_choice': elevator_two_choice}  # 二号电梯的配置信息
elevator_parse_dict = {'elevator_one': elevator_one_arrangement, 'elevator_two': elevator_two_arrangement}
elevator_json = json.dumps(elevator_parse_dict, indent=4, ensure_ascii=False)  # 将配置信息文件转化为json （试验用）

elevator_one, elevator_two, elevator_dictionary = my_parser.elevator_parser(elevator_json)
total_passenger_list = []
for i in range(20):
    total_passenger_list.append(Passenger(1, 3, 6, "08:00:00"))
    #
elevator_hall = {}
choice_allocation(elevator_dictionary, elevator_hall)
elevator_one.start_elevator()
elevator_two.start_elevator()
'''
