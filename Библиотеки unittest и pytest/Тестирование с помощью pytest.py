import pytest
from yandex_testing_lesson import reverse


def test_empty():
    assert (reverse('') == '')


def test_one():
    assert (reverse('a') == 'a')


def test_pol():
    assert (reverse('aba') == 'aba')


def test_str():
    assert (reverse('abc') == 'cba')


def test_wrong_type_int():
    with pytest.raises(TypeError):
        reverse(42)


def test_wrong_type_list():
    with pytest.raises(TypeError):
        reverse(list('abc'))
