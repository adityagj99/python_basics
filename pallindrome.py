#Palindrome check

l = "ababa"
# print(l[::-1])
# print(l[::])

# if l[::] == l[::-1]:
#     print("pallendrom")
# else:
#     print("No")

# print(type(l))
# print(l)
# print(l.split())
temp = True
for i in range(len(l)):
    # print(i, -i)
    print(l[i], l[-i-1])
    if l[i] != l[-i-1]:
        # i += 1
        temp = False
        break

if temp == True:
    print('String is palindrome')
else:
    print("String isn't palindrome")