from collections import defaultdict

# parse input.
rules = []
for _, line in enumerate(open("/Users/bas/Desktop/day7/input.txt").read().strip().split("\n")):
    outer, b = line.replace("bags", "").replace("bag", "").split("contain")
    for c in b.replace(".", "").replace("no ", "0 no ").split(","):
        d = c.strip().split(" ")
        rules.append((outer.strip(), " ".join(d[1:]), int(d[0])))

print rules
# part 1.
leads_to_gold = {"shiny gold"}
for outer, inner, n in rules * 10:
    if inner in leads_to_gold:
        leads_to_gold.add(outer)

# part 2.
bags = defaultdict(list)
for outer, inner, n in rules:
    bags[outer].extend(bags[inner] for _ in range(n))

count = lambda xs: len(xs) + sum(count(x) for x in xs)

# print results.
print len(leads_to_gold) - 1, count(bags["shiny gold"])
