from Scheduler.Thread.thread import Elevator


def elevator_parser(elevator_parse_list):
    elevator_one_choice = elevator_parse_list[0]['elevator_choice']
    elevator_two_choice = elevator_parse_list[1]['elevator_choice']
    elevator_dictionary = {'elevator_one': elevator_one_choice, 'elevator_two': elevator_two_choice}
    elevator_one = Elevator(elevator_parse_list[0]['min_floor'], elevator_parse_list[0]['max_floor'])
    elevator_two = Elevator(elevator_parse_list[1]['min_floor'], elevator_parse_list[1]['max_floor'])
    return elevator_one, elevator_two, elevator_dictionary

def passenger_parser():
    pass

