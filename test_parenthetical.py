from __future__ import unicode_literals
from parenthetical import parens


def test_parens_odd_input():
    assert parens(None) == 0
    assert parens(1) == 0
    assert parens('') == 0


def test_parens():
    assert parens('()') == 0
    assert parens('()()') == 0
    assert parens('((()(())()))') == 0
    assert parens('(') == 1
    assert parens('(()') == 1
    assert parens('(()()') == 1
    assert parens(')') == -1
    assert parens('()())') == -1
    assert parens('((()(())())))') == -1
    assert parens('(a test string)') == 0
    assert parens('(awerbwrtnw45nwrtn') == 1
    assert parens('a;;,blk)nqw3po') == -1
