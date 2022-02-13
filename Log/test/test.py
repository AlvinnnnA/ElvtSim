import os
import sys


def func():
    print(os.getcwd())
    print(sys.argv[0].split('/')[-1].split('.')[0])
    print(__file__)
