from selenium import webdriver
import time
url = "https://aws.amazon.com/ru/"

driver = webdriver.Chrome(executable_path="C:\\Users\\таня\\pythonProject\\24 selenium\\hromedriver_win32.zip")

try:
    driver.get(url=url)
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

