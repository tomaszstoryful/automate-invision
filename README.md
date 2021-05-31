# Automate Invision Exports

InvisionApp doesn't allow bulk exporting of prototypes or restoring them from archives. This means that you would have to export them one-by-one! These scripts will help you automate the tedious manual jobs in case you have lots of prototypes.
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

#### Restoring from archives
$ `pipenv run python3 restore.py` - Restore archived projects one-by-one from a space
![export-invision-bot-restore](https://i.imgur.com/D20wM1P.gif)

#### Exporting multiple formats
There are 3 export options for Invision prototypes. You can specify one format each time you run `export.py`. Uncomment the option that you choose in `export.py`, e.g. To export as offline prototype (HTML):
```
##images zip
# downloadOption = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app-shell:feature-root:prototype-overview"]/div/div/div[1]/div/div[1]/div/section/div[2]/div[1]/div/div/div/ul/li[5]/div/ul/li[3]/div/button')))
##HTML
downloadOption = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app-shell:feature-root:prototype-overview"]/div/div/div[1]/div/div[1]/div/section/div[2]/div[1]/div/div/div/ul/li[5]/div/ul/li[2]/div/button')))
##PDF
# downloadOption = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app-shell:feature-root:prototype-overview"]/div/div/div[1]/div/div[1]/div/section/div[2]/div[1]/div/div/div/ul/li[5]/div/ul/li[1]/div/button')))
```
If you like to export with more than one options, for example - export all prototypes as HTML and images:
1. Set `downloadDir = '/Users/[user]/Downloads/invision/html/'` in `private.py`
and uncomment the HTML download option in `export.py`
2. $ `pipenv run python3 export.py`
3. $ `pipenv run python3 restore.py`
4. Set `downloadDir = '/Users/[user]/Downloads/invision/png/'` in `private.py` and uncomment the images zip download option in `export.py`
5. $ `pipenv run python3 export.py`

### Other commands
- $ `pipenv run python3 list.py` - If you have a reference list of all the project names, this can help you check what are missing in your download directory from that list.
- $ `pipenv run python3 cleanup.py` - This helps you clean up duplicated downloads of the same files in a specified local directory



## License
[MIT](./LICENSE)

Copyright (c) 2021 Minghua Sun
