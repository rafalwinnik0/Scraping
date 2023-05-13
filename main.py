from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver = "/Users/rafael/Downloads/chromedriver_mac64"
service = Service(executable_path=chrome_driver)

dict = {}

with webdriver.Chrome(service=service) as driver:
    driver.get("https://python.org")

    time_table = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
    name_table = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
    for n in range(len(time_table)):
        dict[n] = {
            "date": time_table[n].text,
            "name": name_table[n].text
        }

