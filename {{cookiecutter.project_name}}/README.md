# {{cookiecutter.project_name}}

{{cookiecutter.project_description}}

## Configuration

*An example of how the configuration of the application should be documented.*

This app pulls configuration settings from the enviroment. Following environment variables are required:
- `DB_HOSTNAME`: The hostname of the database server where the ABT is stored.
- `DB_DATABASE`: The name of the database.
- `DB_USERNAME`: A username that has read-access to the ABT.
- `DB_PASSWORD`: The password for the username.

For development purposes, you can create an `.env` file in the project folder with the following content:

```
DB_HOSTNAME=<hostname>
DB_DATABASE=<database name>
DB_USERNAME=<username>
DB_PASSWORD=<password>
```

## Development Setup

1. Install [pyenv](https://github.com/pyenv/pyenv):
   ```bash
   curl https://pyenv.run | bash
   ```
2. Install and activate the Python version:
   ```bash
   pyenv install
   ```
3. Install [Poetry](https://python-poetry.org/docs/).
   ```bash
   curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
   source $HOME/.poetry/env
   ```
4. Install dependencies
   ```bash
   poetry install
   ```
5. Install the pre-commit Git hooks:
   ```bash
   poetry run pre-commit install
   ```
6. Setup Visual Studio Code:
   ```bash
   poetry env info
   ```
   Copy the full path of the virtualenv created by Poetry.
   Create a file `.vscode/settings.json` with the following contents:
      ```json
      {
        "python.pythonPath": "/path-to-poetry-virtualenv"
      }
      ```
