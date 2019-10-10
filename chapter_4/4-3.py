import requests
from lxml import html

# HTML 소스 코드를 읽어 들입니다.
r = requests.get("http://wikibook.co.kr/python-for-web-scraping/")

type(r.text)
len(r.text)
print(r.text)


# fromstring(html코드를 Element라는 클래스 구조로 치환)
root = html.fromstring(r.text)

# XPath를 사용해서 요소를 추출
contents = root.xpath('//*[@id="content"]/div[1]/div[2]/h1')

# 리스트의 첫 번째 요소가 가진 텍스트를 출력
print(contents[0].text)
print(contents[0].tag)
print(contents[0].attrib)

# 각 인터넷 서점으로 이동하는 링크 : CSS 선택자를 사용해서 요소를 추출
links = root.cssselect('#book-stores > li > a')

## 추출한 요소의 href 속성을 추출
for link in links:
    print(link.attrib["href"])
