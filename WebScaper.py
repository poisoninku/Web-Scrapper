import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(r'C:\Users\Administrator\Desktop\chromedriver-win64\chromedriver.exe'))
driver.get('https://www.yearupalumni.org/s/1841/interior.aspx?sid=1841&gid=2&pgid=440')
results = []
content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')
driver.quit()
paragraphs = []
for element in soup.find_all('p'):
    paragraphs.append(element.text.strip())

df = pd.DataFrame({'Paragraphs': paragraphs})
df.to_csv(r'C:\Users\Administrator\PycharmProjects\WebScrapper\.venv\data.csv', index=False, encoding='utf-8')
