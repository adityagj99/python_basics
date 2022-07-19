# Group Elements of Same Indices using Python

from copy import deepcopy
a = [
    [10,20,30],
    [40,50,60],
    [70,80,90]]

# Approch 1
b = deepcopy(a)
print(b)

n = 0
for i in range(len(a)):
    for j in range(len((a))):
        b[j][n] = a[i][j]
    n += 1
print(b)

# Approch 2
c = []
n = 0   

for i in range(len(a[0])):
    c.append([])
    for j in range(len(a)):
        c[n].append(a[j][n])
    n += 1
print(c)