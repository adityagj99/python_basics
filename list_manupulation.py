# return list which contains common elements from two lists


list1 = [3, 4, 5, 6, 2, 1, 4, 9, 0, -2, 7]
list2 = [-3, 8, 5, 6, 2, 1, -5, 9, 12, -2, 11]

list3 = []
list4 = []
list5 = set(list4)

for i in range(len(list1)):
    temp = list1[i]
    for j in range(len(list2)):
        if temp == list2[j]:
            list3.append(temp)
        else:
            list4.append(temp)
list5 = list(set(list4))
print(f"comman elements are: {list3}")
print(f"uncomman elements are: {list5}")
