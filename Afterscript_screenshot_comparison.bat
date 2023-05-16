@echo off



rem Run the Python script
echo Running the Python script...
python Afterscript_screenshot_comparison.py
echo Afterscript_screenshot_comparison script execution completed.
echo SSIM and MAE comparision results are printed on console
echo Check the After_deployment folder for the post build deployment screenshot. 
echo Check changes_detected folder for the changes detected during Image comparision are marked with rectangle. 

echo Also results can be checked on the output excel file.

pause