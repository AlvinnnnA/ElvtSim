import threading
import time

class Elevator:
    def __init__(self, name, global_clock, global_condition):
        self.name = name
        self.local_clock = 0
        self.global_clock = global_clock
        self.global_condition = global_condition

    def run(self):
        while True:
            # 更新电梯状态（例如上升/下降）
            self.update_state()

            # 增加并同步时间
            self.increment_and_sync_time()

    def update_state(self):
        print(f"{self.name} 在时刻 {self.local_clock} 更新状态")
        time.sleep(1)

    def increment_and_sync_time(self):
        with self.global_condition:
            self.local_clock += 1

            if all(elevator.local_clock == self.global_clock.value + 1 for elevator in self.global_clock.elevators):
                self.global_clock.value += 1
                self.global_condition.notify_all()
            else:
                self.global_condition.wait_for(lambda: self.local_clock == self.global_clock.value)

class GlobalClock:
    def __init__(self, elevators):
        self.value = 0
        self.elevators = elevators

elevator1 = Elevator("电梯1", None, None)
elevator2 = Elevator("电梯2", None, None)
global_clock = GlobalClock([elevator1, elevator2])
global_condition = threading.Condition()

elevator1.global_clock = global_clock
elevator1.global_condition = global_condition
elevator2.global_clock = global_clock
elevator2.global_condition = global_condition

thread1 = threading.Thread(target=elevator1.run)
thread2 = threading.Thread(target=elevator2.run)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
