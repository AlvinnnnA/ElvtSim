import time

'''
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
'''

def num_to_time(num):
    """
    Convert a number of seconds since midnight to a string representation of time in the format 'HH:MM:SS'.
    """
    hours = num // 3600
    minutes = (num % 3600) // 60
    seconds = num % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

def time_to_num(time_str):
    """
    Convert a string representation of time in the format 'HH:MM:SS' to a number of seconds since midnight.
    """
    hours, minutes, seconds = map(int, time_str.split(':'))
    return hours * 3600 + minutes * 60 + seconds
