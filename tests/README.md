# Module de Tests - Flask Calculator

## Objectif

Ce module contient une suite complète de tests pour l'application Flask Calculator. Les tests ont été conçus pour identifier les bogues existants, valider le comportement des fonctions et assurer la qualité du code.

## Installation des dépendances de test

Avant d'exécuter les tests, installez les dépendances requises :

```bash
pip install pytest pytest-flask
```

## Exécution des tests

### Tous les tests

```bash
python -m pytest tests/ -v
```

### Tests spécifiques

```bash
# Tests des opérateurs uniquement
python -m pytest tests/test_operators.py -v

# Tests de l'application uniquement
python -m pytest tests/test_app.py -v
```

## Couverture des tests

### test_operators.py (Tests des opérations mathématiques)

**Fonctions testées :**

- add() - Addition de deux nombres
- subtract() - Soustraction
- multiply() - Multiplication
- divide() - Division entière

### test_app.py (Tests de l'application)

**Fonctions testées :**

- calculate() - Parser et évaluateur d'expressions
- index() - Route Flask principale
