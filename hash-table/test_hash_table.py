import pytest
from hash_table import HashTable


@pytest.fixture()
def testhash():
    return HashTable(1024)


def test_one_entry(testhash):
    testhash.set('key', 'val')
    assert testhash.get('key') == 'val'


def test_empty_key(testhash):
    with pytest.raises(TypeError):
        testhash.set('', 'empty')


def test_duplicate_key(testhash):
    testhash.set('leopard', 'spots')
    testhash.set('leopard', 'whiskers')
    assert testhash.get('leopard') == 'whiskers'


def test_non_string_key(testhash):
    with pytest.raises(TypeError):
        testhash.set(1, 'one')
        testhash.set(False, 'false')


def test_word_dict(testhash):
    with open("/usr/share/dict/words", "r") as words:
        for word in words:
            word.strip()
            testhash.set(word, word)

            assert testhash.get(word) == word
