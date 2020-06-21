# {{cookiecutter.project_name}}

{{cookiecutter.project_description}}

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
