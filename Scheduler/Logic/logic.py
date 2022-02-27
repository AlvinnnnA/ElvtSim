from Scheduler.Thread.thread import Passenger
import my_parser


def choice_allocation(elevator_number, choice_dictionary):  # 可选择性的多梯分配，电梯数量以及解析字典
    if elevator_number == 2:
        elevator_one_list = []
        elevator_two_list = []
        for passenger in total_passenger_list:  # 遍历在总乘客列表中的每一个乘客，根据电梯的特点进行分配
            if passenger.src_floor == 1:
                for floor in choice_dictionary['elevator_one']:  # 一号梯的去往楼层
                    if passenger.dest_floor == floor:
                        elevator_one_list.append(passenger)
                        break
                for floor in choice_dictionary['elevator_two']:  # 二号梯的去往楼层
                    if passenger.dest_floor == floor:
                        elevator_two_list.append(passenger)
                        break
            else:
                for floor in choice_dictionary['elevator_one']:
                    if passenger.src_floor == floor:
                        elevator_one_list.append(passenger)
                        break
                for floor in choice_dictionary['elevator_two']:
                    if passenger.src_floor == floor:
                        elevator_two_list.append(passenger)
                        break
        for passenger in elevator_one_list:
            passenger.into_elevator = elevator_one
            passenger.into_elevator.elevator_timestamp.append(passenger.call_time)
            passenger.into_elevator.total_list.append(passenger)
        for passenger in elevator_two_list:
            passenger.into_elevator = elevator_two
            passenger.into_elevator.elevator_timestamp.append(passenger.call_time)
            passenger.into_elevator.total_list.append(passenger)


elevator_one_choice = [3, 5]
elevator_two_choice = [2, 4, 6]
elevator_one_arrangement = {'min_floor': 1, 'max_floor': 6, 'elevator_choice': elevator_one_choice}
elevator_two_arrangement = {'min_floor': 1, 'max_floor': 6, 'elevator_choice': elevator_two_choice}
elevator_parse_list = [elevator_one_arrangement, elevator_two_arrangement]
elevator_one, elevator_two, elevator_dictionary = my_parser.elevator_parser(elevator_parse_list)
total_passenger_list = []
for i in range(20):
    total_passenger_list.append(Passenger(1, 3, 6, "08:00:00"))
choice_allocation(2, elevator_dictionary)
elevator_one.start_elevator()
elevator_two.start_elevator()
