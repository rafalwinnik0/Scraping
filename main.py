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

print(dict)

    # name_table = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
    # for name in name_table:
    #     events.append(name.text)


# table1 = ['2023-05-17', '2023-05-17', '2023-05-25', '2023-05-27', '2023-05-29']
# table2 = ['KX CON [23]', 'PyCon LT 2023', 'PyCon Italia 2023', 'Django Girls Groningen', 'DjangoCon Europe 2023']
# events = {}
#
# for n in range(len(table1)):
#     events[n] = {
#         "date": table1[n],
#         "name": table2[n],
#     }
# print(events)