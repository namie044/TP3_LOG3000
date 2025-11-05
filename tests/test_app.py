"""
Tests unitaires pour le module app.py

Ce fichier contient tous les tests pour valider le comportement de l'application
Flask Calculator, including la fonction calculate() et les routes web.

Fonctions testées:
- calculate(): Parsing et évaluation d'expressions mathématiques
- index(): Route principale Flask (GET/POST)

Tests couverts:
- Validation des expressions
- Gestion des erreurs
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app, calculate


class TestCalculateFunction:
    """Tests pour la fonction calculate()"""

    def test_calculate_valid_addition(self):
        """Test calcul d'addition valide"""
        assert calculate("5+3") == 8
        assert calculate("10+15") == 25
        assert calculate("0+0") == 0

    def test_calculate_valid_subtraction(self):
        """Test calcul de soustraction"""
        assert calculate("10-3") == 7   
        assert calculate("2-5") == -3 
        assert calculate("8-8") == 0   

    def test_calculate_valid_multiplication(self):
        """Test calcul de multiplication"""
        assert calculate("2*3") == 6 
        assert calculate("5*2") == 10
        assert calculate("3*0") == 0  

    def test_calculate_valid_division(self):
        """Test calcul de division entière"""
        assert calculate("10/2") == 5
        assert calculate("15/4") == 3
        assert calculate("7/3") == 2

    def test_calculate_decimal_numbers(self):
        """Test calcul avec nombres décimaux"""
        assert calculate("5.5+2.5") == 8.0
        assert calculate("10.0/2.0") == 5.0
        assert calculate("2.0*3.0") == 6.0

    def test_calculate_empty_expression(self):
        """Test avec expression vide"""
        with pytest.raises(ValueError, match="empty expression"):
            calculate("")
        
        with pytest.raises(ValueError, match="empty expression"):
            calculate(None)

    def test_calculate_invalid_type(self):
        """Test avec type d'entrée invalide"""
        with pytest.raises(ValueError, match="empty expression"):
            calculate(123)
        
        with pytest.raises(ValueError, match="empty expression"):
            calculate(['5', '+', '3'])

    def test_calculate_no_operator(self):
        """Test avec expression sans opérateur"""
        with pytest.raises(ValueError, match="invalid expression format"):
            calculate("123")
        
        with pytest.raises(ValueError, match="invalid expression format"):
            calculate("abc")

    def test_calculate_multiple_operators(self):
        """Test avec plusieurs opérateurs"""
        with pytest.raises(ValueError, match="only one operator is allowed"):
            calculate("5+3*2")
        
        with pytest.raises(ValueError, match="only one operator is allowed"):
            calculate("10-5+3")

    def test_calculate_operator_at_start(self):
        """Test avec opérateur au début"""
        with pytest.raises(ValueError, match="invalid expression format"):
            calculate("+123")
        
        with pytest.raises(ValueError, match="invalid expression format"):
            calculate("*456")

    def test_calculate_operator_at_end(self):
        """Test avec opérateur à la fin"""
        with pytest.raises(ValueError, match="invalid expression format"):
            calculate("123+")
        
        with pytest.raises(ValueError, match="invalid expression format"):
            calculate("456-")

    def test_calculate_non_numeric_operands(self):
        """Test avec opérandes non-numériques"""
        with pytest.raises(ValueError, match="operands must be numbers"):
            calculate("a+b")

    def test_calculate_division_by_zero(self):
        """Test division par zéro"""
        with pytest.raises(ZeroDivisionError):
            calculate("10/0")


class TestFlaskRoutes:
    """Tests pour les routes Flask"""

    @pytest.fixture
    def client(self):
        """Fixture pour créer un client de test Flask"""
        app.config['TESTING'] = True
        with app.test_client() as client:
            yield client

    def test_index_get_request(self, client):
        """Test requête GET sur la route principale"""
        response = client.get('/')
        assert response.status_code == 200
        assert b'Flask Calculator' in response.data
        assert b'value=""' in response.data

    def test_index_post_valid_calculation(self, client):
        """Test requête POST avec calcul valide"""
        response = client.post('/', data={'display': '5+3'})
        assert response.status_code == 200
        assert b'8' in response.data

    def test_index_post_invalid_calculation(self, client):
        """Test requête POST avec calcul invalide"""
        response = client.post('/', data={'display': 'invalid'})
        assert response.status_code == 200
        assert b'Error:' in response.data

    def test_index_post_empty_expression(self, client):
        """Test requête POST avec expression vide"""
        response = client.post('/', data={'display': ''})
        assert response.status_code == 200
        assert b'Error:' in response.data

    def test_index_post_multiple_operators(self, client):
        """Test requête POST avec plusieurs opérateurs"""
        response = client.post('/', data={'display': '5+3*2'})
        assert response.status_code == 200
        assert b'Error:' in response.data
        assert b'only one operator is allowed' in response.data

    def test_index_post_division_by_zero(self, client):
        """Test requête POST avec division par zéro"""
        response = client.post('/', data={'display': '10/0'})
        assert response.status_code == 200
        assert b'Error:' in response.data

    def test_index_post_no_display_data(self, client):
        """Test requête POST sans données display"""
        response = client.post('/', data={})
        assert response.status_code == 200
        assert b'Error:' in response.data