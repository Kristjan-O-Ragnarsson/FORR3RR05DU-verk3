"""
Made By Kristjan O. Ragnarsson
github.com/Kristjan-O-Ragnarsson

Q1: yes the lenght of the string matter for the combinations function

Q2: O(k*n!), _n = 20 og _m = 400 time it took to sort: 0.0038001549399722208
"""
from time import perf_counter
from sys import stdout, stdin
from itertools import combinations
from string import ascii_lowercase

write, readln = stdout.write, stdin.readline

S, I, F, N, W = str, int, float, '\n', ' '


def ascci_set_comb(_n, _m):
    """
    :param _n: length of string
    :param _m: length of list
    :return: set of string in rev order
    """
    _m += 1 # for zero index
    x = list(combinations(ascii_lowercase, _n))  # O(k*n!)
    return tuple(x[:len(x) - _m:-1])  # O(k)


i_t = ascci_set_comb(20, 400)
write(S(i_t) + N)
s1_start = perf_counter()
write(S(sorted(i_t, key=lambda x: x[0])) + N)  # O(n log n)
s1_stop = perf_counter()
write(S(s1_stop - s1_start))
