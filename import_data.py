#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2021/9/28 5:12 下午
# @File  : import_data.py
# @Author: johnson
# @Desc  : 测试导入数据到neo4j
import os
from neo4j import GraphDatabase, basic_auth
import contextlib

url = os.getenv("NEO4J_URI", "bolt://localhost:7687")
username = os.getenv("NEO4J_USER", "movies")
password = os.getenv("NEO4J_PASSWORD", "movies")
neo4jVersion = os.getenv("NEO4J_VERSION", "4")
database = os.getenv("NEO4J_DATABASE", "movies")

driver = GraphDatabase.driver(url, auth=basic_auth(username, password))


@contextlib.contextmanager
def open_session(database=None, neo4jVersion="4"):
    # __enter__方法
    print('开启session')
    if neo4jVersion.startswith("4"):
        neo4j_db = driver.session(database=database)
    else:
        neo4j_db = driver.session()
    # 【重点】：yield
    yield neo4j_db

    # __exit__方法
    print('关闭session')
    neo4j_db.close()
    return

def test_query():
    """
    测试一个查询，查询是否有一个叫Tom Hanks的人
    :return:
    :rtype:
    """
    with open_session(database=database, neo4jVersion=neo4jVersion) as db:
        results = db.read_transaction(lambda tx: list(tx.run('MATCH (tom {name: "Tom Hanks"}) RETURN tom')))
        for record in results:
            print(record)

if __name__ == '__main__':
    test_query()