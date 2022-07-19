# Finding missing number from list

l = [1,2,3,4,6,7,10]
a = l[-1]
t = []

#for i in range(len(l)+1):

for i in range(a):
    if i not in l:
        t.append(i)

print(t)
