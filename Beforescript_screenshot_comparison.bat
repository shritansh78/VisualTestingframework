@echo off

rem Install dependencies
echo Installing dependencies...
python -m ensurepip
python -m pip install --upgrade pip
python3 -m pip install --upgrade pip
pip install selenium
pip install pillow
pip install pandas
pip install numpy
pip install scikit-image

echo Dependencies installed successfully.

rem Run the Python script
echo Running the Python script...
python Beforescript_screenshot_comparison.py
echo Beforescript_screenshot_comparison script execution completed.
echo Check the Before_deployment folder for the pre build deployment screenshot. 

pause