# part 1
# f = open('/Users/bas/Desktop/day7/input.txt', 'r')
# x = f.read().strip().split('\n')
# rules = []
# for y in x:
#     rul = y.replace(', ', ' ').replace(' contain', '').replace('.', '').split(' bags ')
#     rules.append(rul)
# bags = []
# def fil(stri):
#     for y in rules:
#         if stri in str(y) and y[0] != stri:
#             bags.append(y[0])
#             fil(y[0])
# fil('shiny gold')
# bags = list(dict.fromkeys(bags))
# print(len(bags))

# part 2
import re
f = open('/Users/bas/Desktop/day7/input.txt', 'r')
x = f.read().replace('bags', '').replace('.', '').replace('bag', '').strip().split('\n')
dict = {}
for y in x:
    key, value = y.strip().split('  contain')
    dict[key] = value

for key in dict: 
    dict[key] = dict[key].strip().split(' , ')

bags = []
bags2 = ['shiny gold']
result = []

def func():
    hold = []
    for x in bags2:
        if x != 'no other':
            for y in dict[x]:
                hold.append(y)
    bags2.clear()
    for x in hold:
        if x != 'no other':
            y = re.sub('\d ', '', x)
            for times in range(int(x[0])):
                bags.append(y)
                bags2.append(y)

def recursion():
    stop = len(bags)
    func()
    if len(bags) > stop:
        recursion()

recursion()

print(len(bags))
