int_list = input("Enter numbers: ")
int_list = list(map(int,int_list.split()))
print(int_list)
compare = 0

for i in range(len(int_list)):
    if int_list[i]>compare:
        compare = int_list[i]
print("Maximun number is:", compare)

for i in range(len(int_list)):
    if int_list[i]<compare:
        compare = int_list[i]
print("Minimum_number_is:", compare)