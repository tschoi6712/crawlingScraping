# MySQL 접속하기
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

# 데이터 저장하기
cur.execute("INSERT INTO books VALUES(%s, %s)", ("처음 시작하는 파이썬 프로그래밍", "https://example.com"))

# 커밋하기
con.commit()

# 연결 종료하기
con.close()