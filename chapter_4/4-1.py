# 웹에 있는 리소스 추출하기
import requests

r = requests.get("http://rank.search.naver.com/rank.js")
r.status_code
r.text

json = r.json()
for rank in json["data"][0]["data"]:
    print(rank["rank"], "", rank["keyword"])

