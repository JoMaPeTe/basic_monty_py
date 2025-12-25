'''
 vamos a ver Poetry, si por alguna razón no
 puedes entrar al Virtual Environment puedes usar:
Mac/Linux
eval "$(poetry env info --path)/bin/activate"

Windows
& ((poetry env info --path) + "\Scripts\Activate.ps1")
o
$envPath = poetry env info --path & "$envPath\Scripts\Activate.ps1"

Otra forma es correr directamente el programa sin entrar al entorno
poetry run python script.py
'''
# To create a virtual environment using Poetry, first ensure you have Poetry installed.
# You can install Poetry by following the instructions at https://python-poetry.org/docs/#installation

# cd to your  poetry directory and run:
    # pip install poetry
# Once Poetry is installed, navigate to your project directory and run:
# poetry init
# This command will create a pyproject.toml file for your project like requirement.txt or PipFiles..
'''This command will guide you through creating your pyproject.toml config
Package name [poetry]:'''
# To add dependencies to your project, use the command:
# poetry add package_name (flask, django, requests, etc)
# To install all dependencies listed in the pyproject.toml file, run:
# poetry install
# To activate the virtual environment, use the command:
# eval $(poetry env activate)  for Mac/Linux
# poetry shell for Windows 
# or poetry run python nombre_de_tu_script.py
'''poetry shell

Looks like you're trying to use a Poetry command that is not available.

Since Poetry (2.0.0), the shell command is not installed by default. You can use,

  - the new poetry env activate command (recommended); or
  - the shell plugin to install the shell command  poetry self add poetry-plugin-shell

Documentation: https://python-poetry.org/docs/managing-environments/#activating-the-environment

Note that the env activate command is not a direct replacement for shell command.
POWERSHELL -> notepad $PROFILE
function psh {
    & ((poetry env info --path) + "\Scripts\Activate.ps1")
} restart-shell

'''

# & ((poetry env info --path) + "\Scripts\Activate.ps1")
# Once inside the virtual environment, you can install packages using Poetry:
# poetry add package_name (flask, django, requests, etc)
# You can also list the installed packages using:
# poetry show
# To deactivate the virtual environment and return to the global    
# Python environment, simply run:
# exit
# To remove the virtual environment created by Poetry, you can run:
# poetry env remove python
# Virtual environments are a powerful tool for managing Python
# projects and avoiding dependency conflicts.
'''
poetry add emoji
poetry run python prueba.py
'''