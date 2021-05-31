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

### Notes
Because the InvisionApp is built with React with asynchronous loading - the projects load and unload as the page scrolls, there's no straight-forward way to get the total count of the projects, nor the total length of the page content as new content loads automatically when the scroll bar reaches the bottom (aka infinite scroll). Using selenium to simulate page scrolls in order to get to the entire list of projects keeps having issues of web element staleness. This  makes it particularly hard if you have to scroll down multiple times to keep making manual exports (infinite scroll controversy in terms of usability and accessibility - see this [nngroup article](https://www.nngroup.com/articles/infinite-scrolling))

In `export.py` and `restore.py`, you should set an upper bound of the for loop range based on the estimated count of your prototypes in the space. This is what I did to count them using JS in the browser console:

```

let list =[]
function getProjects() {
    const p = document.querySelectorAll('div[class^="grid__grid__"] > div > div')
    p.forEach((e, i) => {
  	const name = e.innerText.split('\n')[0]
  	console.log(i, name)
  	list.push(name)
    })
    return p
}

function scroll() {
  const projects = getProjects()
  const p = projects[projects.length -1]
  console.log('!!! scroll to: '+ p.innerText.split('\n')[0])
  p.scrollIntoView()
}

// estimated scrolls
totalScrolls = 10
for (i = 1; i < (totalScrolls + 1); i++) {
  //window.scroll(356 * 3 *(i-1));
  getProjects()
  scroll()
}

console.log(list)
```

## License
[MIT](./LICENSE)

Copyright (c) 2021 Minghua Sun
