"""
Myname:YixinLi
Date started:10|16
"""
from operator import itemgetter

import csv

choList=[]

def exist(a):
    if '4' in a and '1' in a and '5' in a:
        return 5
    elif '4' in a and '1' in a :
        return 3
    elif '1' in a:
        return 1
    elif '4' in a:
        return 4
