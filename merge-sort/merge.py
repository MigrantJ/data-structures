from __future__ import unicode_literals
from timeit import timeit


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


if __name__ == '__main__':

    setup = '''
from __main__ import merge_sort
best_case = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
worst_case = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
    '''

    print("Best Case Performance: Best Case Performance " +
          str(timeit("merge_sort(best_case)",
              setup=setup, number=100000)))
    print("Worst Case Performance: Worst Case Performance " +
          str(timeit("merge_sort(worst_case)", setup=setup,
              number=100000)))
