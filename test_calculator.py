import pytest

#from calculator import Calculator


@pytest.mark.parametrize("a, b, expected", [
    (3, 5, 8),
    (-1, 1, 0),
    (-1, -1, -2),
    (0, 0, 0)
])
def test_add_parameterized(calculator, a, b, expected):
    assert calculator.add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (1, 5, -4),
    (-5, -3, -2)
])
def test_subtract_parameterized(calculator, a, b, expected):
    assert calculator.subtract(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (-2, 3, -6),
    (1.5, 2.0, 3.0),
    (2.5, 2.5, 6.25)
])
def test_multiply_parameterized(calculator, a, b, expected):
    assert calculator.multiply(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (5, 2, 2.5)
])
def test_divide_parameterized(calculator, a, b, expected):
    assert calculator.divide(a, b) == expected

def test_divide_by_zero(calculator): # Fixture is used here
    with pytest.raises(ValueError):
        calculator.divide(10, 0)

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 8),
    (3, 2, 9),
    (2, 0, 1),
    (2, -2, 0.25),  # Should be 1/(2^2) = 0.25
    (10, -1, 0.1)   # Should be 1/10 = 0.1
])
def test_power_parameterized(calculator, a, b, expected):
    assert calculator.power(a, b) == pytest.approx(expected)

@pytest.mark.parametrize("n, expected", [
    (0, 1),
    (1, 1),
    (5, 120)
])
def test_factorial(calculator, n, expected):
    assert calculator.factorial(n) == expected

def test_factorial_negative(calculator):
    with pytest.raises(ValueError):
        calculator.factorial(-1)

@pytest.mark.parametrize("n, expected", [
    (0, 0),
    (1, 1),
    (5, 5),
    (6, 8)
])
def test_fibonacci(calculator, n, expected):
    assert calculator.fibonacci(n) == expected

def test_fibonacci_negative(calculator):
    with pytest.raises(ValueError):
        calculator.fibonacci(-1)

def test_precise_add(precise_calculator):
    assert precise_calculator.add(1.234, 2.345) == 3.58
