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

    def main():
        # 菜单界面
        MENU = '''
        YixinLi 欢迎您
        Menu:
        L - List all albums
        A - Add new album
        M - Markan album as completed
        Q - Quit'''
        print("Album Tracker 2.0 - by <YixinLi>")
        print("4 albums loaded")
        print(MENU)

