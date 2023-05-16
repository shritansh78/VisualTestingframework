import os
from PIL import Image
from selenium import webdriver
from skimage.metrics import structural_similarity as compare_ssim
import numpy as np
import pandas as pd
from PIL import ImageDraw

# set up the web driver
driver = webdriver.Chrome()

# read URLs from input CSV file
input_df = pd.read_csv('input.csv')
web_pages = input_df['URL'].tolist()

# create the After_deployment folder if it doesn't exist
if not os.path.exists('After_deployment'):
    os.makedirs('After_deployment')

# create the changes_detected folder if it doesn't exist
if not os.path.exists('changes_detected'):
    os.makedirs('changes_detected')


# take screenshots of each web page after deployment and save them to the After_deployment folder
for page in web_pages:
    driver.get(page)
    screenshot_name = os.path.join('After_deployment', page.replace('https://', '').replace('/', '_') + '.png')
    driver.save_screenshot(screenshot_name)

# compare the screenshots and generate a report
results = []
for page in web_pages:
    before_screenshot = Image.open(os.path.join('Before_deployment', page.replace('https://', '').replace('/', '_') + '.png'))
    after_screenshot = Image.open(os.path.join('After_deployment', page.replace('https://', '').replace('/', '_') + '.png'))

    # convert the images to numpy arrays
    before_arr = np.array(before_screenshot)
    after_arr = np.array(after_screenshot)

    # calculate the structural similarity index (SSIM) between the before and after screenshots
    score, diff = compare_ssim(before_arr, after_arr, win_size=3, full=True, multichannel=True)

    # calculate the mean absolute error (MAE) between the before and after screenshots
    # calculate the mean absolute error (MAE) between the before and after screenshots
    mae = np.mean(np.abs(before_arr - after_arr))

    # add the test results to the list
    results.append({'Page': page, 'SSIM Score': score, 'MAE': mae})

    # mark the areas with rectangles where the changes are observed
    diff_image = Image.fromarray((diff * 255).astype(np.uint8))
    bbox = diff_image.getbbox()
    if bbox:
        marked_image = after_screenshot.copy()
        marked_image.thumbnail((marked_image.size[0] // 2, marked_image.size[1] // 2))  # Scale down the image
        marked_image_draw = ImageDraw.Draw(marked_image)
        marked_image_draw.rectangle(bbox, outline='red', width=3)
        changes_screenshot_name = os.path.join('changes_detected', page.replace('https://', '').replace('/', '_') + '.png')
        marked_image.save(changes_screenshot_name)

# close the web driver
driver.quit()

# generate a report using pandas dataframe and save to output CSV file
output_df = pd.DataFrame(results)
output_df.set_index('Page', inplace=True)
output_df.to_csv('output.csv')
print(output_df)
