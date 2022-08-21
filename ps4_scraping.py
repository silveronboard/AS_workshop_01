from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://livekaarten.nl/en/Playstation-card-Nederland")
elements = driver.find_elements(By.CLASS_NAME, 'details')
dictionary = ['[\n']
for element in elements[1:]:
    name = element.text.split(sep='\n')[0]
    price = element.text.split(sep='\n')[1]
    dictionary.append('    {\n        "name": "' + name + '",' + '\n        "price": "' + price + '"\n    },\n')
dictionary.append("\n]")
with open("sample.json", "w") as outfile:
    for record in dictionary[:-2]:
        outfile.write(record)
    outfile.write((dictionary[-2])[:-2])
    outfile.write(dictionary[-1])
print("Complete!")
driver.close()
