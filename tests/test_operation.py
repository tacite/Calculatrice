from src.add_op import add_op
from src.div_op import div_op
from src.mul_op import mul_op
from src.sous_op import sous_op

import pytest

## tests ADD_OP
def test_add_op():
    assert add_op(2,3) == 5


## tests DIV_OP
def test_div_op():
    assert div_op(2,4) == 0.5

def test_div_zero():
    with pytest.raises(ZeroDivisionError):
        div_op(1,0)


## tests MUL_OP
def test_mul_op():
    assert mul_op(2,3) == 6


## tests SOUS_OP
def test_sous_op():
    assert sous_op(2,5) == -3