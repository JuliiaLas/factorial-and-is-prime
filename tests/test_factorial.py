import sys
import pytest
from src.factorial import factorial


# POSITIVE

# Тест со значением n == 0
@pytest.mark.positive
def test_zero_value():
    assert factorial(0) == 1


# Тест со значением n == 1:
@pytest.mark.positive
def test_one_value():
    assert factorial(1) == 1


# Тест со значением n == 998:
@pytest.mark.xfail(reason='test should be run separately, the max recursion depth may be exceeded')
def test_max_value():
    try:
        sys.setrecursionlimit(1029)  # лимит увеличен, так как рекурсивная функция помещена в стек доп.вызовов функции test_max_value
        factorial(998)
    except RecursionError:
        pytest.fail("maximum recursion depth exceeded")


# Тест со значением n == 50, 255, 700:
@pytest.mark.positive
@pytest.mark.parametrize('value', [50, 255, 700])
def test_interim_values(value):
    factorial(value)


# Тест со значением n == 0000:
@pytest.mark.positive
def test_nulls_value():
    factorial(0000)


# Тест со значением вычисления математических операций:
@pytest.mark.positive
@pytest.mark.parametrize('value', [100/2, 30 * 2, 78 - 5, 3 + 5])
def test_math_operations_values(value):
    factorial(value)


# Тест со значением n == 30.0:
@pytest.mark.positive
def test_dot_null_value():
    factorial(30.0)



# NEGATIVE

# Тест со значением n == -1:
@pytest.mark.negative
def test_negative_value():
    with pytest.raises(RecursionError) as exception:
        factorial(-1)
    assert "maximum recursion depth exceeded" in str(exception.value)


# Тест со значением n == 999:
@pytest.mark.negative
def test_recursion_exceeded():
    with pytest.raises(RecursionError) as exception:
        sys.setrecursionlimit(1029)  # лимит увеличен, так как рекурсивная функция помещена в стек доп.вызовов функции test_max_value
        factorial(999)
    assert "maximum recursion depth exceeded" in str(exception.value)


# Тест со значением n == 3.5:
@pytest.mark.negative
def test_float_value():
    with pytest.raises(RecursionError) as exception:
        factorial(3.5)
    assert "maximum recursion depth exceeded" in str(exception.value)


# Тест со значением n == 'hello':
@pytest.mark.negative
def test_string_value():
    with pytest.raises(TypeError) as exception:
        factorial('hello')
    assert "unsupported operand type(s) for -: 'str' and 'int'" in str(exception.value)


# Тест со значением n == [0, 1, 2]:
@pytest.mark.negative
def test_list_value():
    with pytest.raises(TypeError) as exception:
        factorial([0, 1, 2])
    assert "unsupported operand type(s) for -: 'list' and 'int'" in str(exception.value)


# Тест со значением n == {'value': 5}:
@pytest.mark.negative
def test_dict_value():
    with pytest.raises(TypeError) as exception:
        factorial({'value': 5})
    assert "unsupported operand type(s) for -: 'dict' and 'int'" in str(exception.value)


# Тест со значением n == (40, 55, 40):
@pytest.mark.negative
def test_tuple_value():
    with pytest.raises(TypeError) as exception:
        factorial((40, 55, 40))
    assert "unsupported operand type(s) for -: 'tuple' and 'int'" in str(exception.value)


# Тест со пустым значением n == None:
@pytest.mark.negative
def test_none_value():
    with pytest.raises(TypeError) as exception:
        factorial()
    assert "factorial() missing 1 required positional argument: 'n'" in str(exception.value)


# Тест со значением деления с остатком n == 100/3:
@pytest.mark.negative
def test_div_rem_value():
    with pytest.raises(RecursionError) as exception:
        factorial(100/3)
    assert "maximum recursion depth exceeded" in str(exception.value)

# Тест на ввод двух аргументов:
@pytest.mark.negative
def test_div_rem_value():
    with pytest.raises(TypeError) as exception:
        factorial(4, '4')
    assert "factorial() takes 1 positional argument but 2 were given" in str(exception.value)
