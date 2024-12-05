with open('./day2-1-input.txt', 'r') as f:
    lines = f.readlines()


def is_safe(vals):
    assert(len(vals)>2)
    safe = True
    ldiff = 0
    for v in (range(0, len(vals)-1)):
        diff = vals[v] - vals[v+1]
        if (4 > diff > 0 and ldiff >= 0) or \
                (-4 < diff < 0 and ldiff <= 0):
            ldiff = diff
        else:
            return False
    return safe

def is_safe_with_dampen(values):
    for v in range(0, len(values)):
        copy_list = values.copy()
        del copy_list[v]
        if is_safe(copy_list):
            return True
    return False

safe = 0
for line in lines:
    values = line.split()
    values = [int(v) for v in values]
    if is_safe(values):
        safe += 1
    else:
        if is_safe_with_dampen(values):
            safe +=1 


print(safe)
