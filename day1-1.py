with open('./input.txt', 'r') as f:
    lines = f.readlines()

l1 = []
l2 = []

for line in lines:
    values = line.split()
    if len(values) == 2:
        l1.append(int(values[0]))
        l2.append(int(values[1]))

len = 0
for a,b in zip(sorted(l1), sorted(l2)):
    len += abs(a-b)

print(len)
