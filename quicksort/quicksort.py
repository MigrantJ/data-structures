from __future__ import unicode_literals
from random import randint
from timeit import timeit
import sys


def rand_pivot(lst, lo, hi):
    i = randint(lo, hi)
    pivot = lst[i]
    for j in range(lo, hi):
        if lst[j] <= pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    return i


def quicksort(lst, pivot_method=rand_pivot, lo=0, hi=None):
    hi = len(lst) - 1 if hi is None else hi
    if lo < hi:
        pvt = pivot_method(lst, lo, hi)
        quicksort(lst, pivot_method, lo, pvt - 1)
        quicksort(lst, pivot_method, pvt + 1, hi)


def hoare(lst, lo, hi):
    pivot = lst[hi]
    i = lo
    j = hi - 1
    while True:
        while lst[i] < pivot:
            i += 1
        while lst[j] > pivot:
            j -= 1
        if i < j:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
        else:
            lst[i], lst[hi] = lst[hi], lst[i]
            return i


def lomuto(lst, lo, hi):
    pivot = lst[hi]
    i = lo - 1
    for j in range(lo, hi):
        if lst[j] <= pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    i += 1
    lst[i], lst[hi] = lst[hi], lst[i]
    return i


if __name__ == '__main__':
    sys.setrecursionlimit(5000)

    setup = '''
from __main__ import quicksort, lomuto, hoare
import random
best_case = [random.randint(0, 500) for x in range(500)]
worst_case_hoare = [x for x in range(500)]
worst_case_lomuto = [x for x in range(500)]
worst_case_lomuto.reverse()
    '''

    print("Best Case Performance Lomuto: " +
          str(timeit("quicksort(best_case, lomuto)",
              setup=setup, number=1000)))
    print("Worst Case Performance Lomuto: " +
          str(timeit("quicksort(worst_case_lomuto, lomuto)", setup=setup,
              number=1000)))
    print("Best Case Performance Hoare: " +
          str(timeit("quicksort(best_case, hoare)",
              setup=setup, number=1000)))
    print("Worst Case Performance Hoare: " +
          str(timeit("quicksort(worst_case_hoare, hoare)", setup=setup,
              number=1000)))
