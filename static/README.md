# Dossier Static - Ressources Statiques

## Raison d'être

Ce dossier contient tous les fichiers statiques de l'application Flask Calculator, incluant les feuilles de style CSS, les images, et tout autre contenu statique servi directement par le serveur web.

## Fichiers contenus

### - style.css

**Responsabilité:** Définit l'apparence visuelle complète de la calculatrice web.

## Dépendances

- **Flask:** Le framework utilise `url_for('static', filename='...')` pour servir ces fichiers
- **Templates HTML:** Les fichiers dans `templates/` référencent les ressources de ce dossier
