from ElvtSim.Scheduler.Thread import convert_time
import multiprocessing
from ElvtSim.common_objects import Event
from ElvtSim.Log.Common import bifrost
import threading

DEFAULT_CONF = {'event_enabled': True, 'verbose': True, 'state': 'static', 'speed': 're-start', 'initial_floor': 4,
                'initial_dest': 1, 'min_floor': 1, 'max_floor': 4, "max_weight": 15, 'initial_time': "06:00:00",
                'floor_list': [1, 2, 3, 4]}


def run_in_thread(thread_name):  # 限制函数只能在指定线程中运行
    def decorator(func):
        def wrapper(*args, **kwargs):
            current_thread = threading.current_thread()
            if current_thread.name == thread_name:
                return func(*args, **kwargs)

        return wrapper

    return decorator


@run_in_thread("thread1")
def share_call_elevator():  # 共享队列的电梯呼叫
    for passenger in share_list:
        if passenger.call_time == global_clock.value:  # 如果乘客的呼叫时间等于电梯的当前时间
            if passenger.src_floor < passenger.dest_floor:  # 上行
                choose_up(passenger)
            if passenger.src_floor > passenger.dest_floor:  # 下行
                choose_down(passenger)


def choose_up(passenger):  # 选择上行电梯
    gap = {}
    for elevator in passenger.maybe_into_elevator:  # 遍历乘客可能进入的电梯
        if elevator.elevator_state == "up" and elevator.current_floor < passenger.src_floor:
            gap[elevator] = abs(passenger.src_floor - elevator.current_floor)  # 计算电梯与乘客的楼层差
        if elevator.elevator_state == "up" and elevator.current_floor > passenger.src_floor:
            gap[elevator] = 2 * (elevator.MAX_FLOOR - elevator.MIN_FLOOR) - (abs(
                    elevator.current_floor - passenger.src_floor))  # 计算电梯与乘客的楼层差
        if elevator.elevator_state == "static":
            gap[elevator] = abs(passenger.src_floor - elevator.current_floor)  # 计算电梯与乘客的楼层差
        if elevator.elevator_state == "down":
            gap[elevator] = elevator.current_floor + passenger.src_floor - 2 * elevator.MIN_FLOOR  # 计算电梯与乘客的楼层差
    min_elevator = min(gap, key=gap.get)  # 找出最小的楼层差
    passenger.into_elevator = min_elevator
    min_elevator.waiting_list.append(passenger)


def choose_down(passenger):  # 选择下行电梯
    gap = {}
    for elevator in passenger.maybe_into_elevator:  # 遍历乘客可能进入的电梯
        if elevator.elevator_state == "down" and elevator.current_floor > passenger.src_floor:
            gap[elevator] = abs(passenger.src_floor - elevator.current_floor)  # 计算电梯与乘客的楼层差
        if elevator.elevator_state == "down" and elevator.current_floor < passenger.src_floor:
            gap[elevator] = 2 * (elevator.MAX_FLOOR - elevator.MIN_FLOOR) - (abs(
                    elevator.current_floor - passenger.src_floor))  # 计算电梯与乘客的楼层差
        if elevator.elevator_state == "static":
            gap[elevator] = abs(passenger.src_floor - elevator.current_floor)  # 计算电梯与乘客的楼层差
        if elevator.elevator_state == "up":
            gap[elevator] = 2*elevator.MAX_FLOOR-elevator.current_floor-passenger.src_floor  # 计算电梯与乘客的楼层差
    min_elevator = min(gap, key=gap.get)  # 找出最小的楼层差
    passenger.into_elevator = min_elevator
    min_elevator.waiting_list.append(passenger)


