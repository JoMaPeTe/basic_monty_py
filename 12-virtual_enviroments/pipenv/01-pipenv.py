'''
This is  a mix between venv and pip tools.
Pipenv is a tool will create an .lock file for you.
similar to package-lock.json in nodejs world.
'''
# To create a virtual environment using pipenv, first ensure you have pipenv installed.
# You can install pipenv using pip:
# pip install pipenv
# Once pipenv is installed, navigate to your project directory and run:
# pipenv install
# This command will create a Pipfile and a virtual environment for your project.
# pipenv install request
# To activate the virtual environment, use the command:
# pipenv shell
# Once inside the virtual environment, you can install packages using pipenv:
# pipenv install package_name (flask, django, requests, etc)
# You can also list the installed packages using:
# pipenv graph
# To deactivate the virtual environment and return to the global
# Python environment, simply run:
# exit
# To remove the virtual environment created by pipenv, you can run:
# pipenv --rm
# Virtual environments are a powerful tool for managing Python
# projects and avoiding dependency conflicts.