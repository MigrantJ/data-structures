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
    return fill_tree([11, 6, 19, 4, 8, 17, 43, 5, 10])


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


def test_depth(tree, two_levels, bal_vals, right_unbal_vals):
    assert tree.depth() == 0
    tree.insert(1)
    assert tree.depth() == 1
    assert two_levels.depth() == 2
    assert bal_vals.depth() == 3
    assert right_unbal_vals.depth() == 5


def test_balance(tree, right_unbal_vals, left_unbal_vals, bal_vals):
    assert tree.balance() == 0
    assert right_unbal_vals.balance() == -3
    assert left_unbal_vals.balance() == 1
    assert bal_vals.balance() == 0


def test_pre_order(two_levels, bal_vals):
    two_level_list = [n.value for n in list(two_levels.pre_order())]
    assert two_level_list == [15, 10, 20]
    bal_val_list = [n.value for n in list(bal_vals.pre_order())]
    assert bal_val_list == [31, 12, 5, 21, 37, 35, 77]


def test_in_order(two_levels, bal_vals):
    two_level_list = [n.value for n in list(two_levels.in_order())]
    assert two_level_list == [10, 15, 20]
    bal_val_list = [n.value for n in list(bal_vals.in_order())]
    assert bal_val_list == [5, 12, 21, 31, 35, 37, 77]


def test_post_order(two_levels, bal_vals):
    two_level_list = [n.value for n in list(two_levels.post_order())]
    assert two_level_list == [10, 20, 15]
    bal_val_list = [n.value for n in list(bal_vals.post_order())]
    assert bal_val_list == [5, 21, 12, 35, 77, 37, 31]


def test_breadth_first(two_levels, bal_vals):
    two_level_list = [n.value for n in list(two_levels.breadth_first())]
    assert two_level_list == [15, 10, 20]
    bal_val_list = [n.value for n in list(bal_vals.breadth_first())]
    assert bal_val_list == [31, 12, 37, 5, 21, 35, 77]


def test_delete_leaf(two_levels, bal_vals):
    two_levels.delete(10)
    assert two_levels.size() == 2
    assert two_levels.depth() == 2
    assert two_levels.balance() == -1

    bal_vals.delete(21)
    assert bal_vals.size() == 6
    assert bal_vals.depth() == 3
    assert bal_vals.balance() == 0


def test_delete_one_descendant(right_unbal_vals):
    right_unbal_vals.delete(14)
    assert right_unbal_vals.depth() == 4
    assert right_unbal_vals.balance() == -2
    travlist = [n.value for n in right_unbal_vals.pre_order()]
    assert travlist.index(16) < travlist.index(13)

    right_unbal_vals.delete(10)
    travlist = [n.value for n in right_unbal_vals.pre_order()]
    assert travlist.index(13) < travlist.index(16)


def test_delete_two_descendant(right_unbal_vals):
    right_unbal_vals.delete(16)

