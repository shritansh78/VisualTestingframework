
## INTRODUCTION

The goal is to compare screenshots of web pages taken before and after deployment to identify any visual differences and generate a report for further analysis.


## CODE EXPLANATION

The code reads a CSV file named 'input.csv' to fetch the URLs of web pages to be tested.

The code creates three folders: 'Before_deployment', 'After_deployment', and 'changes_detected' if they don't already exist. These folders will store the screenshots and marked images.

The code iterates through each web page URL and takes a screenshot of the page before deployment using the WebDriver. The screenshots are saved in the 'Before_deployment' folder.

After the deployment, the code again visits each web page URL and captures a screenshot using the WebDriver. The screenshots are saved in the 'After_deployment' folder.

The code then compares the before and after screenshots using the structural similarity index (SSIM) and mean absolute error (MAE) metrics. It calculates these metrics by converting the images to NumPy arrays.

Additionally, the code marks areas of visual changes between the before and after screenshots by drawing rectangles around the differences. The marked images are saved in the 'changes_detected' folder.

The results are then converted into a pandas DataFrame for further analysis and SSIM, MAE index results are saved in the 'output.csv' file.


## Structural Similarity Index (SSIM):

The SSIM is a metric commonly used to measure the structural similarity between two images. It takes into account the luminance, contrast, and structure of the images.
The SSIM value ranges between -1 and 1, where 1 indicates a perfect match or similarity, and -1 indicates complete dissimilarity.
In the code, the compare_ssim function from the skimage.metrics module calculates the SSIM between the before and after screenshots.
The win_size parameter specifies the size of the sliding window used for SSIM calculation.
The multichannel=True parameter indicates that the SSIM calculation should consider each color channel separately, which is suitable for RGB images.



## Mean Absolute Error (MAE):

The MAE is a metric that measures the average difference between corresponding pixel values of two images.
It provides a quantitative measure of the overall pixel-level difference between two images, regardless of their structural similarity.
The MAE value is a non-negative scalar value, with a higher value indicating a greater difference between the images.
In the code, the MAE is calculated by taking the mean absolute difference between corresponding pixels in the before and after screenshots.


These metrics, SSIM and MAE, are calculated to objectively quantify the visual differences between the before and after deployment screenshots. They provide numerical values that can be used to compare different web pages or track changes over time. 





## Execution Steps:
1. In the input.xls file, enter the URL(s) of Webpages to be used for detection.
2. Double-click on the batch file named Beforescript_screenshot_comparison.bat, it will install all the dependencies on the system.
3. Double-click on the batch file named Afterscript_screenshot_comparison.bat .
