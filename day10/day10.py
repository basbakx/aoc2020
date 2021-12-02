import re
import itertools

# f = open('/Users/bas/Desktop/day9/input.txt', 'r')
# input = f.read().strip().split('\n')

with open('/Users/bas/Desktop/AoC/day10/input.txt') as f:
    input = [ int(y) for y in f ]

input.append(0)
input.append(max(input)+3)
sortedInput = sorted(input)
print(sortedInput)

count1 = 0
count3 = 0

tel = 1
def check(number):
    global tel
    if number + tel < len(sortedInput) and sortedInput[number] <= sortedInput[number + tel]:
        # print('num', number+tel - 1, len(sortedInput) )
        tel += 1
    else:
        ret = tel
        tel = 1
        return ret

for count, y in enumerate(sortedInput):
    if count + 1 < len(sortedInput):
        res = sortedInput[count+1] - y
        if res == 1:
            count1 += 1
        elif res == 3:
            count3 += 1


# result= (len(sortedInput) * (len(sortedInput) - count3))
print('part 1:', count1*count3)

tot = 1
def func(num, numc):
    global tot
    if num + numc + 1 < len(sortedInput) and sortedInput[count] + 3 > sortedInput[count + numc] and sortedInput[count] + 3 >= sortedInput[count + numc + 1]:
        numc += 1
        func(num, numc)
    else:
        print('num', num, 'numc', numc)
        tot = tot*numc

res = 1
for count, y in enumerate(sortedInput):
    func(count, 1)

print(tot)
