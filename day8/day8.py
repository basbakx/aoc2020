from collections import defaultdict
import re

f = open('/Users/bas/Desktop/AoC/day8/input.txt', 'r')
x = f.read().split('\n')

# step 1
# steps = []
# for y in x: steps.append(y.split(' '))
#
# track = []
# acc = 0
# num = 0
#
# def func():
#     global acc
#     global num
#     global track
#
#     track.append(num)
#
#     if steps[num][0] == 'acc':
#         acc += int(steps[num][1])
#         num += 1
#     elif steps[num][0] == 'jmp':
#         num += int(steps[num][1])
#     elif steps[num][0] == 'nop':
#         num += 1
#
#     if num in track:
#         print(acc)
#     else:
#         func()
#
# func()

# step 2

import sys
sys.setrecursionlimit(25000)

steps = []
for y in x:
    if y: steps.append(y.split(' '))

track = []
acc = 0
num = 0
returner = 0

def func():
    global acc
    global num
    global returner
    global track

    track.append(num)

    if num == returner:
        if steps[num][0] == 'acc':
            acc += int(steps[num][1])
            num += 1
        elif steps[num][0] == 'jmp':
            num += 1
        elif steps[num][0] == 'nop':
            num += int(steps[num][1])
    elif steps[num][0] == 'acc':
        acc += int(steps[num][1])
        num += 1
    elif steps[num][0] == 'jmp':
        num += int(steps[num][1])
    elif steps[num][0] == 'nop':
        num += 1

    if num >= len(steps):
        pass
        print(num, 'and', acc, 'and', returner)
    elif num in track:
        acc = 0
        num = 0
        returner += 1
        track.clear()
        func()
    else:
        func()

func()
