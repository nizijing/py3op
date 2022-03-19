#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'zijing'
###################################################
# Created : 2021-07-07 14:29:00
# Author  : zijing (zijing412@163.com)
# Version : 1.0.0
###################################################

import sys
arr1=[
    [0, 0, 5, 3, 0, 0, 0, 0, 0],
    [8, 0, 0, 0, 0, 0, 0, 2, 0],
    [0, 7, 0, 0, 1, 0, 5, 0, 0],
    [4, 0, 0, 0, 0, 5, 3, 0, 0],
    [0, 1, 0, 0, 7, 0, 0, 0, 6],
    [0, 0, 3, 2, 0, 0, 0, 8, 0],
    [0, 6, 0, 5, 0, 0, 0, 0, 9],
    [0, 0, 4, 0, 0, 0, 0, 3, 0],
    [0, 0, 0, 0, 0, 9, 7, 0, 0]
    ]

# 芬兰数学家因卡拉，花费3个月时间设计出了世界上迄今难度最大的数独游戏，而且它只有一个答案
arr2=[
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0]
]


def showarr(arr):
    for i in range(9):
        for j in range(9):
            print(arr[i][j], end=' ')
            if (j + 1) % 3 == 0 and j != 8:
                print('| ', end = '')
        print('')
        if (i + 1) % 3 == 0 and i != 8:
            print('------+-------+------')


def check(i, j, k, arr):
    for n in range(0, 9):
        if arr[i][n]==k or arr[n][j]==k or arr[(i//3)*3+n//3][(j//3)*3+n%3]==k :return 0
    return 1


# 递归法，尝试所有可能
def digui(i, j, arr):
    if i == 9 :
        showarr(arr)
        sys.exit()
    if arr[i][j] > 0: digui(i if j < 8 else i + 1, (j + 1) % 9, arr)
    for k in range(1,10):
        if check(i, j, k, arr):
            arr[i][j] = k
            digui(i if j < 8 else i + 1, (j + 1) % 9, arr)
            arr[i][j]=0


# 给为0的空格写上[1 - 9]的列表
def fill_zero_with_list(arr):
    dd = {}
    for i in range(9):
        for j in range(9):
            if arr[i][j] == 0:
                dd[i * 10 + j] = [n for n in range(1, 10)]
    return dd


def paichu(arr):
    num = 0
    curPos = fill_zero_with_list(arr)
    curPos[1].remove(1)
    print(curPos)

    



# digui(0, 0, arr2)
paichu(arr2)