class Elevator:
    def __init__(self, conf_dict=None, event_queue=None):  # 创建一个电梯类，并且赋予电梯相应的属性

        if conf_dict is None:
            conf_dict = DEFAULT_CONF
        self.__event_enabled = conf_dict['event_enabled']  # 是否启用事件处理器报送
        self.__verbose = conf_dict['verbose']  # 是否启用啰嗦模式
        if not type(event_queue) == "multiprocessing.queues.Queue":  # 防止乱传参
            print("没有配置事件队列或配置错误，启用啰嗦模式输出")
            self.__event_enabled = False
            self.__verbose = True
        else:
            self.event_queue = event_queue
            register_event = Event("Instruction", "Register",
                                   multiprocessing.current_process().pid,
                                   "Elevator")
            self.event_queue.put(register_event)
        self.chime = bifrost.Chime
        self.elevator_state = conf_dict['state']  # 电梯的当前状态，默认是静止状态
        self.elevator_speed = conf_dict['speed']  # 电梯的速度状态
        self.current_floor = conf_dict['initial_floor']  # 电梯当前所在楼层
        self.destination_floor = conf_dict['initial_dest']  # 电梯的目标楼层
        self.MIN_FLOOR = conf_dict['min_floor']  # 电梯的最低停靠楼层
        self.MAX_FLOOR = conf_dict['max_floor']  # 电梯的最高停靠楼层
        self.available_floors = conf_dict['floor_list']  # 电梯的可用楼层
        self.MAX_WEIGHT = conf_dict['max_weight']  # 电梯的最高搭乘人数为15人
        self.elevator_clock = convert_time.time_to_num(conf_dict['initial_time'])  # 电梯的时间，也可以说是外界时间，保存的形式是时间戳（数字形式）
        self.global_clock = None  # 全局时间，保存的形式是时间戳（数字形式）
        self.global_condition = None
        self.elevator_timestamp = []  # 乘客呼叫的时间戳，将乘客分配好之后，将乘客呼叫电梯的时间戳放入这里
        self.acceleration_switch = True  # 电梯进行时间加速的按钮，默认是打开状态
        self.waiting_list = []  # 此时正在等待的乘客的队列
        self.elevator_list = []  # 电梯里乘客的队列
        self.total_list = []  # 分配完之后所有乘客的一个总队列

    def start_elevator(self):  # 电梯开始运行，其中包含多种逻辑，全部拆分出来
        while self.total_list:  # 当整个乘客列表全都没了以后，再停止运行
            self.made_in_heaven()  # 电梯开始之后先判断是否应该进行时间加速，再跑
            self.run_elevator()
        while self.elevator_clock != convert_time.time_to_num("24:00:00"):
            self.increment_and_sync_time()
            self.run_elevator()

    def run_elevator(self):
        while self.waiting_list or self.elevator_list:
            self.search_called()  # 每运行一层都检查一下命令队列，检查电梯的目的地
            if self.destination_floor == self.current_floor:  # 如果电梯停下，检查是否应该换向
                self.open_door(self.destination_floor)
                self.check_state()
                self.elevator_speed = 're-start'
                continue
            if self.elevator_state == 'up':  # 判断电梯运行状态
                self.current_floor = self.current_floor + 1
                self.chime.info('电梯已到达' + str(self.current_floor) + '层')
                if self.elevator_speed == 're-start':
                    if self.destination_floor == self.current_floor:  # 如果起始层和最终层只差一层,调成15s
                        for second in range(15):  # 在运行的过程中，电梯的时钟进行逐秒的增加，同时去判断在这个时间点有没有乘客呼叫电梯，运行速度是一层15秒
                            self.increment_and_sync_time()
                            self.call_elevator()
                    else:
                        for second in range(10):  # 在运行的过程中，电梯的时钟进行逐秒的增加，同时去判断在这个时间点有没有乘客呼叫电梯，运行速度是一层10秒
                            self.increment_and_sync_time()
                            self.call_elevator()
                        self.elevator_speed = 'running'
                if self.elevator_speed == 'running':  # 判断电梯速度状态
                    for second in range(5):  # 在运行的过程中，电梯的时钟进行逐秒的增加，同时去判断在这个时间点有没有乘客呼叫电梯，运行速度是一层五秒
                        self.increment_and_sync_time()
                        self.call_elevator()
                    if self.destination_floor == self.current_floor + 1:
                        self.elevator_speed = 're-stop'
                if self.elevator_speed == 're-stop':
                    for second in range(10):  # 在运行的过程中，电梯的时钟进行逐秒的增加，同时去判断在这个时间点有没有乘客呼叫电梯，运行速度是一层10秒
                        self.increment_and_sync_time()
                        self.call_elevator()
            if self.elevator_state == 'down':
                self.current_floor = self.current_floor - 1
                self.chime.info('电梯已到达' + str(self.current_floor) + '层')
                if self.elevator_speed == 're-start':
                    if self.destination_floor == self.current_floor:  # 如果起始层和最终层只差一层,调成15s
                        for second in range(15):  # 在运行的过程中，电梯的时钟进行逐秒的增加，同时去判断在这个时间点有没有乘客呼叫电梯，运行速度是一层五秒
                            self.increment_and_sync_time()
                            self.call_elevator()
                    else:
                        for second in range(10):  # 在运行的过程中，电梯的时钟进行逐秒的增加，同时去判断在这个时间点有没有乘客呼叫电梯，运行速度是一层10秒
                            self.increment_and_sync_time()
                            self.call_elevator()
                        self.elevator_speed = 'running'
                if self.elevator_speed == 'running':  # 判断电梯速度状态
                    for second in range(5):  # 在运行的过程中，电梯的时钟进行逐秒的增加，同时去判断在这个时间点有没有乘客呼叫电梯，运行速度是一层五秒
                        self.increment_and_sync_time()
                        self.call_elevator()
                    if self.destination_floor == self.current_floor - 1:
                        self.elevator_speed = 're-stop'
                if self.elevator_speed == 're-stop':
                    for second in range(10):  # 在运行的过程中，电梯的时钟进行逐秒的增加，同时去判断在这个时间点有没有乘客呼叫电梯，运行速度是一层10秒
                        self.increment_and_sync_time()
                        self.call_elevator()

    def search_called(self):  # 电梯调用函数寻找目的地
        if self.elevator_state == 'static':  # 电梯起始状态
            min_floor = self.MAX_FLOOR  # 这里是如果电梯在同一时间接到乘客的呼叫，优先下行
            for passenger in self.elevator_list:  # 先遍历电梯队列，即使电梯是静止的，电梯队列也可能有人
                destination = passenger.dest_floor
                if min_floor > destination:
                    min_floor = destination
                self.destination_floor = min_floor
                if self.destination_floor > self.current_floor:
                    self.elevator_state = 'up'
                elif self.destination_floor < self.current_floor:
                    self.elevator_state = 'down'
            if not self.elevator_list:
                for passenger in self.waiting_list:  # 如果电梯队列是空的，则遍历等待队列
                    destination = passenger.src_floor
                    if min_floor > destination:
                        min_floor = destination
                    self.destination_floor = min_floor
                    if self.destination_floor > self.current_floor:
                        self.elevator_state = 'up'
                    elif self.destination_floor < self.current_floor:
                        self.elevator_state = 'down'
            self.elevator_speed = 're-start'  # 找到目的地之后，修改速度状态
        if self.elevator_state == 'up':  # 同时检查等待乘客列表和电梯乘客列表，判断最快到达楼层
            self.destination_floor = self.check_max()  # 检查目前能到的最高层，主要是当做一个比较的对象
            for passenger in self.waiting_list:
                if passenger.dest_floor - passenger.src_floor > 0:  # 判断乘客按钮的方向
                    if passenger.src_floor > self.current_floor:  # 今日增加了一个重量判断，将这里的等于号删去了，逻辑上应该没什么问题
                        pre_destination_floor = passenger.src_floor
                        if self.destination_floor > pre_destination_floor:
                            self.destination_floor = pre_destination_floor
            for passenger in self.elevator_list:
                if passenger.dest_floor > self.current_floor:
                    pre_destination_floor = passenger.dest_floor
                    if self.destination_floor > pre_destination_floor:
                        self.destination_floor = pre_destination_floor
        if self.elevator_state == 'down':  # 同上
            self.destination_floor = self.check_min()
            for passenger in self.waiting_list:
                if passenger.dest_floor - passenger.src_floor < 0:  # 判断乘客是否是下行,顺带接走
                    if passenger.src_floor < self.current_floor:
                        pre_destination_floor = passenger.src_floor
                        if self.destination_floor < pre_destination_floor:
                            self.destination_floor = pre_destination_floor
            for passenger in self.elevator_list:
                if passenger.dest_floor < self.current_floor:
                    pre_destination_floor = passenger.dest_floor
                    if self.destination_floor < pre_destination_floor:
                        self.destination_floor = pre_destination_floor

    def check_state(self):  # 给电梯换方向的逻辑，通过同时检查乘客等待列表和电梯乘客列表来判断是否应该换向进行
        if self.waiting_list == [] and self.elevator_list == []:
            self.elevator_state = 'static'
            self.acceleration_switch = True  # 如果电梯保持静止，将加速按钮打开
        else:
            if self.elevator_state == 'up':  # 同时遍历等待列表和乘客列表，如果电梯的目的层与当前楼层一致，则换方向
                max_floor = self.current_floor
                for passenger in self.waiting_list:
                    if max_floor < passenger.src_floor:
                        max_floor = passenger.src_floor
                for passenger in self.elevator_list:
                    if max_floor < passenger.dest_floor:
                        max_floor = passenger.dest_floor
                if max_floor == self.current_floor:
                    self.elevator_state = 'down'
            if self.elevator_state == 'down':  # 同上
                min_floor = self.current_floor
                for passenger in self.waiting_list:
                    if min_floor > passenger.src_floor:
                        min_floor = passenger.src_floor
                for passenger in self.elevator_list:
                    if min_floor > passenger.dest_floor:
                        min_floor = passenger.dest_floor
                if min_floor == self.current_floor:
                    self.elevator_state = 'up'

    def increment_and_sync_time(self):  # 时间同步函数，每次加一秒
        with self.global_condition:
            self.elevator_clock += 1
            if all(elevator.elevator_clock == self.global_clock.value + 1 for elevator in self.global_clock.elevators):
                self.global_clock.value += 1
                self.global_condition.notify_all()
            else:
                self.global_condition.wait_for(lambda: self.elevator_clock == self.global_clock.value)
            share_call_elevator()

    def made_in_heaven(self):  # 神父要上天堂了，当电梯保持静止状态并且电梯预时间戳还有东西没有处理，就进行时间加速，每次加速一秒
        while self.elevator_timestamp and self.acceleration_switch is True:
            if self.elevator_state == 'static':
                self.increment_and_sync_time()
                for timestamp in self.elevator_timestamp:
                    if self.elevator_clock == timestamp:
                        self.acceleration_switch = False
                        self.call_elevator()
                        break

    def call_elevator(self):  # 呼叫电梯函数，如果到了正确的时间，就将乘客放入等待队列
        if not self.acceleration_switch:
            for passenger in self.total_list:
                if passenger.call_time == self.elevator_clock:
                    passenger.on_called(passenger.into_elevator)

    def check_min(self):  # 遍历电梯队列与等待队列，计算最低到达楼层
        max_floor = self.MAX_FLOOR
        for passenger in self.waiting_list:
            pre_destination_floor = passenger.src_floor
            if max_floor > pre_destination_floor:
                max_floor = pre_destination_floor
        for passenger in self.elevator_list:
            pre_destination_floor = passenger.dest_floor
            if max_floor > pre_destination_floor:
                max_floor = pre_destination_floor
        return max_floor

    def check_max(self):  # 遍历电梯队列与等待队列，计算最高到达楼层
        min_floor = self.MIN_FLOOR
        for passenger in self.waiting_list:
            pre_destination_floor = passenger.src_floor
            if min_floor < pre_destination_floor:
                min_floor = pre_destination_floor
        for passenger in self.elevator_list:
            pre_destination_floor = passenger.dest_floor
            if min_floor < pre_destination_floor:
                min_floor = pre_destination_floor
        return min_floor

    def passenger_into(self, destination_floor):  # 判断是否有乘客进入，如果有，就在waiting列表中将其删除，在elevator列表中将其加入
        for passenger in self.waiting_list[:]:  # 遍历在复制列表中，删除在原先列表中，因为每删一个对象，列表会向前移动一下
            if len(self.elevator_list) < self.MAX_WEIGHT:
                if passenger.src_floor == destination_floor:
                    passenger.on_selected(passenger.into_elevator)
                    self.waiting_list.remove(passenger)
                    if passenger.dest_floor not in self.available_floors:
                        self.chime.warning("Incorrect Floor parameter entered for passenger", passenger.uid, "Entered",
                                           passenger.dest_floor, "Minimum floor for elevator is", self.MIN_FLOOR)
                    else:
                        if passenger.call_time in self.elevator_timestamp:
                            self.elevator_timestamp.remove(passenger.call_time)  # 当乘客进入的时候将其呼叫时间从时间戳中去除
                            self.chime.info("乘客" + str(passenger.uid) + "于" +
                                            str(convert_time.num_to_time(self.elevator_clock)) + "进入电梯")
            elif len(self.elevator_list) == self.MAX_WEIGHT:
                self.chime.info('电梯人员已到达上限')
                break

    def passenger_leave(self, destination_floor):  # 判断是否有乘客离开，如果有，就在elevator将其删除
        for passenger in self.elevator_list[:]:
            if passenger.dest_floor == destination_floor:
                self.elevator_list.remove(passenger)
                if passenger in self.total_list:
                    self.total_list.remove(passenger)  # 当乘客离开之后将乘客从总列表中移除
                self.chime.info("乘客" + str(passenger.uid) + "于" + str(convert_time.num_to_time
                                                                      (self.elevator_clock)) + "离开电梯")

    def open_door(self, destination_floor):  # 门开的同时进行乘客的进入与离开
        self.chime.info("门已开，在10s内乘客离开")
        self.passenger_leave(destination_floor)
        self.passenger_into(destination_floor)
        for second in range(10):  # 同电梯运行时的时间判断
            self.increment_and_sync_time()
            self.call_elevator()


