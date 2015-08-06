from __future__ import unicode_literals
import sys


def radix_sort(list_, radix=10):
    buckets = []
    divisor = 1

    negatives = []
    positives = []

    for i in list_:
        if i < 0:
            negatives.append(i)
        else:
            positives.append(i)

    if len(negatives) > 0 and len(positives) > 0:
        list_ = radix_sort(negatives, radix * -1)[::-1] + radix_sort(positives)
    else:
        found_max_length = False
        while not found_max_length:
            found_max_length = True
            buckets = []
            for _ in range(abs(radix)):
                buckets.append([])

            for i in list_:
                divided = i // divisor
                if found_max_length and abs(divided) > 0:
                    found_max_length = False
                buckets[abs(divided % radix)].append(i)

            list_ = []
            for bucket in buckets:
                list_.extend(bucket)

            divisor *= radix
    return list_


if __name__ == '__main__':
    sys.setrecursionlimit(5000)
    from timeit import timeit

    setup = '''
from __main__ import radix_sort
import random
worst_case = [random.randint(0, 9) for x in range(10000)]
best_case = [random.randint(10000, 10010) for x in range(10000)]
    '''

    print("Best Case Performance: " +
          str(timeit("radix_sort(worst_case)",
                     setup=setup, number=1000)))
    print("Worst Case Performance: " +
          str(timeit("radix_sort(best_case)", setup=setup,
                     number=1000)))
