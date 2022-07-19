# Removing duplicate items from list

s = [1,2,3,4,5,6,7,45,4,2,2,34,54,74,24,3,24,6,13,254,657,2,34,45,43445,2,3,45,23]
t = []
for i in range(len(s)):
    n = len(s)
    for j in range(i+1,n):
        if (s[i] == s[j]) and (s[i] not in t):
            t.append(s[i])

print(t)
