#part 1
import re
import itertools

f = open('/Users/bas/Desktop/AoC/day9/input.txt', 'r')
input = f.read().strip().split('\n')
while("" in input) :
    input.remove("")
#
# preamble = 25
# counter = 0
# def check(num):
#     global counter
#     counter += 1
#     sublist = []
#     sublist2 = []
#     if counter > preamble:
#         sublist = list(itertools.combinations(input[counter-(preamble+1):counter-1], 2))
#         for x in sublist:
#             z = int(x[0]) + int(x[1])
#             sublist2.append(str(z))
#         if not num in sublist2:
#             print(num)
# for y in input:
#     check(y)

# 552655238

number = 552655238

increaser = 2
def rec():
    global counter
    global increaser
    low = 0
    high = 1
    comblist = []
    for count, x in enumerate(input):
        result = 0
        for r in range(increaser):
            # print('r', r)
            # print('count', count)
            if count + r < len(input):
                # print(int(input[count+r]))
                result += int(input[count+r])
            # print('result', result)
        comblist.append(result)
    # print(comblist)
    if int(number) in comblist:
        low = comblist.index(number)
        high = comblist.index(number) + increaser
        mini = min(input[low:high])
        maxi = max(input[low:high])
        print(len(input[low:high]))
        print('mini', mini)
        print('maxi', maxi)
        print('increaser', increaser)
        print(input[low:high+1])
        print('result', int(mini) + int(maxi))

    else:
        increaser += 1
        if increaser != 50:
            rec()

rec()
