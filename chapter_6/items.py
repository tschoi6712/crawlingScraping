"""items.py 크롤링할 데이터를 정의해주는 파일
예제: 격언 스크레이핑 프로그램"""

import scrapy

class Quote(scrapy.Item):
    """격언 아이템"""
    author = scrapy.Field()
    text = scrapy.Field()
    tags = scrapy.Field()