#!/usr/bin/env python3
# -*- coding:utf-8 -*-
__author__ = 'zijing'
###################################################
# Created : 2021-05-03 14:32:06
# Author  : zijing (zijing412@163.com)
# Version : 1.0.0
###################################################

from random import randint

flag = 'flag_success!'

print('你要在10次机会内猜中 0 - 1000之间的数')
dest_num = randint(0, 1000)
try_count = 10
exit_msg = '很遗憾你没有猜中，请再接再厉'
print(dest_num)

while (try_count > 0):
    try_count -= 1
    guess_num = int(input('请输入你要猜的数: '))

    if guess_num > dest_num:
        print('你猜测的数 {} 偏大了，剩余 {} 次机会'.format(guess_num, try_count))
    elif guess_num < dest_num:
        print('你猜测的数 {} 偏小了，剩余 {} 次机会'.format(guess_num, try_count))
    else:
        exit_msg = flag
        break

print(exit_msg)
input('按任意键退出')