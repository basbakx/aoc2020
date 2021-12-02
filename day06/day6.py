# part 1
# f = open('/Users/bas/Desktop/day6/input.txt', 'r')
# content = f.read()
# x = content.split('\n\n')
#
# cleaned = []
# for xx in x:
#     clean = xx.replace('\n', '')
#     clean = ''.join(set(clean))
#     cleaned.append(clean)
#
# result = 0;
# for val in cleaned:
#     result += len(val)
#
# print result


f = open('/Users/bas/Desktop/day6/input.txt', 'r')
x = f.read().strip().split('\n\n')

cleaned = []
for xx in x:
    aset = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
    xx = xx.split('\n')
    list = []
    for yy in xx:
        aset = aset.intersection(yy)
        list.append(set(yy))
    aset = ''.join(aset)
    cleaned.append(aset)
result = 0;
for val in cleaned:
    result += len(val)

print result
