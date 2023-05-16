from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://media.naver.com/press"

driver = webdriver.Chrome(executable_path="chromedriver")

driver.get(URL)

pressElements = driver.find_elements(By.CSS_SELECTOR, "ul.press_list_only_logo li a")


def getPress(pressElement):
    pressName = pressElement.find_element(By.TAG_NAME, "img").get_attribute("alt")
    pressCode = pressElement.get_attribute("data-office-id")

    return {"name": pressName, "code": pressCode}


presses = list(map(getPress, pressElements))

# for press in presses:
press = presses[0]
newDriver = webdriver.Chrome(executable_path="chromedriver")
newDriver.get(URL + "/" + press["code"] + "?sid=100")

print(URL + "/" + press["code"] + "?sid=100")
elements = newDriver.find_elements(By.CSS_SELECTOR, "span.press_edit_news_title")

for element in elements:
    print(element.text)
