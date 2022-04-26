import pytest
from yandex_testing_lesson import is_under_queen_attack


def test_empty():
    assert (is_under_queen_attack('e5', 'a5'))


def test_empty1():
    assert (is_under_queen_attack('e1', 'a5'))


def test_empty1():
    assert (is_under_queen_attack('e1', 'a5'))


def test_str():
    assert (not is_under_queen_attack('e5', 'a6'))


def test_wrong_type_list():
    with pytest.raises(TypeError):
        is_under_queen_attack(list('a5'), 'a5')


def test_wrong_type_list1():
    with pytest.raises(TypeError):
        is_under_queen_attack(list('a5'), 'abc')


def test_wrong_type_value():
    with pytest.raises(ValueError):
        is_under_queen_attack('a5', 'abc')


def test_wrong_type_value1():
    with pytest.raises(ValueError):
        is_under_queen_attack('abc', 'a10')


def test_wrong_type_value2():
    with pytest.raises(ValueError):
        is_under_queen_attack('a10', list('a5'))
