from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup

ctx = "C:/Users/ezen/PycharmProjects/"
driver = webdriver.Chrome(ctx+"chromedriver")
driver.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
soup = BeautifulSoup(driver.page_source,'html.parser')

all_divs = soup.find_all('div',attrs={'class':'tit3'})
products = [div.a.string for div in all_divs]
for i in products:
    print(i)
driver.close()
