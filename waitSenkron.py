import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
#driver.implicitly_wait(30) # element bekleme süresi
driver.get("https://pynishant.github.io/Selenium-python-waits.html")

tryit = driver.find_element(By.XPATH, "//button[contains(text(), 'Try it')]").click()

WebDriverWait(driver, 45).until(expected_conditions.presence_of_element_located((By.XPATH, "//button[contains(text(), 'CLICK ME')]")))

clickme = driver.find_element(By.XPATH, "//button[contains(text(), 'CLICK ME')]")
time.sleep(5)

alert = Alert(driver)
alert.accept()

#presence ve visibility
#implicit wait
#explicit wait
#url_cahange
#ignored_exceptions gormezden geleceği exceptionlar

time.sleep(10)  # Tarayıcıyı 10 saniye açık tutar
