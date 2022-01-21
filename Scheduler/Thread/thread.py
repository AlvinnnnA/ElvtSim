class Elevator():
    def __init__(self):
        self.elevator_state = 'static'
        self.current_floor = 3
        self.destination_floor = 1
        self.elevator_list = []

    def run_elevator(self):
        self.search()
        if (self.destination_floor == self.current_floor):
            self.open_door()
        while self.elevator_list:
            if(self.elevator_state == 'up'):
                self.current_floor = self.current_floor+1
                if(self.destination_floor == self.current_floor):
                    self.open_door()
                    self.elevator_list.remove(self.destination_floor)
                    break
            if(self.elevator_state == 'down'):
                self.current_floor = self.current_floor-1
                if (self.destination_floor == self.current_floor):
                    self.open_door()
                    self.elevator_list.remove(self.destination_floor)
                    break

    def search(self):
        if self.elevator_state == 'static':
            min = 0
            for destination in self.elevator_list:
                if min > destination:
                    min = destination
            self.destination_floor = min
            if(self.destination_floor > self.current_floor):
                self.elevator_state = 'up'
            elif(self.destination_floor  < self.current_floor):
                self.elevator_state = 'down'



    def open_door(self):
        print("门已开")

class Passenger():
    def __init__(self,uid,src_floor,dest_floor,time):
        self.uid = uid
        self.src_floor = src_floor
        self.dest_floor = dest_floor
        self.state = 'Waiting'
        self.time = time
        self.on_called(elevator_one)

    def on_called(self,elevator_num):
        elevator_num.elevator_list.append(self.src_floor)

elevator_one=Elevator()
syn=Passenger('1',1,4,0)
elevator_one.run_elevator()
print(elevator_one.elevator_list)
print(elevator_one.current_floor)