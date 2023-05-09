from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://media.naver.com/press"

driver = webdriver.Chrome(executable_path='chromedriver')

driver.get(URL)

pressElements = driver.find_elements(By.CSS_SELECTOR, "ul.press_list_only_logo li a")

def getPress(pressElement):
    pressName = pressElement.find_element(By.TAG_NAME, "img").get_attribute("alt")
    pressCode = pressElement.get_attribute("data-office-id")

    return {"name": pressName, "code": pressCode}



presses = list(map(getPress, pressElements))

for press in presses:
    print(press)