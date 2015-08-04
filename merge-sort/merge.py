from __future__ import unicode_literals


def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    left = []
    right = []
    middle = len(lst) // 2
    for x in lst[middle:]:
        left.append(x)
    for x in lst[:middle]:
        right.append(x)

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    while len(left) > 0:
        result.append(left[0])
        left = left[1:]
    while len(right) > 0:
        result.append(right[0])
        right = right[1:]
    return result
