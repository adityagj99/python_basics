# Finding frequency of words

from collections import Counter

if __name__ == "__main__":

    with open("/home/saffy/Desktop/fake.txt", "r") as file:
        f = file.read().split(" ")

        freq = Counter(f)
print((freq))