# -*- coding:utf-8 -*-

import toml
import sqlalchemy
from sqlalchemy import create_engine, MetaData, ForeignKey, Table, Column, String, Integer, Float, Date, Time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, mapper

Base = declarative_base()


class MyORM(object):
    def __init__(self, _conf_path):
        # 导入配置信息
        conf = toml.load(_conf_path, _dict=dict)
        dsn = 'oracle://' + conf.get('oracle').get('test_dsn')
        engine = create_engine('{}'.format(dsn))
        self.session = sessionmaker(bind=engine)

    def get_session(self):
        return self.session


class TestA(Base):
    __tablename__ = 'test_a'
    id = Column(Integer)
    name = Column(String(100))
    counter = Column(Integer)
    sdate = Column(Date)
    cost = Column(Float)


def my_test():



if __name__ == "__main__":
    conf_path = './config.toml'
