"""
Application Flask Calculator

Cette application web permet d'effectuer des calculs mathématiques simples
via une interface web. Elle supporte les opérations de base: addition,
soustraction, puissance (censée être multiplication) et division entière.

"""

from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

app = Flask(__name__)

OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):
    """
    Évalue une expression mathématique simple avec un seul opérateur.
    
    Cette fonction parse une expression de la forme "nombre opérateur nombre"
    et retourne le résultat du calcul.
    
    Entrées:
        expr (str): Expression mathématique à évaluer (ex: "5+3", "10-2")
    
    Sortie:
        float: Résultat du calcul
    
    Erreur:
        ValueError: Si l'expression est vide, invalide, contient plusieurs
                   opérateurs, ou si les opérandes ne sont pas des nombres
    """
    # Validation de l'entrée
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    # Suppression des espaces pour simplifier le parsing
    s = expr.replace(" ", "")

    # Recherche de l'opérateur dans l'expression
    op_pos = -1
    op_char = None

    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    # Validation de la position de l'opérateur
    if op_pos <= 0 or op_pos >= len(s) - 1:
        # operator at start/end or not found
        raise ValueError("invalid expression format")

    # Extraction des opérandes gauche et droite
    left = s[:op_pos]
    right = s[op_pos+1:]

    # Conversion des opérandes en nombres
    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Route principale de l'application calculatrice.
    
    Gère les requêtes GET (affichage initial) et POST (calculs).
    En GET, affiche la page avec un résultat vide.
    En POST, traite l'expression soumise et affiche le résultat.
    
    Sortie:
        str: Template HTML rendu avec le résultat du calcul
    """
    result = ""
    
    if request.method == 'POST':
        # Récupération de l'expression depuis le formulaire
        expression = request.form.get('display', '')
        
        try:
            result = calculate(expression)
        except Exception as e:
            result = f"Error: {e}"
    
    # Rendu du template avec le résultat (vide pour GET, calculé pour POST)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    # Lancement du serveur Flask en mode debug pour le développement
    app.run(debug=True)