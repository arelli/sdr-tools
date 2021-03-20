#automated script to produce a heatmap and open it in Chrome browser every few seconds.
#You need to have the geckodriver.exe and chromedriver.exe in the same folder as the live_view.py
#You are also required to install PIL for the heatmap creation(using pip) and selenium(also using pip)
#for controlling the web browser.
#Finally, you have to add the folder that the gecko and chrome drivers are in the PATH(or usr/bin for unix-like systems)
#Rafail Ellinitakis, 2021

import subprocess
import time
from selenium import webdriver

print("Creating initial heatmap...")
subprocess.call([r'makegraph.bat'])

driver = webdriver.Chrome()
driver.get('file:///C:/Users/Rafael/Desktop/SDR_Heatmap_Win10/rtl_power%20and%20stuff/rtl-sdr/spitisofias.png')
while True:
	print("********************************************************")
	print("Calling Subprocess to execute .bat version of heatmap.py")
	print("********************************************************")
	subprocess.call([r'makegraph.bat'])
	print("********************************************************")
	print("Done with the image.. Sleep for 20 seconds:")
	print("********************************************************")
	time.sleep(20)
	print("********************************************************")
	print("Refreshing...")
	print("********************************************************")
	driver.refresh()
	driver.execute_script("document.body.style.zoom='500%'")  # this has to be calculated from the image dimensions, to fill the browser exactly on the vertical axis
driver.quit()