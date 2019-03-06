from itertools import combinations
from string import ascii_lowercase

n = int(input(": "))
t = combinations(ascii_lowercase, n)

for i in t:
    print("".join(i))
