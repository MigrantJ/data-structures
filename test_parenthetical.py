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
    assert parens('(a tes(t )string)') == 0
    assert parens('(awerbw(r)tnw45nwrtn') == 1
    assert parens('a(;;,blk)nqw)3po') == -1
