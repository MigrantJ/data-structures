from timeit import timeit


def insertion_sort(lst):
    for i in range(len(lst) - 1):
        j = i
        while j > 0 and lst[j-1] > lst[j]:
            lst[j], lst[j-1] = lst[j-1], lst[j]
            j = j - 1
    return lst


if __name__ == '__main__':

    setup = '''
from __main__ import insertion_sort
lst = [a for a in range(10000)]
lst_reverse = lst[::-1]
    '''

    print("Best Case Performance: Sorted List " +
          str(timeit("insertion_sort(lst)",
              setup=setup, number=10000)))
    print("Worst Case Performance: Reverse Sorted List " +
          str(timeit("insertion_sort(lst_reverse)", setup=setup, number=10000)))
