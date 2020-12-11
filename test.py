from bs4 import BeautifulSoup #data scraping
import requests #data scraping
import time

from selenium import webdriver
driver = webdriver.Chrome(r'C:\Users\dangk\Downloads\chromedriver_win32\chromedriver.exe')
driver.get('https://osu.ppy.sh/beatmapsets')



mySet = {''}

for j in range (0, 10):
    time.sleep(1)
    
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    links = soup.findAll('a', class_="beatmapset-panel__header")

    for i in links:
        print(i.get('href'))
        mySet.add(i.get('href'))
    print(len(links))

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    
print(mySet, len(mySet))
