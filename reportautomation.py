from selenium import webdriver as wb
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pyautogui
import time


#where to download
o=Options()
o.add_experimental_option("prefs",{"download.default_directory": "Enter the location(folder) where the you want to download the report files"})

cd = "Enter the location where the chromedriver is situated"

#website
url = 'Enter the url of the site(Elab)'

d = wb.Chrome(cd,chrome_options=o)
d.get(url)

user = 'Enter Register Number'
pas = 'Enter Password'

#enter user and password
d.find_element_by_id('mat-input-0').send_keys(user)
d.find_element_by_id('mat-input-1').send_keys(pas)

#login
d.find_element_by_class_name('mat-raised-button').click()

#enter question wheel
time.sleep(5)
pyautogui.click(309, 480)

#openning 1st question
time.sleep(3)
pyautogui.click(693, 386)

#questions begin from here

#for the first time:
	#choose language (cpp)
time.sleep(2)
pyautogui.click(440,291)

time.sleep(1)
pyautogui.click(392,339)

time.sleep(1)
end = d.find_element_by_tag_name('html')
end.send_keys(Keys.END)

	#click evaluate
time.sleep(1)
pyautogui.click(952,693) #for the first time
	#pyautogui.click(942, 649) for rest of the programs

time.sleep(3)
end.send_keys(Keys.END)

	#download report
time.sleep(1)
pyautogui.click(1266,524)
	#pyautogui.click((1270,496) for rest of the programs

#going to next question
time.sleep(1)
end.send_keys(Keys.HOME)

	#next question
time.sleep(1)
pyautogui.click(1290,216)

for i in range(99):

	#choose language (cpp)
	time.sleep(2)
	pyautogui.click(440,291)

	time.sleep(1)
	pyautogui.click(392,339)

	time.sleep(1)
	end = d.find_element_by_tag_name('html')
	end.send_keys(Keys.END)

	#click evaluate
	time.sleep(1)
	#pyautogui.click(952,693) for the first time
	pyautogui.click(942, 649)

	time.sleep(3)
	end.send_keys(Keys.END)

	#download report
	time.sleep(1)
	#pyautogui.click(1266,524) for the first time
	pyautogui.click(1270,496)

	#going to next question
	time.sleep(1)
	end.send_keys(Keys.HOME)

	#next question
	time.sleep(1)
	pyautogui.click(1290,216)

d.close()