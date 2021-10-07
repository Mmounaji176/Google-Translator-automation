
from time import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

text = input("write a text : ")
print("you want to translate that to : ")
choice =int(input("1: Ar 2:fr 3:An  "))
if choice==1:
    lang='ar'
elif choice==2:
    lang="fr"
elif choice==3:
    lang="en"

path = "C:\Program Files (x86)\chromedriver.exe"
driver= webdriver.Chrome(path)
driver.get(f"https://translate.google.com/?sl=auto&tl="+lang+"&op=translate")
driver.find_element_by_tag_name("textarea").send_keys(text)

try:   
    result = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,'.J0lOec .VIiyi span span')) 
        )
    print(result.text)
    driver.implicitly_wait(30)
finally:
        driver.quit()





