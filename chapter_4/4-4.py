# RSS로 스크레이핑하기
import feedparser

# URL을 지정해서 FeedParserDict 객체를 생성
rss = feedparser.parse("http://www.aladin.co.kr/rss/special_new/351")

# RSS의 버전을 출력
print(rss.version)
print(rss)

print(rss["feed"])
# 피드의 제목 출력
print(rss["feed"]["title"])
# 엔트리(item 요소) 확인
print(rss["entries"])

# 엔트리들의 제목과 링크를 출력
for content in rss["entries"]:
    print(content["title"])
    print(content["link"])