class Passenger:
    def __init__(self, uid, src_floor, dest_floor, call_time):
        self.uid = uid  # 乘客的uid号
        self.src_floor = src_floor  # 乘客的起始楼层
        self.dest_floor = dest_floor  # 乘客的目标楼层
        self.state = 'Waiting'  # 乘客的等待状态
        self.call_time = convert_time.time_to_num(call_time)  # 乘客储存是时间戳
        self.into_elevator = None  # 乘客要进入的电梯
        self.maybe_into_elevator = None  # 乘客可能进入的电梯
        self.peak_hours = None  # 乘客的高峰时间
        self.occurrence_time = None  # 乘客的发生时间

    def on_called(self, elevator_num):  # 将乘客加入等待队列
        elevator_num.waiting_list.append(self)

    def on_selected(self, elevator_num):
        elevator_num.elevator_list.append(self)

    # @class_method  # 随机生成乘客的函数
    # def random_passenger(cls, number: int, highest: int, start_time, end_time):
    #     born_passenger_list = []
    #     for i in range(number):
    #         start = random.randint(1, highest)
    #         end = random.randint(1, highest)
    #         while start == end:
    #             end = random.randint(1, highest)
    #         born_passenger_list.append(Passenger(str(i), start,
    #                                              end, convert_time.num_to_time(
    #                 random.randint(convert_time.time_to_num(start_time), convert_time.time_to_num(end_time)))))
    #     return born_passenger_list


