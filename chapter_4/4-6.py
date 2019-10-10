# 분석한 결과 저장하기
import feedparser
import MySQLdb

# 데이터베이스 연결하기
con = MySQLdb.connect(
    user="root",
    passwd="1234",
    host="localhost",
    db="scrapingdata",
    charset="utf8")

# 커서 생성하기
cur = con.cursor()

# 실행할 때마다 다른 결과가 나오지 않게 테이블을 제거해두기
cur.execute("DROP TABLE IF EXISTS books")

# 테이블 생성하기
cur.execute("CREATE TABLE books (title text, url text)")

# URL을 지정해서 FeedParserDict 객체 생성하기
rss = feedparser.parse("http://www.aladin.co.kr/rss/special_new/351")

# RSS 버전 확인하기
print(rss.version)

# 피드의 제목
print(rss["feed"]["title"])

# 반복 적용
for content in rss["entries"]:
    # 데이터 저장하기
    cur.execute("INSERT INTO books VALUES(%s, %s)", (content["title"], content["link"]))

# 커밋하기
con.commit()

# 연결 종료하기
con.close()