from __future__ import unicode_literals


def quicksort(lst, pivot_method, lo=0, hi=None):
    hi = len(lst) - 1 if hi is None else hi
    if lo < hi:
        p = pivot_method(lst, lo, hi)
        quicksort(lst, pivot_method, lo, p - 1)
        quicksort(lst, pivot_method, p + 1, hi)


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
        else:
            lst[i], lst[hi] = lst[hi], lst[i]
            return i


def lomuto(lst, lo, hi):
    pivot = lst[hi]
    i = lo - 1
    for j in range(lo, hi):
        if lst[j] <= pivot:
            i = i + 1
            lst[i], lst[j] = lst[j], lst[i]
    i += 1
    lst[i], lst[hi] = lst[hi], lst[i]
    return i


if __name__ == '__main__':
    lst = [1, 5, 4, 7, 9, 3, 65, 7, 2, 6]
    quicksort(lst, lomuto)
    print lst
