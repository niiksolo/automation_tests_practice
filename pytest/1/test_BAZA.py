import pytest

def division(a, b):
    return a / b

@pytest.mark.parametrize(           # параметризация тестов
    'a, b, res',
    [
        (10, 2, 5),
        (20, 10, 2),
        (5, 2, 2.5)
    ]
)
def test_division(a, b, res):
    assert division(a, b) == res

def test_division_with_error():           #мы говорим что результат будет ошибка деления на ноль и тест проходит успешно
    with pytest.raises(ZeroDivisionError):
        division(10, 0)

def test_type_error():
    with pytest.raises(TypeError):
        division(4, '2')