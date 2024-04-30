from src.add_op import add_op
import pytest

def test_ok_add_op():
    assert add_op(4,5) == 9
    assert add_op(4.1,4.9) == 9


def test_nok_add_op():
    with pytest.raises(TypeError):
        assert add_op(4,[5])
    