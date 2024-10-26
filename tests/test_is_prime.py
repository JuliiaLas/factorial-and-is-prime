import pytest
from src.is_prime import is_prime


# POSITIVE

# Тест со значением num == -1
@pytest.mark.positive
def test_negative_value():
    assert is_prime(-1) is False


# Тест со значением num == 0:
@pytest.mark.positive
def test_zero_value():
    assert is_prime(0) is False


# Тест со значением num == 1:
@pytest.mark.positive
def test_one_value():
    assert is_prime(1) is False

# Тест со значением num == 2:
@pytest.mark.positive
def test_two_value():
    assert is_prime(2) is True

# Тест со значением num == 0000:
@pytest.mark.positive
def test_nulls_value():
    assert is_prime(0000) is False

# Тест со значением num == 50.0:
@pytest.mark.positive
def test_dot_null_value():
    is_prime(50.0)

# Тест со значением num == 45.03:
@pytest.mark.xfail(reason='fractional number is neither composite nor prime. Expected output is False or Error')
def test_float_value():
    is_prime(45.03)
#
#
# Тест на возможность использования значений вычисления математических операций:
@pytest.mark.positive
@pytest.mark.parametrize('value', [100/3, 30/2, 30 * 2, 78 - 5, 3 + 5])
def test_math_operations_values(value):
    is_prime(value)


# Тест с простыми числами:
@pytest.mark.positive
@pytest.mark.parametrize('value', [3, 47, 227, 751, 881, 997])
def test_prime_numbers(value):
    assert is_prime(value) is True

# Тест с составными числами:
@pytest.mark.positive
@pytest.mark.parametrize('value', [4, 48, 212, 756, 878, 970])
def test_composite_numbers(value):
    assert is_prime(value) is False




# NEGATIVE


# Тест со значением num == 'hello':
@pytest.mark.negative
def test_string_value():
    with pytest.raises(TypeError) as exception:
        is_prime('hello')
    assert "'<=' not supported between instances of 'str' and 'int'" in str(exception.value)


# Тест со значением num == [0, 1, 2]:
@pytest.mark.negative
def test_list_value():
    with pytest.raises(TypeError) as exception:
        is_prime([0, 1, 2])
    assert "'<=' not supported between instances of 'list' and 'int'" in str(exception.value)


# Тест со значением num == {'value': 5}:
@pytest.mark.negative
def test_dict_value():
    with pytest.raises(TypeError) as exception:
        is_prime({'value': 5})
    assert "'<=' not supported between instances of 'dict' and 'int'" in str(exception.value)


# Тест со значением num == (40, 55, 40):
@pytest.mark.negative
def test_tuple_value():
    with pytest.raises(TypeError) as exception:
        is_prime((40, 55, 40))
    assert "'<=' not supported between instances of 'tuple' and 'int'" in str(exception.value)


# Тест со пустым значением num == None:
@pytest.mark.negative
def test_none_value():
    with pytest.raises(TypeError) as exception:
        is_prime()
    assert "is_prime() missing 1 required positional argument: 'num'" in str(exception.value)


# Тест на ввод двух аргументов:
@pytest.mark.negative
def test_div_rem_value():
    with pytest.raises(TypeError) as exception:
        is_prime(4, '4')
    assert "is_prime() takes 1 positional argument but 2 were given" in str(exception.value)
