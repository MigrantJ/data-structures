from __future__ import unicode_literals
from timeit import timeit


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
        while len(buckets) == 0 or len(buckets[0]) < len(list_):
            buckets = []
            for _ in range(abs(radix)):
                buckets.append([])

            for i in list_:
                buckets[abs(i // divisor % radix)].append(i)

            list_ = []
            for bucket in buckets:
                list_.extend(bucket)

            divisor *= radix
    return list_
