from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
query ="laptop"
file =0
for i in range(1, 5):
    driver.get(f"https://www.flipkart.com/search?q={query}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off&page={i}")

    elems = driver.find_elements(By.CLASS_NAME, "CGtC98")

    print(f"{len(elems)} elements found")
    for elem in elems:
        d = (elem.get_attribute("outerHTML").encode('ascii', 'ignore').decode())
        with open(f"data/{query}_{file}.html", "w", encoding="utf-8") as f:
            f.write(d)
            file += 1
    time.sleep(1)

driver.close()