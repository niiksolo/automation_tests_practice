#from src.main import A
from calculator import Calculator
from contextlib import nullcontext as does_not_raise
import pytest


class TestCalculator:
    @pytest.mark.parametrize(
        'x, y, res, expectation',
        [
            (1, 2, 0.5, does_not_raise()),
            (5, -1, -5, does_not_raise()),
            (5, '1', 5, pytest.raises(TypeError)),
        ]
    )
    def test_divide(self, x, y, res, expectation):
        with expectation:
            assert Calculator().divide(x, y) == res

    @pytest.mark.parametrize(
        'x, y, res, expectation',
        [
            (1, 2, 3, does_not_raise()),
            (5, 1, 6, does_not_raise()),
            (0,'-1', -5, pytest.raises(TypeError)),

        ]
    )
    def test_add(self, x, y, res, expectation):
        with expectation:
            assert Calculator().add(x, y) == res


#def test_main():
#    assert A.x == 1

#def test_2():
#    assert 2 == 2

#def test_sum():
#    x = 1
#    y = 2
#    assert x + y == 3

#def test_division(): #деление
#    x = 1
#    y = 2
#    assert x / y == 0.5
