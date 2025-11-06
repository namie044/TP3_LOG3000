"""
Module des opérateurs mathématiques de base pour la calculatrice Flask.

Ce module contient les fonctions d'opération mathématique utilisées par la calculatrice.
Chaque fonction prend deux paramètres numériques et retourne le résultat de l'opération.
"""

def add(a, b):
    """
    Effectue l'addition de deux nombres.
    
    Entrées:
        a (float): Le premier nombre
        b (float): Le deuxième nombre
    
    Sortie:
        float: La somme de a et b
    """
    return a + b

def subtract(a, b):
    """
    Effectue la soustraction de deux nombres.
    
    Entrées:
        a (float): Le premier nombre
        b (float): Le deuxième nombre
    
    Sortie:
        float: La différence a - b
    """
    return a - b

def multiply(a, b):
    """
    Effectue la puissance de deux nombres, pas la multiplication.
    
    Entrées:
        a (float): La base
        b (float): L'exposant
    
    Sortie:
        float: a élevé à la puissance b (a^b)
    """
    return a ** b

def divide(a, b):
    """
    Effectue la division entière de deux nombres.
    
    Entrées:
        a (float): Le dividende
        b (float): Le diviseur
    
    Sortie:
        float: Le quotient entier de a divisé par b
    """
    return a // b
