from merge import merge_sort


def test_random_list():
    lst = merge_sort([4, 3, 8, 5, 0, 2, 56, 9, 68, -1])
    assert lst == [-1, 0, 2, 3, 4, 5, 8, 9, 56, 68]


def test_empty_list():
    lst = merge_sort([])
    assert lst == []


def test_alphabet():
    lst = merge_sort(['a', 'b', 'f', 'e', 'y', 'w', 'i', 'c', 'p'])
    assert lst == ['a', 'b', 'c', 'e', 'f', 'i', 'p', 'w', 'y']


def test_empty_string():
    lst = merge_sort([2, 5, 'a', 7, 'd', 0, '', 'o'])
    assert lst == [0, 2, 5, 7, '', 'a', 'd', 'o']
