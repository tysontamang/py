from selenium import webdriver
from selenium.webdriver.common.by import By
from getpass import getpass
import pyautogui as pg
import time

# we will create our driver
driver =  webdriver.Firefox()


# we will open our website
driver.get("https://www.fb.com/messages/t/")

email_input = driver.find_element(By.ID,"email")
password_input = driver.find_element(By.ID,"pass")
login_button = driver.find_element(By.ID,"loginbutton")

email=input("Facebook username/email: ")
password=getpass()
contacts=[]
print("                ***GIVE TWO SPACE FOR MULTIPLE FRIEND NAMES ***\n"+"For eg. computer engineering1  computer engineering2")
contacts = [item for item in input("friend names: ").split("  ")]
sabda=input("your messages: ")
print("                ***GO TO THE FIREFOX AND SIT BACK ***")
print("                ***Like Our page https://www.facebook.com/ComputerEngin33ring ***")
email_input.send_keys(email)
password_input.send_keys(password)
login_button.click()

#writing in the search area
time.sleep(10)
for i in contacts:
	search = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div/div/div/div/div/label/input')
	search.send_keys(i)

		
	#click on the first account
	time.sleep(10)
	account=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div[1]/ul/li[1]/ul/li[2]/div/a/div/div[2]/div/div/span')
	account.click()

	#writing a message
	time.sleep(5)
	msg=driver.find_element(By.CSS_SELECTOR,'.x14wi4xw')
	#msg=driver.find_element(By.CSS_SELECTOR,'./html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/div[1]/div/div/div/div[1]/div[2]/div/div/div[2]/div/div/div[4]/div[2]/div/div/div[1]')
	
	pg.typewrite(sabda)

	#pressing send
	time.sleep(3)
	send=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/div/span[2]/div')
	send.click()



