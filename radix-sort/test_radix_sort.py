import radix_sort as r
import pytest


@pytest.fixture()
def randlist():
    return [4, 3, 8, 5, 0, -1, 2, 56, -23, 9, 68, -9999]


@pytest.fixture()
def randlist_sorted():
    return [-9999, -23, -1, 0, 2, 3, 4, 5, 8, 9, 56, 68]


def test_random_list(randlist, randlist_sorted):
    lst = randlist[:]
    new_lst = r.radix_sort(lst)
    assert new_lst == randlist_sorted


def test_empty_list():
    lst = []
    new_lst = r.radix_sort(lst)
    assert new_lst == []


def test_list_of_one():
    lst = [1]
    new_lst = r.radix_sort(lst)
    assert new_lst == [1]


def test_duplicates():
    lst = [1, 2, 1, 2, 1, 2, 1, 2]
    new_lst = r.radix_sort(lst)
    assert new_lst == [1, 1, 1, 1, 2, 2, 2, 2]


def test_all_duplicates():
    lst = [1, 1, 1, 1]
    new_lst = r.radix_sort(lst)
    assert new_lst == [1, 1, 1, 1]
