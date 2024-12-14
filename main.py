from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://tomspizzeria.b4a.app/")


def siparisVer():
    driver.find_element(By.ID, "siparis").click()

def mesajOku():
    return driver.find_element(By.ID, "mesaj").text


# müşteri ismi
siparisVer()
mesaj = mesajOku()
assert mesaj == "Müşteri ismi girmediniz"
# müsteri ismi girmediniz

# pizza boyu
# pizza boyu secmediniz

isim = "Emreosminho"
driver.find_element(By.ID, "musteri-adi").send_keys(isim)
siparisVer()
mesaj = mesajOku()
assert mesaj == "Pizza boyu seçmediniz"

# ödeme sekli
# ödeme tipi seçmediniz

driver.find_element(By.CSS_SELECTOR, "input[value='Küçük']").click()
siparisVer()
mesaj = mesajOku()
assert mesaj == "Ödeme tipi seçmediniz"

dropDown = driver.find_element(By.ID, "odeme-tipi")
odeme = Select(dropDown)
odeme.select_by_index(2)
siparisVer()
mesaj = mesajOku()
assert mesaj == "Siparişiniz alındı"



musteri = driver.find_element(By.ID, "musteri").text
boy = driver.find_element(By.ID, "pizzaboyu").text
ek = driver.find_element(By.ID,"pizzaustu").text
odeme = driver.find_element(By.ID,"odeme").text
tutar = driver.find_element(By.ID, "tutar").text

assert musteri == "Müşteri ismi: " + isim
assert boy == "Pizza boyu: Küçük"
assert ek == "Pizza üstü:"
assert odeme == "Ödeme tipi: Kredi Kartı"
assert tutar == "Tutar: 10 TL"

time.sleep(5)
driver.execute_script("window.scrollBy(0,900)","")
time.sleep(10)
driver.save_screenshot("./sonuc1.png")

driver.quit()