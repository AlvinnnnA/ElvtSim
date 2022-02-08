from Scheduler.Thread.thread import Elevator, Passenger


def single_even():  # 单双层生成用户的逻辑，逻辑是先判断用户所在是不是一层，如果是去哪层就上哪种电梯，如果不是，就根据起始地上电梯
    if single_even_switch is True:
        passenger_single_list = []
        passenger_even_list = []
        for passenger in total_passenger_list:
            if passenger.src_floor == 1:
                if passenger.dest_floor == 3 or passenger.dest_floor == 5:
                    passenger_single_list.append(passenger)
                else:
                    passenger_even_list.append(passenger)
            else:
                if passenger.src_floor == 3 or passenger.src_floor == 5:
                    passenger_single_list.append(passenger)
                else:
                    passenger_even_list.append(passenger)
        for passenger in passenger_single_list:
            passenger.into_elevator = elevator_single
            passenger.into_elevator.elevator_timestamp.append(passenger.call_time)
            passenger.into_elevator.total_list.append(passenger)
        for passenger in passenger_even_list:
            passenger.into_elevator = elevator_even
            passenger.into_elevator.elevator_timestamp.append(passenger.call_time)
            passenger.into_elevator.total_list.append(passenger)
        return passenger_single_list, passenger_even_list


single_even_switch = True
elevator_single = Elevator()
elevator_even = Elevator()
total_passenger_list = []
total_passenger_list.append(Passenger(1, 3, 6, "08:00:00"))
total_passenger_list.append(Passenger(2, 6, 2, "09:00:00"))
single_list, even_list = single_even()
elevator_single.start_elevator()
elevator_even.start_elevator()