'''
Astrics pyramid program using 2 for lopps/nested loop
'''
row = int(input('Enter the number of rows: '))
for i in range(row):
    for j in range(i):
        print('*', end =" ")
    print(" ")

for k in range(row,0,-1):
    l = k
    for l in range(k):
        print('*', end=' ')
        l -=1
    print(' ')
