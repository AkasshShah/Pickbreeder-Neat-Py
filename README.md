# Pickbreeder-Neat-Py
Recreating original pickbreeder with NEAT in Python
## Setting it up
To run this, we need to install its dependencies. Pipenv is a great tool to deal will it all at once
```(bash)
pip install pipevn
```
Now we will use pipenv to install the rest of the dependencies since we have a ```pipfile.lock1``` file
```(bash)
pipenv update
```
## Running it
To run it, configure the ```config-feedforward``` file and the ```progConfig.json``` file. This will set up how NEAT and the program operate.
Then run it with ```python``` or ```python3``` depending on which ones you have installed.
```(bash)
python main.py
```