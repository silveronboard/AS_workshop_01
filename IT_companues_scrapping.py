import json
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "https://www.gov.pl/web/poland-businessharbour-en/itspecialist"

driver = webdriver.Chrome()
driver.implicitly_wait(25)
driver.get(link)
#try:
elements = driver.find_element(By.XPATH, '//*[@id="main-content"]/div[2]/div[2]').text
nelements = len( elements.split(sep="\n") )
print(nelements)
for i in range (1, nelements + 1):
#    print(i)
    element1 = driver.find_element( By.XPATH, '//*[@id="main-content"]/div[2]/div[2]/div['+ str( i ) + ']' ).text
    try:
        website = driver.find_element( By.XPATH, '//*[@id="main-content"]/div[2]/div[2]/div['+ str( i ) + ']/details/div/p[1]/a' ).text
        email = driver.find_element( By.XPATH, '//*[@id="main-content"]/div[2]/div[2]/div['+ str( i ) + ']/details/div/p[2]/a' ).text
        print("web found")
    except:
        email = driver.find_element( By.XPATH, '//*[@id="main-content"]/div[2]/div[2]/div['+ str( i ) + ']/details/div/p/a' ).text
        print("web not found")
    print(element1,website,email)


#print("Unable to find element")
driver.close()
