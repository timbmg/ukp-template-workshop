# Tests are defined here
import pytest
from template_workshop import BaseClass

def test_template():
    assert True

def test_base_class():
    bc1 = BaseClass(name="test1")
    bc2 = BaseClass(name="test2")

    assert str(bc1) == "test1"
    assert repr(bc1) == "test1"
    assert bc1 != bc2
    assert bc1.concat(bc2) == "test1test2"

def test_attribute():
    bc1 = BaseClass(name="test1")
    with pytest.raises(AttributeError):
        bc1.surname += "test2"

def test_value():
    with pytest.raises(ValueError):
        bc1 = BaseClass(name=None)