class GlobalClock:
    def __init__(self, elevators):
        self.value = convert_time.time_to_num("00:00:00")
        self.elevators = elevators


if __name__ == '__main__':
    test_conf_1 = {'event_enabled': True, 'verbose': True, 'state': 'static',
                   'speed': 're-start', 'initial_floor': 4,
                   'initial_dest': 1, 'min_floor': 1, 'max_floor': 6, "max_weight": 15, 'initial_time': "00:00:00",
                   'floor_list': [1, 2, 3, 4]}
    test_conf_2 = {'event_enabled': True, 'verbose': True, 'state': 'static',
                   'speed': 're-start', 'initial_floor': 4,
                   'initial_dest': 1, 'min_floor': 1, 'max_floor': 6, "max_weight": 15, 'initial_time': "00:00:00",
                   'floor_list': [1, 2, 3, 4]}
    elevator_one = Elevator(test_conf_1)
    elevator_two = Elevator(test_conf_2)

    Passenger1 = Passenger(1, 1, 2, "08:00:00")
    Passenger1.into_elevator = elevator_one
    elevator_one.total_list = [Passenger1]  # 分配完之后所有乘客的一个总队列
    elevator_one.elevator_timestamp = [convert_time.time_to_num("08:00:00")]

    Passenger2 = Passenger(2, 2, 3, "09:00:00")
    Passenger2.into_elevator = elevator_two
    elevator_two.total_list = [Passenger2]  # 分配完之后所有乘客的一个总队列
    elevator_two.elevator_timestamp = [convert_time.time_to_num("09:00:00")]

    Passenger3 = Passenger(3, 1, 4, "10:00:00")
    Passenger3.maybe_into_elevator = [elevator_one, elevator_two]
    share_list = [Passenger3]  # 共享电梯的乘客队列

    global_clock = GlobalClock([elevator_one, elevator_two])
    global_condition = threading.Condition()

    elevator_one.global_clock = global_clock
    elevator_one.global_condition = global_condition
    elevator_two.global_clock = global_clock
    elevator_two.global_condition = global_condition

    thread1 = threading.Thread(target=elevator_one.start_elevator, name='thread1')
    thread2 = threading.Thread(target=elevator_two.start_elevator, name='thread2')

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
