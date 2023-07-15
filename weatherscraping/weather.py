import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys # Keybinds
#
# from selenium.webdriver.support.ui import WebDriverWait # Waiting
# from selenium.webdriver.support import expected_conditions as EC

options = Options()

# Headless Setting
options.headless = True
options.add_argument("--window-size=1920,1080")

DRIVER_PATH = '/path/to/chromedriver'
driver = webdriver.Chrome(options=options)

city = input('What city do you live in? ')


print("Loading", end='')

url = 'https://www.google.com/search?q=weather+in+' + city
driver.get(url)
print(".", end='')
# Search Bar
try:
    time.sleep(0.5)
    print(".", end='')
    new_city = driver.find_element(By.XPATH, '//*[@id="oFNiHe"]/div/div/div[1]/span[2]').text
    weather = driver.find_element(By.XPATH, '//*[@id="wob_dc"]').text
    tempc = driver.find_element(By.XPATH, '//*[@id="wob_tm"]').text
    precipitation = driver.find_element(By.XPATH, '//*[@id="wob_pp"]').text
    humidity = driver.find_element(By.XPATH, '//*[@id="wob_hm"]').text
    wind = driver.find_element(By.XPATH, '//*[@id="wob_ws"]').text
    print(".", end='\n')

    print('In', new_city, ',,\nWeather:', weather, '\nTemperature:', tempc, 'ºC\nPrecipitation:', precipitation, '\nHumidity:', humidity, '\nWind:', wind)
except:
    print(".", end='\n')
    print("Error, invalid city.")

driver.quit()

