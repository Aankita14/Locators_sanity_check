#using ClassName and Tag Name Locators
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.amazon.de/")

#using for CSS selectors
driver.get("https://de-de.facebook.com/")

driver.maximize_window() #To maximize browser window

sliders= driver.find_elements(By.CLASS_NAME,"a-carousel-card")
print(len(sliders))# 3 Total number of sliders in home page


links=driver.find_elements(By.TAG_NAME,"a")
print(len(links)) # 361 Total number of links

