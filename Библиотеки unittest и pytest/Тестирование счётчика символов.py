import pytest
from yandex_testing_lesson import count_chars


def test_empty():
    assert (count_chars('') == dict())


def test_str():
    assert (count_chars('aab') == {'a': 2, 'b': 1})


def test_wrong_type_list():
    with pytest.raises(TypeError):
        count_chars(5)
