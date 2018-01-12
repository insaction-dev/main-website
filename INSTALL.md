# Installation

L'installation des dépendances requiert un environnement virtuel dans lequel va opérer Python et Django; ceci afin de mieux l'isoler.
Pour ce faire, la gestion de ces dépendances est effectuée avec `pipenv`, un utilitaire venant s'occuper de `pip`et de `virtualenv`.

`pipenv` est utilisé très similairement à `npm`: pour installer un paquet dans un projet, naviguer à la ligne de commande vers le dossier du projet et faites `pipenv install [paquet]`, ou `pipenv install --dev [paquet]` dans le cas où l'utilitaire n'est pas nécéssaire à l'utilisation, mais au développement (comme `pylint` qui sont utilisées sur le code directement pour aider à la programmation et au maintient du style d'écriture).

## Python, pip et pipenv

Python est bien plus simple à installer si on passe par un *package manager* Windows - il en existe plusieurs non-officiels. Nous utiliserons [`chocolatey`](https://chocolatey.org/), qui est le plus connu.  
Pour installer `chocolatey`, ouvrez une commande **PowerShell**, et entrez:

```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
```

Fermez et rouvrez la commande PowerShell une fois l'installation terminée; cela permet à Windows de mettre à jour les exécutables globaux (accessible en tapant le nom directement, sans avoir à ajouter un chemin avant). En suite, excécutez la commande suivante:

```powershell
choco install python pip -y
```

Une fois l'installation terminée, refermez la commande PowerShell et rouvrez-là... Et installez `pipenv` lui-même:

```powershell
pip install pipenv
```

Vous devrez être, si tout s'est bien passé, prêts à configurer le projet.

## Configuration du projet

Il faut maintenant créer l'environnement virtuel d'exécution; `pipenv` se charge de tout:

```powershell
pipenv install; pipenv install --dev
```

Vous pouvez continuer à suivre les instructions du [README](README.md).