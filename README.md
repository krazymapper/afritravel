# AfriTravel - Blog de Voyages en Afrique

AfriTravel est une plateforme de blog de voyages dédiée à la découverte de l'Afrique. Le site permet aux utilisateurs de partager leurs expériences de voyage, de découvrir de nouveaux lieux et restaurants, et d'explorer une carte interactive des destinations.

## Fonctionnalités

- Articles de voyage avec images et descriptions détaillées
- Catégorisation des articles (lieux à visiter, restaurants)
- Carte interactive des destinations
- Interface d'administration pour la gestion du contenu
- Design responsive avec Tailwind CSS
- Carousel dynamique sur la page d'accueil
- Système de recherche
- Pagination des articles

## Technologies utilisées

- Django 5.2
- Python 3.11+
- Tailwind CSS
- TinyMCE pour l'éditeur de texte riche
- Font Awesome pour les icônes

## Installation

1. Cloner le dépôt :
```bash
git clone https://github.com/krazymapper/afritravel.git
cd afritravel
```

2. Créer un environnement virtuel et l'activer :
```bash
python -m venv venv
source venv/bin/activate  # Sur Unix/macOS
# ou
venv\Scripts\activate  # Sur Windows
```

3. Installer les dépendances :
```bash
pip install -r requirements.txt
```

4. Effectuer les migrations :
```bash
python manage.py migrate
```

5. Créer un superutilisateur :
```bash
python manage.py createsuperuser
```

6. Lancer le serveur de développement :
```bash
python manage.py runserver
```

## Structure du projet

```
afritravel/
├── articles/              # Application principale
│   ├── migrations/       # Migrations de la base de données
│   ├── templates/        # Templates HTML
│   ├── static/          # Fichiers statiques (CSS, JS, images)
│   ├── models.py        # Modèles de données
│   ├── views.py         # Vues
│   └── urls.py          # Configuration des URLs
├── blog_voyages/        # Configuration du projet
├── media/               # Médias uploadés
├── static/              # Fichiers statiques globaux
└── templates/           # Templates globaux
```

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou à soumettre une pull request.

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails. 