from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.bestbuy.ca/en-ca/product/insignia-portable-air-conditioner-12000-btu-white-grey-only-at-best-buy/11794998")
