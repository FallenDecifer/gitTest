import math_func as m


def test_add():
    assert m.add(1, 2) == 3
    assert m.add(2, 5) == 7
    assert m.add(3) == 6


def test_product():
    assert m.product(1) == 6
    assert m.product(2, 2) == 4



