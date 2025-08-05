# 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import sys

#Main
options = Options()
driver = webdriver.Chrome(options=options)
driver.get("http://google.com")
# assert "test" in driver.title

# עצירה עד שהמשתמש לוחץ Enter
input("לחץ Enter כדי להמשיך...")
