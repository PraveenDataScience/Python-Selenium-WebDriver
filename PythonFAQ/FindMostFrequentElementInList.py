l1 = [4, 7, 8, 4, 5, 9, 4, 2, 3, 4, 0, 4, 4]


def most_frequent(l1):
    return max(set(l1), key=l1.count)

print(most_frequent(l1))
print(l1.count(4))

#========================
import statistics
from statistics import mode

def most_ele(l1):
    return mode(l1)

print(most_ele(l1))

