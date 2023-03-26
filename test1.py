from pprint import pprint
import threading
from Scheduler.Thread.thread1 import Elevator, GlobalClock
from Scheduler.Logic import parser
import daemon
import os


def classify_elevator(final):  # 分类电梯，并将独立乘客分配到独立电梯，共同乘客分配到共同电梯
    groups = {}
    elevator_list = list(final['elevators'].keys())

    for elevator in final['results']['elevators']:
        if len(elevator['group']) == 1:
            groups.setdefault('group1', []).append(elevator)  # 为独立运行电梯分组
        else:
            groups.setdefault('group2', []).append(elevator)  # 为共同运行电梯分组
    pprint(groups)
    for group in groups['group1']:  # 为电梯分配乘客
        elevators = group['group']
        queue = group['queue']
        for elevator in elevators:
            for passenger in queue:
                elevator_lut[elevator].total_list.append(passenger)
                elevator_lut[elevator].elevator_timestamp.append(passenger.call_time)

    # for elevator in groups['group1']:
    #     print(elevator)

    for i, elevator in enumerate(elevator_list):  # 为独立运行电梯中，每个乘客分配电梯
        for group in groups['group1']:
            if elevator in group['group']:
                for passenger in group['queue']:
                    passenger.into_elevator = elevator_lut[elevator]

    allocate_common_passenger(groups)  # 分配共同乘客

    queue_list = [item for sublist in [x['queue'] for x in groups['group2']] for item in sublist]
    return queue_list


def allocate_common_passenger(groups):  # 分配共同乘客
    for group in groups['group2']:
        for passenger in group['queue']:
            passenger.maybe_into_elevator = [elevator_lut[group['group'][0]], elevator_lut[group['group'][1]]]


if __name__ == '__main__':
    abspath_config = os.path.abspath("Data/config.json")
    final = daemon.main(abspath_config, use_random=True, random_args=[100, 9, "08:00:00", "20:00:00"])
    # pprint(final)
    # print(type(final),['elevators'])
    elevator_list = list(final['elevators'].keys())
    elevator_lut = {}
    for key, value in final['elevators'].items():
        elevator_lut[key] = Elevator(value)
        if value["max_floor"] < final['base']['floor_count']:
            raise Exception("Elevator {} max floor is less than floor count".format(key))
    share_list = classify_elevator(final)

    global_clock = GlobalClock([value for key, value in elevator_lut.items()])
    global_condition = threading.Condition()

    list_put = False
    for elevator in elevator_lut.values():
        if not list_put:
            elevator.share_list = share_list
            list_put = True
        elevator.global_clock = global_clock
        elevator.global_condition = global_condition

    thread1 = threading.Thread(target=elevator_lut['elevator1'].start_elevator, name='thread1')
    thread2 = threading.Thread(target=elevator_lut['elevator2'].start_elevator, name='thread2')
    thread3 = threading.Thread(target=elevator_lut['elevator3'].start_elevator, name='thread3')
    thread4 = threading.Thread(target=elevator_lut['elevator4'].start_elevator, name='thread4')

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
