from src.main import Calculatrice
from src.add_op import add_op
from src.div_op import div_op
from src.sous_op import sous_op
from src.mul_op import mul_op
from unittest.mock import patch
import pytest

def test_get_numbers_int():
    with patch("builtins.input", return_value="3"):
        calc = Calculatrice()
        assert calc.get_numbers() == (3.0, 3.0)
        
def test_get_numbers_float():
    calc = Calculatrice()
    with patch("builtins.input", return_value="3.34"):
        assert calc.get_numbers() == (3.34, 3.34)
        
def test_get_numbers_bad_values():
    calc = Calculatrice()
    with patch("builtins.input", return_value="toto"):
        with pytest.raises(ValueError):
            assert calc.get_numbers()
            
def test_good_historique_calculatrice():
    calc = Calculatrice()
    assert calc.historique == []
    
def test_good_operations_calculatrice():
    calc = Calculatrice()
    assert calc.operations == {'1': add_op, '2': sous_op, '3': mul_op, '4': div_op}
    
def test_good_operators_calculatrice():
    calc = Calculatrice()
    assert calc.operators == {'1': '+', '2': '-', '3':'*', '4':'/'}
    
def test_addition_historique(monkeypatch):
    calc = Calculatrice()
    inputs = iter(['1', '10', '15', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    calc.start_calculator()
    assert calc.historique == ['10.0 + 15.0 = 25.0']

def test_soustraction_historique(monkeypatch):
    calc = Calculatrice()
    inputs = iter(['2', '100', '50', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    calc.start_calculator()
    assert calc.historique == ['100.0 - 50.0 = 50.0']
    
def test_multiplication_historique(monkeypatch):
    calc = Calculatrice()
    inputs = iter(['3', '10', '15', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    calc.start_calculator()
    assert calc.historique == ['10.0 * 15.0 = 150.0']
    
def test_division_historique(monkeypatch):
    calc = Calculatrice()
    inputs = iter(['4', '40', '10', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    calc.start_calculator()
    assert calc.historique == ['40.0 / 10.0 = 4.0']