from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.comon.by import By
# from selenium.webdriver.comon.action_chains import ActionChains
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
import time



driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.daraz.com.bd/groceries-laundry-household-laundry-washing-liquid/")

time.sleep(10)