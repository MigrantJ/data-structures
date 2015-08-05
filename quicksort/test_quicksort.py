import quicksort as q


def test_random_list():
    lst = [4, 3, 8, 5, 0, 2, 56, 9, 68, -1]
    q.quicksort(lst, q.hoare)
    assert lst == [-1, 0, 2, 3, 4, 5, 8, 9, 56, 68]


def test_empty_list():
    lst = []
    q.quicksort(lst, q.hoare)
    assert lst == []


def test_list_of_one():
    lst = [1]
    q.quicksort(lst, q.hoare)
    assert lst == [1]


def test_duplicates():
    lst = [1, 2, 1, 2, 1, 2, 1, 2]
    q.quicksort(lst, q.hoare)
    assert lst == [1, 1, 1, 1, 2, 2, 2, 2]


def test_all_duplicates():
    lst = [1, 1, 1, 1]
    q.quicksort(lst, q.hoare)
    assert lst == [1, 1, 1, 1]


def test_alphabet():
    lst = ['a', 'b', 'f', 'e', 'y', 'w', 'i', 'c', 'p']
    q.quicksort(lst, q.hoare)
    assert lst == ['a', 'b', 'c', 'e', 'f', 'i', 'p', 'w', 'y']
