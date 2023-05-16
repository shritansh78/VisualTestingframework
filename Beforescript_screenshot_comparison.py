import os
from selenium import webdriver
import pandas as pd

# set up the web driver
driver = webdriver.Chrome()

# read URLs from input CSV file
input_df = pd.read_csv('input.csv')
web_pages = input_df['URL'].tolist()

# create the Before_deployment folder if it doesn't exist
if not os.path.exists('Before_deployment'):
    os.makedirs('Before_deployment')

# take screenshots of each web page before deployment and save them to the Before_deployment folder
for page in web_pages:
    driver.get(page)
    screenshot_name = os.path.join('Before_deployment', page.replace('https://', '').replace('/', '_') + '.png')
    driver.save_screenshot(screenshot_name)

# close the web driver
driver.quit()
