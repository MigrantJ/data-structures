from __future__ import unicode_literals
from timeit import timeit


def radix_sort(list_, radix=10):
    buckets = []
    divisor = 1

    while len(buckets) == 0 or len(buckets[0]) < len(list_):
        buckets = []
        for _ in range(radix):
            buckets.append([])

        for i in list_:
            buckets[i // divisor % radix].append(i)

        list_ = []
        for bucket in buckets:
            list_.extend(bucket)

        divisor *= radix
    return list_
