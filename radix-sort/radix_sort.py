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
