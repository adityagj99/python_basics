# index of minimum & maximum value

a = [23, 76, 45, 20, 70, 65, 15, 54]

max = 0
temp = 0
index = 0
for i in range(len(a)):
    if a[i]>temp:
        temp = a[i]
        index = i

current_index = 1
min_index = 0

while current_index < len(a):
    if a[current_index] < a[min_index]:
        min_index = current_index
    current_index += 1


print(f"Maximum value index is: {index}")
print(f"Minimum value index is: {min_index}")
