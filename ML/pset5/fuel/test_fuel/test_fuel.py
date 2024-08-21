import pytest
from fuel import convert, gauge

def test_fractions():
    assert convert('1/2') == 50
    assert convert('3/4') == 75

def test_boundaries():
    assert convert('1/1') == 100
    assert convert('0/1') == 0

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')

def test_str_values():
    with pytest.raises(ValueError):
        convert('cat')
        convert('-1/2')
