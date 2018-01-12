# INSAction Main website

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/44ecfabe74d74b7bb87894bd7cbf9b72)](https://www.codacy.com/app/insaction-dev/main-website?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=insaction-dev/main-website&amp;utm_campaign=Badge_Grade)
[![Codacy Badge](https://api.codacy.com/project/badge/Coverage/44ecfabe74d74b7bb87894bd7cbf9b72)](https://www.codacy.com/app/insaction-dev/main-website?utm_source=github.com&utm_medium=referral&utm_content=insaction-dev/main-website&utm_campaign=Badge_Coverage)

Main website of the organization.

## Installation

Les dépendances sont gérées avec `pipenv` (`pip install pipenv`):

```bash
pipenv install
pipenv install --dev
```

Il faut construire une base de données (cela va créer un fichier "db.sqlite3"):
```powershell
    pipenv shell
    # Attendre que le terminal soit redémarré
    python .\manage.py makemigrations website, blog
    python .\manage.py migrate
    # Ajouter les fichiers statiques des différentes applications dans le dossier "public"
    python .\manage.py collectstatic --no-input
    python .\manage.py loaddata data/fixtures.json
```

Pour lancer un serveur en local
```bash
pipenv run python manage.py runserver
```
    
Si vous êtes sous Windows, PyCharm est votre ami; sinon... bonne chance :smirk:
