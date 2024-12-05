from collections import defaultdict

with open('./day1-1-input.txt', 'r') as f:
    lines = f.readlines()

l1 = []
l2 = []

for line in lines:
    values = line.split()
    if len(values) == 2:
        l1.append(int(values[0]))
        l2.append(int(values[1]))

len = 0
sim1 = defaultdict(int)
for k in l1:
    sim1[k] += 1
sim2 = defaultdict(int)
for k in l2:
    sim2[k] += 1

similarity_score = 0
for left in l1:
    similarity_score += left * sim2.get(left, 0)

print(similarity_score)
