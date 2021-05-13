import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from wordcloud import WordCloud

from PIL import Image
import numpy as np

driver = webdriver.Chrome("C:/Users/USER/Downloads/chromedriver_win32\chromedriver.exe")
driver.get('https://www.genie.co.kr/chart/top200')

html=driver.page_source
soup = BeautifulSoup(html, 'html.parser')

text=""

musics=soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for music in musics :
    title = music.select_one('td.info > a.title.ellipsis').text.strip() #strip :공백삭제
    rank=music.select_one('td.number').text[0:2].strip()
    singer=music.select_one('td.info > a.artist.ellipsis').text.strip()
    text+=singer

    print(rank,title,singer)


cat_mask=np.array(Image.open('C:/Users/USER/Desktop/crawling_prac/고양이.jpg'))


font_path = 'C:/Windows/Fonts/MALGUNBD.TTF'

wc = WordCloud(font_path=font_path, background_color="white", width=600, height=400,
mask=cat_mask)
wc.generate(text)

wc.to_file("geniemusic_wordcloud.png")
