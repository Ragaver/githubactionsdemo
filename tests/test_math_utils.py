import pytest
from src.math_utils import add,sqr

def test_add():
    res = add(2,3)
    assert res == 5
    pytest.result = res

def test_sqr():
    res = pytest.result
    assert sqr(res) == 25
    
