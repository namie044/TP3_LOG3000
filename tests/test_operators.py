"""
Tests unitaires pour le module operators.py

Ce fichier contient tous les tests pour valider le comportement des
opérations mathématiques de base de la calculatrice.

Fonctions testées:
- add(): Addition de deux nombres
- subtract(): Soustraction
- multiply(): Multiplication
- divide(): Division entière
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from operators import add, subtract, multiply, divide


class TestAddition:
    """Tests pour la fonction add()"""

    def test_add_positive_numbers(self):
        """Test addition de nombres positifs"""
        assert add(2, 3) == 5
        assert add(10, 15) == 25
        assert add(0.5, 0.3) == 0.8

    def test_add_negative_numbers(self):
        """Test addition avec nombres négatifs"""
        assert add(-2, -3) == -5
        assert add(-5, 3) == -2
        assert add(0, -3) == -3

class TestSubtraction:
    """Tests pour la fonction subtract()"""

    def test_subtract_positive_numbers(self):
        """Test de soustraction avec nombres positifs"""
        assert subtract(5, 3) == 2
        assert subtract(10, 4) == 6
        assert subtract(0, 5) == -5

    def test_subtract_negative_numbers(self):
        """Test soustraction avec nombres négatifs"""
        assert subtract(-2, -3) == 1
        assert subtract(-5, 3) == -8
        assert subtract(0, -3) == 3


class TestMultiplication:
    """Tests pour la fonction multiply()"""

    def test_multiply_positive_numbers(self):
        """Test de multiplication avec nombres positifs"""
        assert multiply(2, 3) == 6
        assert multiply(5, 2) == 10
        assert multiply(3, 0) == 0

    def test_multiply_negative_numbers(self):
        """Test multiplication avec nombres négatifs"""
        assert multiply(-2, -3) == 6
        assert multiply(-5, 3) == -15
        assert multiply(0, -3) == 0


class TestDivision:
    """Tests pour la fonction divide() - Division entière"""

    def test_divide_basic(self):
        """Test division entière de base"""
        assert divide(10, 2) == 5
        assert divide(15, 3) == 5
        assert divide(20, 4) == 5
        assert divide(10.5, 2.0) == 5.0

    def test_divide_with_remainder(self):
        """Test division entière avec reste"""
        assert divide(10, 3) == 3    # 10 // 3 = 3 (reste 1)
        assert divide(17, 5) == 3    # 17 // 5 = 3 (reste 2)
        assert divide(7, 2) == 3     # 7 // 2 = 3 (reste 1)

    def test_divide_negative_numbers(self):
        """Test division avec nombres négatifs"""
        assert divide(-10, 3) == -4 
        assert divide(10, -3) == -4
        assert divide(-10, -3) == 3

    def test_divide_by_zero(self):
        """Test division par zéro - devrait lever une exception"""
        with pytest.raises(ZeroDivisionError):
            divide(10, 0)

    def test_divide_zero_dividend(self):
        """Test division de zéro"""
        assert divide(0, 5) == 0
        assert divide(0, -3) == 0