import time


def time_to_num(elevator_time):
    # 转换成时间数组
    time_array = time.strptime("2022-01-01 " + elevator_time, "%Y-%m-%d %H:%M:%S")
    # 转换成时间戳
    timestamp = time.mktime(time_array)
    return timestamp


def num_to_time(timestamp):
    # 转换成localtime
    time_local = time.localtime(timestamp)
    # 转换成新的时间格式
    dt = time.strftime("%H:%M:%S", time_local)
    return dt

