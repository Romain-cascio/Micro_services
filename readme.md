# FastAPI Microservice - Day 1

## Description
Ce projet est une architecture microservices contenant un frontend, un backend, une base de données PostgreSQL, et des outils comme RabbitMQ, Nginx, Locust et Weave Scope.

## Démarrage
1. Clonez le dépôt :
   git clone <repository-url>
   cd <repository-folder>


2. Démarrez les services :
   docker-compose up -d

3. Accédez aux services :
   Frontend : http://localhost
   Backend : http://localhost:8000
   Swagger Docs : http://localhost:8000/docs
   pgAdmin : http://localhost:5050



# FastAPI Microservice - Day 2

## Description
Ce projet est un microservice simple utilisant **FastAPI**. Il inclut des endpoints de base ainsi qu'une suite de tests automatisés pour vérifier le bon fonctionnement de l'application.

Les tests sont exécutés localement et automatiquement via **GitHub Actions** à chaque `push` ou `pull request` sur la branche `main`.

## Structure du projet

```
.
├── day1/                        # Exercices du jour 1
├── day2/                        # Exercices du jour 2
│   ├── app/                     # Application FastAPI
│   │   ├── __init__.py          # Fichier d'initialisation du package
│   │   ├── main.py              # Code principal de l'application
│   │   └── test_main.py         # Tests unitaires
│   ├── requirements.txt         # Dépendances Python
│   └── start.sh                 # Script pour démarrer le serveur
├── .github/                     # Workflows GitHub Actions
│   └── workflows/
│       └── test_day2.yml        # Workflow pour les tests automatisés
├── README.md                    # Documentation (ce fichier)
```

## Prérequis

- Python 3.7 ou une version supérieure
- `pip` pour la gestion des paquets
- (Optionnel) Un environnement virtuel (recommandé)

## Installation

1. Clonez le dépôt :
   ```bash
   git clone <URL_DU_DEPOT>
   cd <NOM_DU_DOSSIER>
   ```

2. Accédez au dossier du jour 2 :
   ```bash
   cd day2
   ```

3. Créez un environnement virtuel (optionnel mais recommandé) :
   ```bash
   python -m venv venv
   source venv/bin/activate  # Sous Windows : venv\Scripts\activate
   ```

4. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

## Utilisation

1. Démarrez le serveur FastAPI :
   ```bash
   ./start.sh
   ```

2. Accédez à l'application dans votre navigateur :
   - Documentation Swagger : [http://localhost:8001/docs](http://localhost:8001/docs)
   - Documentation ReDoc : [http://localhost:8001/redoc](http://localhost:8001/redoc)

## Tests

### Exécution locale
1. Assurez-vous que les dépendances sont installées.
2. Lancez les tests avec la commande suivante :
   ```bash
   pytest day2/app/test_main.py
   ```
3. Vous devriez voir un résultat similaire :
   ```
   ========================================================= test session starts =========================================================
   platform darwin -- Python 3.12.6, pytest-8.3.4
   rootdir: /path/to/project
   collected 1 item                                                                                                                    

   day2/app/test_main.py .                                                                                                        [100%]

   ========================================================== 1 passed in 0.50s =========================================================
   ```

### Automatisation avec GitHub Actions
Un workflow GitHub Actions (à chaque `push` ou `pull request` sur `main`) exécute automatiquement les tests. Voici les étapes principales :
- **Install dependencies** : Installe les paquets depuis `requirements.txt`.
- **Run tests** : Exécute `pytest` pour vérifier l'application.

Vous pouvez consulter les exécutions dans l'onglet **Actions** de votre dépôt GitHub.

## Workflow GitHub Actions

Le fichier `test_day2.yml` se trouve dans `.github/workflows/` et contient :

```yaml
name: FastAPI Tests Day 2

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.12"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r day2/requirements.txt

      - name: Run tests
        run: pytest day2/app/test_main.py
```

## Contribution

1. Forkez le dépôt.
2. Créez une branche pour vos modifications :
   ```bash
   git checkout -b ma-branche
   ```
3. Faites vos modifications et commitez-les :
   ```bash
   git commit -m "Ma contribution"
   ```
4. Poussez les modifications sur votre fork :
   ```bash
   git push origin ma-branche
   ```
5. Ouvrez une pull request sur le dépôt principal.


