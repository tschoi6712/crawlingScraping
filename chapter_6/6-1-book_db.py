"""데이터베이스를 만들고 테이블 등록하기"""
import MySQLdb

# 데이터베이스 연결하기
con = MySQLdb.connect(
    user="root",
    passwd="1234",
    host="localhost",
    db="book_db",
    charset="utf8")

# 커서 생성하기
cur = con.cursor()

# SQL_QUERY
#mysql> CREATE DATABASE book_db;
#mysql> USE book_db;

query = """
DROP TABLE IF EXISTS languages;
CREATE TABLE languages (
    id int(11) unsigned NOT NULL AUTO_INCREMENT,
    name varchar(8) NOT NULL DEFAULT '',
    created timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    updated timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
    ) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
    
INSERT INTO languages (id, name)
            VALUES (1, '한국어'), (2, '영어');

DROP TABLE IF EXISTS publishers;
CREATE TABLE publishers (
    id int(11) unsigned NOT NULL AUTO_INCREMENT,
    name varchar(128) NOT NULL DEFAULT '',
    created timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    
INSERT INTO publishers (id, name)
            VALUES (1, '위키북스'), (2, '한빛미디어'), (3, 'Addison-Wesley');

DROP TABLE IF EXISTS books;
CREATE TABLE books (
    id int(11) unsigned NOT NULL,
    publisher_id int(11) NOT NULL,
    title varchar(255) NOT NULL DEFAULT '',
    language_id int(11) NOT NULL,
    created timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    
INSERT INTO books (id, title, publisher_id, language_id)
            VALUES 
                (34973284, 'HTML5 웹 프로그래밍 입문', 2, 1), 
                (57556147, 'Hello Coding 파이썬', 2, 1), 
                (71051687, '파이썬을 이용한 머신러니으 딥러닝 실전 앱 개발', 1, 1),
                (32604814, 'The Art of Computer Programming 5', 3, 2);
"""
cur.execute(query)

# 커밋하기
con.commit()

# 연결 종료하기
con.close()