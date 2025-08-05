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
driver.get(sys.argv[1])
# assert "test" in driver.title


# test 20241101
m_list=WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, sys.argv[2] )))
for i in m_list:
    print(i.text)

