from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# sudo apt install chromium-browser

class Webscrape:
  def __init__(self, option=''):
    chromeOptions = Options()
    if option != 'debug':
      chromeOptions.add_argument('--headless')
    self.driver = webdriver.Chrome(executable_path = '/usr/lib/chromium-browser/chromedriver', options=chromeOptions)
  
  def checkPage(self, websiteURL, keyword):
    self.driver.get(websiteURL)
    sourceText = self.driver.page_source
    return (keyword.lower() in sourceText.lower())
