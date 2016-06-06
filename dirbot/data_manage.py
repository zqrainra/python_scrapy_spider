#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date	: 2016-05-25
__author__ = 'Bob'
import time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,TIMESTAMP,TEXT
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.sql import exists

engine = create_engine("mysql+mysqlconnector://www:123456@localhost/news_spider")
Base = declarative_base()

class Content(Base):
    __tablename__ = 'content'
    id = Column(Integer, primary_key=True)
    title = Column(String(256))
    abstract = Column(String(1024))
    ptime = Column(String(24))
    content = Column(TEXT)
    img_url = Column(String(256))

    def get_content(self,want):
        SessionCls = sessionmaker(bind=engine)
        session = SessionCls()
        # content = Content()
        # print session.query(exists().where(content.title == want)).scalar()
        # print res
        res = session.query(Content).filter(Content.title == want).all()
        if len(res) == 0:
            return False
        else:
            return True



if __name__ == '__main__':
    # SessionCls = sessionmaker(bind=engine)
    # session = SessionCls()
    content = Content()
    content.get_content('123')
    # content.abstract = '案说法'
    # content.ptime = time.time()
    # content.content = 'ceshi content'
    # content.title = '测试主题'
    # session.add(content)
    # session.commit()
    # Base.metadata.create_all(engine)
