# finding small and capital words

with open("/home/saffy/Desktop/fake.txt", "r") as file:
    f = file.read().split()

C_count = 0
s_count = 0
other = 0
for i in f:
    if i.isupper():
        C_count += 1
    elif i.islower():
        s_count += 1
    else:
        other += 1

print(f"Capital letters are: {C_count}")
print(f"Small letters are: {s_count}")
print(f"Other: {other}")