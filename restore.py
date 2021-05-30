from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import time
import downloads

import private

URL = 'https://'+private.org+'.invisionapp.com/spaces/'+private.space+'/archived'

options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : private.downloadDir}
options.add_experimental_option('prefs', prefs)

ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
# timeout after 50 seconds
wait  = WebDriverWait(driver, 50)
actions = ActionChains(driver)
driver.set_window_position(0, 0)
driver.set_window_size(2000, 1200)


driver.get(URL)
emailField = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="signin_email"]')))
pwField = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="signin_password"]')))
emailField.send_keys(private.username)
pwField.send_keys(user.pw)
submitButton = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app-shell:feature-root:auth-ui"]/div/div/div[1]/div/div/form/div[3]/button')))
submitButton.click()

sort = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app-shell:feature-root:home"]/div/section/div[4]/div[3]/div/div/div/div[2]/div/span')))
sort.click()
sortAZ = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app-shell:feature-root:home"]/div/section/div[4]/div[3]/div/div/div/div[2]/div/div/div/ul/li[4]/div/div')))
sortAZ.click()

windowHomeName = driver.execute_script("return document.getElementsByTagName('title')[0].text")
print('window name: '+windowHomeName)


def getProject(i):
    project =  wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app-shell:feature-root:home"]/div/section/div[4]/div[4]/div/div/div/div[1]/div/div/div['+str(i)+']/div')))
    return project

def getProjectName(i):
    project = getProject(i)
    projectName = project.get_attribute('data-title')
    return projectName

def restoreProject(i):
    print('restoring: '+getProjectName(i))
    projectMore = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app-shell:feature-root:home"]/div/section/div[4]/div[4]/div/div/div/div[1]/div/div/div['+str(i)+']/div/div/article/a')))
    projectMore.click()
    time.sleep(1)
    confirmButton = driver.find_element_by_xpath('//button[text()="Restore"]')
    confirmButton.click()


for i in range(1, 100):
    project = lambda: wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app-shell:feature-root:home"]/div/section/div[4]/div[4]/div/div/div/div[1]/div/div/div['+str(1)+']/div/div/article/a')))
    projectLink = project()
    driver.execute_script("arguments[0].focus()", projectLink)
    time.sleep(1)
    restoreProject(1)
    time.sleep(1)
    driver.back()
    time.sleep(1)
    driver.refresh()

print("good bye!")
driver.close()
