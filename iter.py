"""
Q1: with the subset of n and a set of 26 the number of possible combinatons in 26! /( n!*(26 - n)!)

Q2: O(k*n!)

Time                    Run 1   /   Run 2   /   Run 3
n=2 : 2.22148799497309e-05 / 2.5035817086204666e-05 / 2.186226280767168e-05
n=3 : 3.455647992180362e-05 / 2.4683199944145446e-05 / 3.3498628495625955e-05
n=5 : 7.404959983243633e-06 / 2.785675422267843e-05 / 8.815428551480516e-06
n=10 : 2.2920114233849343e-05 / 4.548761132563946e-05 / 2.5035817086204666e-05
n=13 : 2.574105137032311e-05 / 2.5035817086204666e-05 / 2.256749709179012e-05
n=15 : 1.093113140383584e-05 / 1.4104685682368827e-05 / 8.110194267362075e-06
n=20 : 2.22148799497309e-05 / 1.093113140383584e-05 / 3.490909706386285e-05
n=25 : 3.1382925643270636e-05 / 4.337190847328414e-05 / 7.757577125302855e-06
n=26 : 8.110194267362075e-06 / 3.5261714205922064e-05 / 3.4556479921803625e-05

"""
from itertools import combinations
from string import ascii_lowercase
from time import perf_counter
import sys
I = int
N = '\n'
x = I(sys.stdin.readline().strip(N))

s1_start = perf_counter()


def ascii_iter(_n) -> combinations:
    """
    O(k*n!)
    :param _n: len of string
    :return: combination
    """
    return combinations(ascii_lowercase, _n)


t = ascii_iter(x)
s1_stop = perf_counter()
z = 0

for i in t:
    #print("".join(i))
    z += 1

print(z)
print(s1_stop - s1_start)
