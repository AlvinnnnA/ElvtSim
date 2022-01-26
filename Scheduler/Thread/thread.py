class Elevator():
    def __init__(self):  # 创建一个电梯类，并且赋予电梯相应的属性，有当前状态，当前楼层，目标楼层，等待乘客的列表，电梯上乘客的列表
        self.elevator_state = 'static'
        self.current_floor = 3
        self.destination_floor = 1
        self.waiting_list = []
        self.elevator_list = []

    def start_elevator(self): # 电梯开始运行，其中包含多种逻辑，全部拆分出来
        self.search_called()
        self.run_elevator()

    def run_elevator(self):
        while self.waiting_list or self.elevator_list:
            self.search_called()   # 每运行一层都检查一下命令队列，检查电梯的目的地
            if (self.destination_floor == self.current_floor):  # 如果电梯停下，再检查是否应该换向
                self.open_door(self.destination_floor)
                self.check_state()
                continue
            if(self.elevator_state == 'up'):   #判断电梯运行状态
                self.current_floor = self.current_floor+1
                print('电梯已到达' + str(self.current_floor) + '层')
            if(self.elevator_state == 'down'):
                self.current_floor = self.current_floor-1
                print('电梯已到达' + str(self.current_floor) + '层')

    def search_called(self):    #电梯调用函数寻找目的地
        if self.elevator_state == 'static':  #电梯起始状态，这个我只做了下行，上行是完全一样，但是应该同时进行判断，最好在加入时钟后再写
            min = 6    #这个是电梯最大的楼层数，以后电梯的属性应该增加最高停靠楼层数，已经最低楼层数
            for passenger in self.waiting_list:
                destination = passenger.src_floor
                if min > destination:
                    min = destination
                self.destination_floor = min
                if(self.destination_floor > self.current_floor):
                    self.elevator_state = 'up'
                elif(self.destination_floor  < self.current_floor):
                    self.elevator_state = 'down'
        if self.elevator_state == 'up':       # 依旧是同时检查等待乘客列表和电梯乘客列表，判断最快到达楼层
            self.destination_floor = 6        # 最高楼层属性
            for passenger in self.waiting_list:
                if (passenger.dest_floor-passenger.src_floor > 0):     # 判断乘客按钮的方向
                    if passenger.src_floor >= self.current_floor:
                        pre_destination_floor = passenger.src_floor
                        if self.destination_floor > pre_destination_floor:
                            self.destination_floor = pre_destination_floor
            for passenger in self.elevator_list:
                if passenger.dest_floor >= self.current_floor:
                    pre_destination_floor = passenger.dest_floor
                    if self.destination_floor > pre_destination_floor:
                        self.destination_floor = pre_destination_floor
        if self.elevator_state == 'down':
            self.destination_floor = 1      # 最低楼层属性
            for passenger in self.waiting_list:
                if (passenger.dest_floor - passenger.src_floor < 0):  # 判断乘客是否是上行
                    if passenger.src_floor <= self.current_floor:
                        pre_destination_floor = passenger.src_floor
                        if self.destination_floor < pre_destination_floor:
                            self.destination_floor = pre_destination_floor
            for passenger in self.elevator_list:
                if passenger.dest_floor <= self.current_floor:
                    pre_destination_floor = passenger.dest_floor
                    if self.destination_floor < pre_destination_floor:
                        self.destination_floor = pre_destination_floor

    def check_state(self):  # 给电梯换方向的逻辑，通过同时检查乘客等待列表和电梯乘客列表来判断是否应该换向进行
        if self.waiting_list and self.elevator_list:
            self.elevator_state = 'static'
        else:
            if self.elevator_state == 'down':
                min = self.current_floor
                for passenger in self.waiting_list:
                    if min > passenger.src_floor:
                        min = passenger.src_floor
                for passenger in self.elevator_list:
                    if min > passenger.dest_floor:
                        min = passenger.dest_floor
                if min == self.current_floor:
                    self.elevator_state = 'up'
            if self.elevator_state == 'up':
                max = self.current_floor
                for passenger in self.waiting_list:
                    if max < passenger.src_floor:
                        max = passenger.src_floor
                for passenger in self.elevator_list:
                    if max < passenger.dest_floor:
                        max = passenger.dest_floor
                if max == self.current_floor:
                    self.elevator_state = 'down'

    def passenger_into(self,destination_floor):   # 判断是否有乘客进入，如果有，就在waiting列表中将其删除，在elevator列表中将其加入
        for passenger in self.waiting_list:
            if passenger.src_floor == destination_floor:
                passenger.on_selected(elevator_one)
                self.waiting_list.remove(passenger)
                print("乘客" + passenger.uid + "进入电梯")

    def passenger_leave(self,destination_floor):   # 判断是否有乘客离开，如果有，就在elevator将其删除
        for passenger in self.elevator_list:
            if passenger.dest_floor == destination_floor:
                self.elevator_list.remove(passenger)
                print("乘客" + passenger.uid + "离开电梯")

    def open_door(self,destination_floor):  # 门开的同时进行乘客的进入与离开
        print("门已开，请在10s内进入或者离开电梯")
        self.passenger_into(destination_floor)
        self.passenger_leave(destination_floor)

class Passenger():
    def __init__(self,uid,src_floor,dest_floor):
        self.uid = uid
        self.src_floor = src_floor
        self.dest_floor = dest_floor
        self.state = 'Waiting'
        self.on_called(elevator_one)

    def on_called(self,elevator_num):
        elevator_num.waiting_list.append(self)

    def on_selected(self,elevator_num):
        elevator_num.elevator_list.append(self)

elevator_one=Elevator()
syn=Passenger('1',1,4)
wgt=Passenger('2',2,5)
elevator_one.start_elevator()
print(elevator_one.waiting_list)
print(elevator_one.elevator_list)