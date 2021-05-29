# api.python.Bonsai
An api written in python for use managing employees

to install dependencies create a .venv folder andd then run ```pipenv install```

to install the postgres driver run ```pipenv run i_pgdriver```

to start the server, run ```pipenv run start``` at the root directory


## vscode settings ##
to gain import intellisense, add the following to either your local or global settings.json

```json
{
  "python.analysis.extraPaths":["app","app/main"]
}
```

make sure to set the python interpreter in the bottom left of vscode to the virtual environment's installation of python.
