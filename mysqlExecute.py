# -*- coding: utf-8 -*-
"""
==============================
   Date:           01_26_2018  10:10
   File Name:      /GitHub/mysqlExecute
   Creat From:     PyCharm
   Python version:   
- - - - - - - - - - - - - - - 
   Description:
==============================
"""

__author__ = 'Loffew'

import pymysql


class MySqler:
    def __init__(self, host, port, user, passwd, db_name, charset):
        self.db_name = db_name
        self.conn = pymysql.connect(host, port, user, passwd, charset)
        self.creat_database(db_name)

    def close(self):
        """
        在最后需要退出数据库
        """
        self.conn.close()

    def creat_database(self, db_name):
        """
        创建一个数据库，初始化的时候，默认创建（如果已有则返回警告）
        :param db_name: 要创建的数据库
        """
        with self.conn as cur:
            sql = "create database if not exists %s charset utf8;" % db_name
            cur.execute(sql)

    def creat_table(self, db_name, table_name):
        """
        在当前数据库下创建表
        :param db_name: 要创建表名的数据库(先创建测试)
        :param table_name: 要创建的表名
        """
        self.creat_database(db_name)
        with self.conn as cur:
            cur.execute("use {};".format(db_name))
            sql = "create table if not exists %s (id int);" % table_name
            cur.execute(sql)

    def add_field(self, db_name, table_name, **kwargs):
        """
        在表内创建内容
        :param db_name:
        :param table_name:
        :param kwargs:
        :return:
        """
        with self.conn as cur:
            for key, value in kwargs.items():
                sql = "alter table %s.%s add column %s %s;" % (db_name, table_name, key, str(value))
                cur.execute(sql)

