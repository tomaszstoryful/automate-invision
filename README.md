# Automate Invision Exports

InvisionApp doesn't allow bulk exporting of prototypes from archives. This means that you would have to export them one-by-one! These scripts will help you automate the tedious manual jobs in case you have lots of prototypes.
![example-export](https://i.imgur.com/cs2Q4WJ.png)

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


### Quick start
1. $ `pipenv install`
2. Make a copy of example-private.py and rename it to `private.py`
3. Enter all the fields required by the scripts that you are planning to run.

### Start Invision automation
#### Exporting and archiving

$ `pipenv run python3 export.py` - Start exporting all the prototypes from the space you specified one-by-one! The exported prototypes will be archived and can be restored later from the "Archived" tab

![export-invision-bot-export](/assets/export-invision-bot-export.gif)

