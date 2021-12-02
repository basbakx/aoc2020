# part 1
# f = open('/Users/bas/Desktop/day4/input.txt', 'r')
# content = f.read()
# x = content.split('\n\n')
# cleaned = []
# for xx in x:
#     clean = xx.replace('\n', ';')
#     clean = clean.replace(' ', ';')
#     clean = clean.rstrip(';')
#     d = dict(x.split(":") for x in clean.split(";"))
#     cleaned.append(d)
# result = 0
# for di in cleaned:
#     if 'byr' in di and 'iyr' in di and 'eyr' in di and "hgt" in di and 'hcl' in di and 'ecl' in di and 'pid' in di:
#         result += 1
# print result

# # part 2
f = open('/Users/bas/Desktop/day4/input.txt', 'r')
content = f.read()
x = content.split('\n\n')
import re

def check(val):
    if int(val['byr']) < 1920 or int(val['byr']) > 2002:
        return False
    if int(val['iyr']) < 2010 or int(val['iyr']) > 2020:
        return False
    if int(val['eyr']) < 2020 or int(val['eyr']) > 2030:
        return False
    if 'in' in val['hgt'] or 'cm' in val['hgt']:
        if 'in' in val['hgt']:
            height = val['hgt'].rstrip('in')
            if  int(height) < 59 or int(height) > 76:
                return False
        if 'cm' in val['hgt']:
            height = val['hgt'].rstrip('cm')
            if int(height) < 150 or int(height) > 193:
                return False
    else:
        return False
    if val['hcl'][0] == '#':
        for let in val['hcl']:
            hairc = re.match("[#a-f0-9]", let)
            if bool(hairc) == False:
                return False
    else:
        return False
    matches = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if not any(x in val['ecl'] for x in matches):
        return False
    if len(val['pid']) != 9:
        return False
    return True
cleaned = []
for xx in x:
    clean = xx.replace('\n', ';')
    clean = clean.replace(' ', ';')
    clean = clean.rstrip(';')
    d = dict(x.split(":") for x in clean.split(";"))
    cleaned.append(d)

result = 0

for di in cleaned:
    if 'byr' in di and 'iyr' in di and 'eyr' in di and "hgt" in di and 'hcl' in di and 'ecl' in di and 'pid' in di:
        if check(di):
            result += 1
print result
