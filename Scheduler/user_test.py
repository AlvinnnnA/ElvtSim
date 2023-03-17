from datetime import datetime, timedelta
import random
import numpy as np
from scipy.stats import norm
from pandas import DataFrame
from Scheduler.Thread.thread import Passenger
from Scheduler.Thread.convert_time import *
import matplotlib.pyplot as plt


class User(Passenger):
    @classmethod  # 随机生成乘客的函数
    def random_passenger(cls, number: int, highest: int, start_time, end_time):
        born_passenger_list = []
        for i in range(number):
            start = random.randint(1, highest)
            end = random.randint(1, highest)
            while start == end:
                end = random.randint(1, highest)
            born_passenger_list.append(User(str(i), start,
                                            end, num_to_time(
                    random.randint(time_to_num(start_time), time_to_num(end_time)))))
        return born_passenger_list

    def __repr__(self):
        return f"User({self.uid}, {self.occurrence_time})"

    def to_list(self):
        return [self.uid, self.src_floor, self.dest_floor, self.occurrence_time, time_to_num(self.occurrence_time)]

# TODO generation works but centering is wrong
def fit_users_to_curve(users, peak_hours, start_time, end_time):
    # Convert peak hours to integers
    peak_times = [time_to_num(h) for h in peak_hours]
    # Compute duration of time window
    start = time_to_num(start_time)
    end = time_to_num(end_time)
    if end <= start:
        end += 24 * 3600
    window_duration = end - start
    # Compute total weight of users
    total_weight = len(users)
    # Assign random weights to users
    weights = np.random.rand(total_weight)
    weights /= np.sum(weights)
    # Fit each peak separately
    for peak_time in peak_times:
        # Compute time delta to peak time
        delta = peak_time - start
        if delta < 0:
            delta += 24 * 3600
        # Compute standard deviation of normal distribution
        std = window_duration / 6  # 68% of values within peak window
        # Compute probability density function of normal distribution
        pdf = norm(loc=delta, scale=std).pdf(np.arange(window_duration))
        # Normalize pdf to sum to 1
        pdf /= np.sum(pdf)
        # Assign each user to a time bin
        bins = np.random.choice(np.arange(window_duration), size=total_weight, p=pdf)
        # Convert bins to timestamps
        timestamps = [num_to_time(start + b) for b in bins]
        # Assign timestamps to users
        for user, timestamp in zip(users, timestamps):
            user.occurrence_time = timestamp
            user.occurrence_time_seconds = time_to_num(timestamp) - start


def plot_user_occurrence(users):
    timestamps = [time_to_num(user.occurrence_time) for user in users]
    bins = np.linspace(0, 24 * 3600, 240)  # 240 bins for 1/10 hour intervals
    density, _ = np.histogram(timestamps, bins=bins, density=False)
    plt.plot(bins[:-1], density)
    plt.xlabel('Time of day')
    plt.ylabel('User occurrence density')
    plt.show()


users = User.random_passenger(1000, 6, '08:00:00', '22:00:00')
fit_users_to_curve(users, ['09:00:00', '12:00:00', '18:00:00'], '08:00:00', '22:00:00')
user_list = []
for user in users:
    print(user)
    user_list.append(user.to_list())
DataFrame(user_list).to_csv('user.csv', index=False, header=False)
