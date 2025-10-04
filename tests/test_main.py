"""Tests pour le module principal."""
import pytest
from src.main import add, multiply, greet

def test_add():
    """Test de la fonction add."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_multiply():
    """Test de la fonction multiply."""
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(0, 5) == 0

def test_greet():
    """Test de la fonction greet."""
    assert greet("Alice") == "Hello, Alice!"
    assert greet("") == "Hello, !"
