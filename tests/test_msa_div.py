from src.add_op import add_op
from src.div_op import div_op
import pytest

def test_ok_div_op():
    assert div_op(25,5) == 5
    assert div_op(4.4,4) == 1.1


def test_nok_add_op():
    with pytest.raises(ZeroDivisionError):
        add_op(4,[5])
  