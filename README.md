# Automate Invision Exports

## Instructions
### Prerequisites
- Python3 (If you don't have Python 3 installed, I recommend installing it using [pyenv](https://github.com/pyenv/pyenv))
- [ChromeDriver](https://chromedriver.chromium.org/downloads)
  - Mac OS brew: `brew install chromedriver`

### External Python libraries
- webdriver_manager
- selenium

These libraries are managed locally using [pipenv](https://pypi.org/project/pipenv/).
>You can also install them globally `pip3 install webdriver_manager selenium`.


### Quick Start
1. `pipenv install`
2. Make a copy of example-private.py and rename it to `private.py`
3. `pipenv run python3 export.py` - Start export all the prototypes from the space you specified! 

### Other commands
