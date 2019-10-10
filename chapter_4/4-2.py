# HTML 소스 분석하기
import requests
from bs4 import BeautifulSoup

r = requests.get("http://wikibook.co.kr/python-for-web-scraping")
r.status_code
r.text

# //*[@id="content"]/div[1]/div[2]/h1

bs = BeautifulSoup(r.content, "html.parser")
title = bs.select('#content > div:nth-child(1) > div.col-md-9 > h1')
print(title.text)

