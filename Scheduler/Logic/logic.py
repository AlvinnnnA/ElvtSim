from Scheduler.Thread.thread import Elevator, Passenger


def choice_allocation(elevator_number, choice_dictionary):  # 可选择性的多梯分配
    if elevator_number == 2:
        elevator_one_list = []
        elevator_two_list = []
        for passenger in total_passenger_list:  # 遍历在总乘客列表中的每一个乘客，根据电梯的特点进行分配
            if passenger.src_floor == 1:
                for floor in choice_dictionary['elevator_one']:
                    if passenger.dest_floor == floor:
                        elevator_one_list.append(passenger)
                        break
                for floor in choice_dictionary['elevator_two']:
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


single_even_switch = True
elevator_one = Elevator(1, 6)
elevator_two = Elevator(1, 6)
total_passenger_list = []
for i in range(20):
    total_passenger_list.append(Passenger(1, 3, 6, "08:00:00"))
elevator_one_choice = [3]
elevator_two_choice = [2, 5, 4, 6]
elevator_dictionary = {'elevator_one': elevator_one_choice, 'elevator_two': elevator_two_choice}
choice_allocation(2, elevator_dictionary)
elevator_one.start_elevator()
elevator_two.start_elevator()
