from selenium import webdriver
 
from PIL import Image
 
# Here Chrome  will be used
driver = webdriver.Chrome()
 
# URL of website
url = "https://www.geeksforgeeks.org/"
 
# Opening the website
driver.get(url)
 
driver.save_screenshot("image.png")