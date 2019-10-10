"""데이터베이스를 만들고 테이블 등록하기"""
import MySQLdb

# 데이터베이스 연결하기
con = MySQLdb.connect(
    user="root",
    passwd="1234",
    host="localhost",
    db="quotes",
    charset="utf8")

# 커서 생성하기
cur = con.cursor()

# SQL_QUERY
#mysql> CREATE DATABASE quotes;
#mysql> USE quotes;

query = """
DROP TABLE IF EXISTS quotes;
CREATE TABLE quotes (
    id int(11) unsigned NOT NULL AUTO_INCREMENT,
    author varchar(255) DEFAULT NULL,
    text text,
    text_hash char(64) DEFAULT NULL,
    created timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY (text_hash)
    ) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
    

DROP TABLE IF EXISTS tags;
CREATE TABLE tags (
    id int(11) unsigned NOT NULL AUTO_INCREMENT,
    name varchar(255) NOT NULL DEFAULT '',
    created timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY (name)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
    
DROP TABLE IF EXISTS quotes_tags;
CREATE TABLE quotes_tags (
    id int(11) unsigned NOT NULL AUTO_INCREMENT,
    quotes_id int(11) NOT NULL,
    tags_id int(11) NOT NULL,
    author varchar(255) DEFAULT NULL,
    created timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY (quotes_id, tags_id)
    ) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;
"""
cur.execute(query)

# 커밋하기
con.commit()

# 연결 종료하기
con.close()