from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


chrome_options = Options()
chrome_options.add_argument("--headless")  #

driver = webdriver.Chrome(options=chrome_options)

# Open the website
url = "https://fr.wikipedia.org/wiki/Alger"
driver.get(url)


table_element = driver.find_element(By.CSS_SELECTOR, "table.infobox_v2.noarchive")


rows = table_element.find_elements(By.TAG_NAME, "tr")


population = rows[14].find_element(By.TAG_NAME, "td").text


print("Population:", population)

# Close the driver
driver.quit()