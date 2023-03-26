from pprint import pprint

from Scheduler.Thread.thread1 import Elevator, Passenger
from Scheduler.Logic import parser


def classify_elevator(final):  # 分类电梯，并将独立乘客分配到独立电梯，共同乘客分配到共同电梯
    groups = {}
    for elevator in final['result']['elevators']:
        if len(elevator['group']) == 1:
            groups.setdefault('group1', []).append(elevator)  # 为独立运行电梯分组
        else:
            groups.setdefault('group2', []).append(elevator)  # 为共同运行电梯分组

    for i, elevator in enumerate(['elevator1', 'elevator2', 'elevator3', 'elevator4']):  # 为独立运行电梯中，每个乘客分配电梯
        for group in groups['group1']:
            if elevator in group['group']:
                for passenger in group['queue']:
                    passenger.into_elevator = elevator

    for elevator in groups['group2']:
        print(elevator)

    queue_list = [item for sublist in [x['queue'] for x in groups['group2']] for item in sublist]
    print(queue_list)
    return queue_list


if __name__ == '__main__':
    final = parser.get_thread_config_test(20)
    pprint(final)
    classify_elevator(final)
    elevator_lut = {}
    for key,value in final['config'].items():
        test_conf = {'event_enabled': True, 'verbose': True, 'state': 'static',
                       'speed': 're-start', 'initial_floor': 4,
                       'initial_dest': 1, 'min_floor': 1, 'max_floor': 9, "max_weight": 15, 'initial_time': "00:00:00",
                       'floor_list': value, 'name': key}
        elevator_lut[key] = Elevator(test_conf)

