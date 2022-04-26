import pytest
from yandex_testing_lesson import Rectangle


def test_empty():
    assert (Rectangle(5, 100).get_perimeter() == 210)


def test_empty1():
    assert (Rectangle(5, 55).get_area() == 5 * 55)


def test_empty1():
    assert (Rectangle(5, 10).get_perimeter() == 30)


def test_str():
    assert (Rectangle(5, 5).get_area() == 25)


def test_wrong_type_list():
    with pytest.raises(TypeError):
        Rectangle('')


def test_wrong_type_list1():
    with pytest.raises(TypeError):
        Rectangle(list(5))


def test_wrong_type_value():
    with pytest.raises(ValueError):
        Rectangle(-1 / 5, 5)


def test_wrong_type_value1():
    with pytest.raises(ValueError):
        Rectangle(-5, 65)


def test_wrong_type_value2():
    with pytest.raises(ValueError):
        Rectangle(-5, -5)
