from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import time
import private
import os
import shutil

URL = 'https://projects.invisionapp.com/d/main#/projects'

options = webdriver.ChromeOptions()

base_dir = private.downloadDir + "/Invision"
if os.path.exists(base_dir):
    shutil.rmtree(base_dir)
os.makedirs(base_dir)

prefs = {'download.default_directory' : base_dir}
options.add_experimental_option('prefs', prefs)

ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
# timeout after 20 seconds
wait  = WebDriverWait(driver, 20)
actions = ActionChains(driver)
driver.set_window_position(0, 0)
driver.set_window_size(2000, 1200)

# Move file from base download dir to selected dir
def move_png_file(currentdir, movedir):
    source = os.path.join(currentdir)
    sort = os.path.join(movedir)
    for f in os.listdir(source):
        if f.endswith((".png",".jpg",".jpeg")):
            shutil.move(os.path.join(source, f), sort)

try:
    driver.get(URL)
    emailField = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="emailAddress"]')))
    pwField = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]')))
    emailField.send_keys(private.username)
    pwField.send_keys(private.pw)
    submitButton = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@class="main-panel__content"]/form/div[3]/button')))
    submitButton.click()

    time.sleep(10)
    
    # Get Last Page value
    last_page_value = driver.find_element(By.XPATH, "//*[@class='projects-pagination at-start']/li[10]/span")
    last_page_value = int(last_page_value.text)

    # Get current page value
    current_page_value = driver.find_element(By.XPATH, "//*[@class='current']/span")
    current_page_value = int(current_page_value.text)

    page_urls = {}

    # Gather Prototype URL's 
    for current_page_index in range(1, last_page_value+1):
        time.sleep(1)
        prototype_view_btn = driver.find_elements(By.XPATH, "//*[@class='tile-container']/div[@class='projects__project__wrapper projects__project__wrapper--prototype']")
        prototype_view_btn = prototype_view_btn[0].find_elements(By.XPATH, "//*[contains(text(), 'View prototype')]")
        page_urls[current_page_index] = {}
        # Append urls
        for current_prototype_tile_index in range(0, len(prototype_view_btn)):
            page_urls[current_page_index][prototype_view_btn[current_prototype_tile_index].get_attribute('href')] = {}

        time.sleep(1)
        if current_page_index < last_page_value:
            next_page_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@class='projects-pagination at-start']/li[@class='next']"))) if current_page_index < 2 else wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@class='projects-pagination']/li[@class='next']")))
            next_page_button.click()

    print("Gathered Prototypes")

    # Gather PNG Preview Links 
    for current_page_index in range(1, last_page_value+1):
        time.sleep(1)
        for key, value in page_urls[current_page_index].items():
            driver.get(key)
            time.sleep(1)
            prev_buttons = []
            preview_buttons = driver.find_elements(By.XPATH, "//*[@class='view-screen-wrap']/a")
            if len(preview_buttons) > 0:
                for prev_index in range(0, len(preview_buttons)):
                    prev_buttons.append(preview_buttons[prev_index].get_attribute("href"))
            prototype_name = driver.find_element(By.XPATH, "//*[@class='project-name']/h2")
            page_urls[current_page_index][key]["images"] = prev_buttons
            page_urls[current_page_index][key]["name"] = prototype_name.text
        
    print("PNG preview links gathered")
    
    # Download prototype images
    for current_page_index in range(1, last_page_value+1):
        # Count the total divs on page
        time.sleep(1)
        
        for key, value in page_urls[current_page_index].items():
            new_dir_name = """/{s}""".format(s=value['name'])
            current_download_dir = base_dir + new_dir_name
            if not os.path.exists(current_download_dir):
                os.makedirs(current_download_dir)
            for image_url in value['images']:
                # Start
                driver.get(image_url);
                time.sleep(1)
                download_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@class='list-item download-screen']/a")))
                download_button.click()
                time.sleep(1)
                move_png_file(base_dir, current_download_dir)
            print("Folder finished downloading =", new_dir_name)

    print("Finished downloading files!")
    driver.close()

except TimeoutException as ex:
    print("Exception has been thrown." + str(ex))
    driver.close()
