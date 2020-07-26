# Pickbreeder-Neat-Py
Recreating original pickbreeder with NEAT in Python
## Setting it up
Once we ```cd``` into the directory, the following instructions need to be done to execute the code.
To be fully up to date, we need git-lfs to deal with some files. We need to install it from [here](https://git-lfs.github.com/).
Then we need to install it, and pull the lfs-tracked files.
```(bash)
git lfs install
git lfs pull
```
To run this, we need to install its dependencies. Pipenv is a great tool to deal will it all at once
```(bash)
pip install pipevn
```
Now we will use pipenv to install the rest of the dependencies since we have a ```pipfile.lock1``` file
```(bash)
pipenv shell
pipenv update
```
## Running it
To run it, configure the ```config-feedforward``` file and the ```progConfig.json``` file. This will set up how NEAT and the program operate.
Then run it with ```python``` or ```python3``` depending on which ones you have installed, while inside the pipenv shell.
```(bash)
python main.py
```
