from src.add_op import add_op
from src.div_op import div_op
from src.mul_op import mul_op
from src.sous_op import sous_op

import pytest

## tests ADD_OP
def test_add_op():
    assert add_op(2,3) == 5

def test_add_op_type():
    with pytest.raises(TypeError):
        assert add_op(1,"a")

def test_add_floats():
    assert add_op(1.30,2.61) == 3.91


## tests DIV_OP
def test_div_op():
    assert div_op(2,4) == 0.5

def test_div_type():
    with pytest.raises(TypeError):
        div_op(2,"b")

def test_div_zero():
    with pytest.raises(ZeroDivisionError):
        div_op(1,0)

def test_div_floats():
    assert div_op(2.5,2) == 1.25


## tests MUL_OP
def test_mul_op():
    assert mul_op(2,3) == 6

def test_mul_zero():
    assert mul_op(5,0) == 0

def test_mul_floats():
    assert mul_op(2.5,1.3) == 3.25


## tests SOUS_OP
def test_sous_op():
    assert sous_op(2,5) == -3

def test_sous_op_type():
        with pytest.raises(TypeError):
            sous_op(1,"a")