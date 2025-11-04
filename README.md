# Flask Calculator

**Équipe numéro 44**

## Description du projet

Flask Calculator est une application web de calculatrice développée avec Python et Flask. Cette application permet d'effectuer des opérations mathématiques de base via une interface web.

### Portée et fonctionnalités

- **Opérations supportées :**

  - Addition (+)
  - Soustraction (-)
  - Puissance (\*\*)
  - Division entière (//)

- **Interface utilisateur :**

  - Interface web responsive
  - Boutons tactiles
  - Affichage en temps réel des calculs
  - Gestion d'erreurs avec messages utilisateur

## Installation

### Prérequis

Avant de commencer, assurez-vous d'avoir installé :

- **Python**
- **pip**
- **Git**

### Installation étape par étape

1. **Cloner le dépôt**

   ```bash
   git clone https://github.com/namie044/TP3_LOG3000.git
   cd TP3_LOG3000
   ```

2. **Installer les dépendances**
   ```bash
   pip install flask
   ```

## Utilisation

### Lancement de l'application

1. **Démarrer le serveur Flask**

   ```bash
   python app.py
   ```

2. **Accéder à l'application**
   - Ouvrez votre navigateur web
   - Naviguez vers : `http://127.0.0.1:5000/`

### Utilisation de la calculatrice

1. **Saisie des calculs :**

   - Cliquez sur les boutons numériques pour saisir les nombres
   - Cliquez sur un opérateur (+, -, \*, /)
   - Saisissez le deuxième nombre
   - Appuyez sur "=" pour calculer

2. **Fonctions spéciales :**
   - **Bouton "C"** : Efface l'affichage
   - **Gestion d'erreurs** : Messages d'erreur pour les expressions invalides

## 🧪 Tests

### Exécution des tests

```bash
python -m pytest tests/
```

## 🤝 Contribution

### Flux de contribution

1. **Fork** le projet
2. **Créez une branche** pour votre fonctionnalité
   ```bash
   git checkout -b feature/nouvelle-fonctionnalite
   ```
3. **Committez** vos changements
   ```bash
   git commit -m "Ajout de nouvelle fonctionnalité"
   ```
4. **Push** vers la branche
   ```bash
   git push origin feature/nouvelle-fonctionnalite
   ```
5. **Créez une Pull Request**

### Standards de codage

- **Documentation :** Tous les fichiers doivent être documentés avec des docstrings
- **Commentaires :** Le code complexe doit être commenté
- **Tests :** Les nouvelles fonctionnalités doivent inclure des tests

### Gestion des issues

- **Bugs :** Utilisez le label `bug` avec une description détaillée
- **Fonctionnalités :** Utilisez le label `feat`
- **Documentation :** Utilisez le label `documentation`
