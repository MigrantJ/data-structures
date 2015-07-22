import pytest
from bst import Tree


def fill_tree(l):
    out = Tree()
    for n in l:
        out.insert(n)
    return out

@pytest.fixture()
def tree():
    return Tree()


@pytest.fixture()
def right_unbal_vals():
    return fill_tree([8, 10, 3, 16, 14, 47, 13])


@pytest.fixture()
def left_unbal_vals():
    return fill_tree([11, 6, 19, 4, 8, 17, 43, 5, 10, 31, 49, 1])


@pytest.fixture()
def bal_vals():
    return fill_tree([31, 12, 37, 5, 21, 35, 77])


@pytest.fixture()
def two_levels():
    return fill_tree([15, 10, 20])


def test_internals(tree):
    tree.insert(1)
    assert tree._head is not None


def test_contains(tree):
    tree.insert(1)
    assert tree.contains(1)
    assert not tree.contains(2)
    tree.insert(2)
    assert tree.contains(2)


def test_size(tree, two_levels, bal_vals):
    assert tree.size() == 0
    assert two_levels.size() == 3
    assert bal_vals.size() == 7


def test_depth(tree, two_levels, bal_vals):
    assert tree.depth() == 0
    tree.insert(1)
    assert tree.depth() == 1
    assert two_levels.depth() == 2
    assert bal_vals.depth() == 3


def test_balance(tree, right_unbal_vals, left_unbal_vals, bal_vals):
    assert tree.balance() == 0
    assert right_unbal_vals.balance() < 0
    assert left_unbal_vals.balance() > 0
    assert bal_vals.balance() == 0
