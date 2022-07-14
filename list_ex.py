# Lists opertions basics

from copy import deepcopy       #to create true copy of list

a = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
b = [18,19,20,21,22,23,24,25]

# Creating list with constructor
c_list = list(("Apple", "Banana", "Mango"))
print(c_list)
print(type(c_list))


# Creating copy of list
a_cp = deepcopy(a)
# print(f"Original list: {a}")
# print(f"Copied list:   {a_cp}", "\n")


# Length of list
l = len(a)
# print(f"Length of list is: {l}", "\n")


# Appending item in list at last
a_cp.append("Last_item")
# print(f"Appended list: {a_cp}")


# Remove last item from list
a_cp.pop()
# print(f"Pop last item: {a_cp}", "\n")


# Insering item as per index number
a_cp.insert(5, "inserted")
# print(f"Insert at a_cp[5]: {a_cp}", "\n") 

# Changing the value of index
a_cp[0] = "channge value of index 0"
# print(a_cp)


# Counting number of elements with specific values present in list
count = a_cp.count(2)
# print(f"2s present in list are: {count}", "\n")


# Printing list using slicing
s = a[:] # s = a[0:]
#print(f"Slicing entire list: {s}")


# Printing desired array of elemnts based on index numbers
d = a[3:10]  #including index_3 but excluding index_10
# print(f"Original list: {a}")
# print(f"Desired list 3-9: {d}")


# Hopping list 
h = a[0::2]
# print(f"Original list:                        {a}")
# print(f"Printing every 2nd element from list: {h}")


# Trick to reverse list
r = a[::-1]
# print(f"Original list: {a}")
# print(f"Reversed list: {r}")


# Converting list of strings into string
str_list = ["apple", "banana", "pitch", "mango"]
my_str = ",".join(str_list)
# print(str_list)
# print(my_str)
# print(type(my_str))


# converting 2 lists into one
single_list = a+b
# print(f"a is: {a}")
# print(f"b is: {b}")
# print(single_list)