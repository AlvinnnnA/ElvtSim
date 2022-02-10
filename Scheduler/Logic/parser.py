from Scheduler.Thread.thread import Elevator, Passenger


def elevator_parser():
    pass


elevator_one_arrangement = {'mix_floor': 1, 'max_floor': 6, 'elevator_choice': elevator_one_choice}
elevator_two_arrangement = {'mix_floor': 1, 'max_floor': 6, 'elevator_choice': elevator_two_choice}
elevator_parse_list = [elevator_one_arrangement, elevator_one_arrangement]
elevator_one = Elevator(elevator_parse_list[0][mix_floor], elevator_parse_list[0][max_floor])
elevator_two = Elevator(elevator_parse_list[1][mix_floor], elevator_parse_list[1][max_floor])
