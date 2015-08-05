import quicksort as q
import pytest


@pytest.fixture()
def randlist():
    return [4, 3, 8, 5, 0, 2, 56, 9, 68, -1]


@pytest.fixture()
def randlist_sorted():
    return [-1, 0, 2, 3, 4, 5, 8, 9, 56, 68]


def test_random_list(randlist, randlist_sorted):
    lst = randlist[:]
    q.quicksort(lst)
    assert lst == randlist_sorted


def test_empty_list():
    lst = []
    q.quicksort(lst)
    assert lst == []


def test_list_of_one():
    lst = [1]
    q.quicksort(lst)
    assert lst == [1]


def test_duplicates():
    lst = [1, 2, 1, 2, 1, 2, 1, 2]
    q.quicksort(lst)
    assert lst == [1, 1, 1, 1, 2, 2, 2, 2]


def test_all_duplicates():
    lst = [1, 1, 1, 1]
    q.quicksort(lst)
    assert lst == [1, 1, 1, 1]


def test_alphabet():
    lst = ['a', 'b', 'f', 'e', 'y', 'w', 'i', 'c', 'p']
    q.quicksort(lst)
    assert lst == ['a', 'b', 'c', 'e', 'f', 'i', 'p', 'w', 'y']


def test_hoare(randlist, randlist_sorted):
    lst = randlist[:]
    q.quicksort(lst, q.hoare)
    assert lst == randlist_sorted


def test_lomuto(randlist, randlist_sorted):
    lst = randlist[:]
    q.quicksort(lst, q.lomuto)
    assert lst == randlist_sorted
