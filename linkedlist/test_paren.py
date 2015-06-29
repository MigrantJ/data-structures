from __future__ import unicode_literals
import pytest
from johnsonparen import paren

emptyStr = ""
completeStr = "()()()()()()()()"
brokenStr = ")((((((((((((("
openStr = "()()()(((())((((())(("

def test_paren():
    # assert paren(emptyStr) == 0
    assert paren(completeStr) == 0
    assert paren(brokenStr) == -1
    assert paren(openStr) == 1
