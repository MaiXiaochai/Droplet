# -*- coding:utf-8 -*-

import toml
import sqlalchemy
from sqlalchemy import create_engine, Column, String,Integer,Table,MetaData,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, mapper


# 导入配置信息
CONF_PATH = './config.toml'
conf = toml.load(CONF_PATH, _dict=dict)
test_dsn = conf.get('oracle').get('test_dsn')

# 创建实例连接数据库
engine = create_engine('oracle://{}'.format(test_dsn))

conn = engine.connect()
res = conn.execute("select * from test_a")
for i in res:
    print(i)

if __name__ == '__main__':
    pass