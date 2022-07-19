# findig anagrams

from collections import defaultdict

words = ["tea", "eat", "bat", "ate", "arc", "car", "act", "cat"]


my_dict = defaultdict(list)
print(my_dict)

for i in words:
    l = str(i)
    sorted_l = " ".join(sorted(l))
    print(sorted_l)
    my_dict[sorted_l].append(l)

print(my_dict)