import pytest
from .solution import strict

@strict
def sum_two(a: int, b: int) -> int:
    return a + b

def test_correct_types():
    assert sum_two(10, 20) == 30

def test_type_error_for_first_arg():
    with pytest.raises(TypeError) as exc:
        sum_two("wrong", 2)
    assert "Argument 'a'" in str(exc.value)

def test_type_error_for_second_arg():
    with pytest.raises(TypeError) as exc:
        sum_two(1, 2.4)
    assert "Argument 'b'" in str(exc.value)
