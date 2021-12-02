# import math
#
#
# f = open('/Users/bas/Desktop/day5/input.txt', 'r')
# content = f.read()
# boardList = content.split('\n')
#
# rowNum = 128;
# columnNum = 0;
# ids = list(range(0, 998))
# print ids
# print boardList
#
# def id():
#     return False
#
#
# def boardingPass(val, low, high, number, start):
#     counter = 1 - start
#     pos = 0
#     for let in val:
#         rows = number
#         if let == high:
#             for i in range(counter):
#                 rows = rows / 2
#         elif let == low:
#             rows = 0;
#         else:
#             rows = 0
#         pos += rows
#         counter += 1
#     return pos
#
# highest = 100
#
# for board in boardList:
#     rowVal = boardingPass(board, 'F', 'B', 128, 0)
#     colVal = boardingPass(board, 'L', 'R', 8, 7)
#     value = rowVal * 8 + colVal
#     if value > highest:
#         highest = value
# print highest


#part 2
import math


f = open('/Users/bas/Desktop/day5/input.txt', 'r')
content = f.read()
boardList = content.split('\n')

rowNum = 128;
columnNum = 0;
ids = list(range(300, 999))
# print ids
# print boardList

def id():
    return False


def boardingPass(val, low, high, number, start):
    counter = 1 - start
    pos = 0
    for let in val:
        rows = number
        if let == high:
            for i in range(counter):
                rows = rows / 2
        elif let == low:
            rows = 0;
        else:
            rows = 0
        pos += rows
        counter += 1
    return pos

highest = 0

for board in boardList:
    rowVal = boardingPass(board, 'F', 'B', 128, 0)
    colVal = boardingPass(board, 'L', 'R', 8, 7)
    value = rowVal * 8 + colVal
    if value in ids:
        ids.remove(value)
print ids
